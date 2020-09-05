
# from PIL import Image 
from time import sleep
from time import time
import random
import pyautogui as pag

### internal
from .popupdata import *
from .sreading import *
from .cheats import *
from .kpops import *
from .std import *
from .sdata import *
from .hashdata import *


pag.FAILSAFE = False


class GS:
    x = 0
    y = 0
    w = 1440
    h = 930
    debugging = False           # bool from cli
    args = None                 # args from cli app execution
    systems = set()             # set of system hashes from base review
    click_bases = [1155, 460]   # happy spot for base investment
    max_bases_per_system = 2    # putting this here to override.
    max_bases_to_prune = 95     # putting this here to override.
    time_stale_game = 0         # epoch from last stale game detected 
    time_last_popup = 0         # epoch from last pop killed
    time_last_base = 0          # epoch from last base review
    time_start = 0              # epoch from the start of the game
    popup_msgs = {}
    im_app = None               # current app window image
    mouse_pos = None            # current app mouse location
    stale_next_secs = 5        # after bening stale click next
    dos_box_in_game = True      # do we do the click when search for the dos box?
    system_data = {}
    lost_system_keys = set()


def run():
    app_config()
    look_for_dos_box()
    print(f"New game?   {GS.args.new_game}")
    if GS.args.new_game:
        system_data_delete()
        clear_fleet()
        review_systems()
        print(f"Moo Money Cheat?   {GS.args.mo_money}")
        if GS.args.mo_money:
            mo_money(hunreds=21)
        print(f"Galaxy Cheat?   {GS.args.show_galaxy}")
        if GS.args.show_galaxy:
            show_map_all()
    print(f"Check Systems?   {GS.args.check_systems}")
    if GS.args.check_systems:
        review_systems()
    system_data_read()
    GS.time_stale_game = time()       # stale game 
    GS.time_last_popup = time()       # last popup
    GS.time_last_base = time()        # last base investment review
    GS.time_start = time()            # app start time
    idle_game_string_last = ''                        # the idle game string
    print('Starting "do the clicks loop".')
    try:
        loop_count = 0
        while True:
            ### update stats & kill popups
            loop_count += 1
            datime = time()
            ms_pos = pag.position()
            rel_x = ms_pos.x - GS.x
            rel_y = ms_pos.y - GS.y
            kill_popups()
            system_count = system_data_count()
            idle_game_string = get_idle_game_string()
            last_stale_game_secs = int(datime - GS.time_stale_game)
            last_system_mon_secs = int(datime - GS.time_last_base)
            ### game bar test
            if idle_game_string == '---':
                """
                if '---' then the app window is not at a restful state.
                """
                GS.time_stale_game = time() 
                continue
            elif idle_game_string_last != idle_game_string:
                """
                something is moving on the screen.
                """
                idle_game_string_last = idle_game_string
                GS.time_stale_game = time() 
                GS.stale_next_secs = 5
                continue
            # elif last_stale_game_secs < 2:
            #     continue
            print('finished clicking.')
            ### AUTO STUFF - don't want to do stuff while pops are still running.
            if (last_stale_game_secs <= GS.stale_next_secs 
                    and last_system_mon_secs > (system_count * 3)
                    or system_count == 0):
                play_time = int(datime - GS.time_start)
                print(f'You have been planing for {play_time} seconds and system count is {system_count}.')
                gen_popup_report()
                review_systems()
                GS.time_last_base = time()
                print(f'>>>>>>System Monitoring complete')
            elif last_stale_game_secs <= GS.stale_next_secs:
                print(f'>>>>>>{last_stale_game_secs} stale secs, pointer @ ', (rel_x, rel_y))
            elif last_stale_game_secs > GS.stale_next_secs:
                print('>>>>>>AUTO CLICK BABY!!!')
                pag.press(['n'])
                move_pointer_to_home()
                GS.stale_next_secs = 1
                
            ### quite if -qe
            if GS.args.quick_exit:
                break
    except KeyboardInterrupt:
        print('\nDone.')
