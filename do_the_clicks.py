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
    print('Starting "do the clicks loop".')
    try:
        loop_count = 0
        ma.GS.new_col = True
        while True:
            loop_count += 1
            ms_pos = ma.pyautogui.position()
            # rel_x = ms_pos.x - ma.GS.x
            # rel_y = ms_pos.y - ma.GS.y
            # if ma.GS.args.debugging:
            #     print(f'{loop_count} clicking n', (rel_x, rel_y))
            ma.kill_popups()
            if ma.GS.args.quick_exit:
                break
    except KeyboardInterrupt:
        print('\nDone.')


if __name__ == "__main__":
    main()