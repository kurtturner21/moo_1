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
    ma.GS.time_stale_game = ma.time()     # stale game 
    ma.GS.time_last_popup = ma.time()     # last popup
    ma.GS.time_last_stat = ma.time()      # last update
    ma.GS.time_last_base = ma.time()      # last base investment review
    ma.GS.time_start = ma.time()          # app start time
    print('Starting "do the clicks loop".')
    try:
        loop_count = 0
        ma.GS.new_col = True
        while True:
            loop_count += 1
            datime = ma.time()
            ms_pos = ma.pyautogui.position()
            rel_x = ms_pos.x - ma.GS.x
            rel_y = ms_pos.y - ma.GS.y
            ma.kill_popups()
            ### game bar test
            if not ma.is_game_visible():
                ma.GS.time_stale_game = ma.time() 
                continue
            ### timed actions - don't want to do stuff while pops are still running.
            last_popup_secs = int(datime - ma.GS.time_start)
            last_stale_game_secs = int(datime - ma.GS.time_stale_game)
            if (datime - ma.GS.time_last_stat) > 120 and last_popup_secs > 10:
                play_time = int(datime - ma.GS.time_start)
                print(f'You have been planing for {play_time} seconds.')
                ma.GS.time_last_stat = ma.time()
                ma.gen_popup_report()
            if (datime - ma.GS.time_last_base) > 300 and last_popup_secs > 10:
                ma.GS.time_last_base = ma.time()
                ma.review_systems()
            if last_stale_game_secs > 10 and  last_stale_game_secs <= 20:
                print(f'>>>>>>Stale game warning  {last_stale_game_secs} seconds.')
                print(f'>>>>>>{loop_count} clicking n', (rel_x, rel_y))
            # elif last_stale_game_secs > 20:
            #     print('>>>>>>AUTO CLICK BABY!!!')
            #     ma.pyautogui.press(['n'])          

            ### quite if -qe
            if ma.GS.args.quick_exit:
                break
    except KeyboardInterrupt:
        print('\nDone.')


if __name__ == "__main__":
    main()