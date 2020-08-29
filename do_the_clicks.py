import moo_auto as ma

"""
Purpose: I really like playing MOO on a "Huge" map, but hate clicking the buttons.  This app will kill all the popups for me.
Goals:
 - Kill technology popups for me. 
"""

def main():
    ma.app_config()
    ma.look_for_dos_box()
    print(f"New game?   {ma.GS.args.new_game}")
    if ma.GS.args.new_game:
        # ma.start_new_game()
        ma.clear_fleet()
    print(f"Moo Money Cheat?   {ma.GS.args.mo_money}")
    if ma.GS.args.mo_money:
        ma.mo_money(hunreds=21)
    print(f"Galaxy Cheat?   {ma.GS.args.show_galaxy}")
    if ma.GS.args.show_galaxy:
        ma.show_map_all()
    print(f"Check Systems?   {ma.GS.args.check_systems}")
    if ma.GS.args.check_systems:
        ma.review_systems()
    ma.GS.time_stale_game = ma.time()     # stale game 
    ma.GS.time_last_popup = ma.time()     # last popup
    ma.GS.time_last_base = ma.time()      # last base investment review
    ma.GS.time_start = ma.time()          # app start time
    idle_game_string_last = ''                        # the idle game string
    print('Starting "do the clicks loop".')
    try:
        loop_count = 0
        while True:
            ### update stats & kill popups
            loop_count += 1
            datime = ma.time()
            ms_pos = ma.pyautogui.position()
            rel_x = ms_pos.x - ma.GS.x
            rel_y = ms_pos.y - ma.GS.y
            ma.kill_popups()
            system_count = len(ma.GS.systems)
            idle_game_string = ma.get_idle_game_string()
            ### game bar test
            if idle_game_string == '---':
                """
                if '---' then the app window is not at a restful state.
                """
                ma.GS.time_stale_game = ma.time() 
                continue
            elif idle_game_string_last != idle_game_string:
                """
                something is moving on the screen.
                """
                idle_game_string_last = idle_game_string
                ma.GS.time_stale_game = ma.time() 
                continue
            ### timed actions - don't want to do stuff while pops are still running.
            last_stale_game_secs = int(datime - ma.GS.time_stale_game)
            last_system_mon_secs = int(datime - ma.GS.time_last_base)
            if last_system_mon_secs > 300 or system_count == 0:
                play_time = int(datime - ma.GS.time_start)
                print(f'You have been planing for {play_time} seconds and system count is {system_count}.')
                ma.gen_popup_report()
                ma.review_systems()
                ma.GS.time_last_base = ma.time()
                print(f'>>>>>>System Monitoring complete')
            elif last_stale_game_secs <= ma.GS.stale_next_secs:
                print(f'>>>>>>{last_stale_game_secs} stale secs, pointer @ ', (rel_x, rel_y))
            elif last_stale_game_secs > ma.GS.stale_next_secs:
                print('>>>>>>AUTO CLICK BABY!!!')
                ma.pyautogui.press(['n'])
                ma.move_pointer_to_home()


            ### quite if -qe
            if ma.GS.args.quick_exit:
                break
    except KeyboardInterrupt:
        print('\nDone.')


if __name__ == "__main__":
    main()