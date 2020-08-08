import pyautogui
import argparse
from time import sleep
from time import time
import json
import os
pyautogui.FAILSAFE = True
import moo_auto as ma


"""
Purpose: I really like playing MOO on a "Huge" map, but hate clicking the buttons.  This app will kill all the popups for me.
Goals:
 - Kill technology popups for me. 
"""


### TODO
# 1. Speed up excape screens

def app_config(): 
    parser = argparse.ArgumentParser(description='MOO button clicker.')
    parser.add_argument('-mm', '--mo_money',
        action='store_true', 
        default=False,
        help='Run the mo money cheat.')
    parser.add_argument('-sg', '--show_galaxy',
        action='store_true', 
        default=False,
        help='Run the galaxy map cheat.')
    parser.add_argument('-qe', '--quick_exit',
        action='store_true', 
        default=False,
        help='Run some feachers and exit.')
    parser.add_argument('-n', '--new_game',
        action='store_true', 
        default=False,
        help='Run a new game (random).')
    args = parser.parse_args()
    return args


def run_game():
    global app_vars
    try:
        while True:
            # ms_pos = pyautogui.position()
            # rel_x = ms_pos.x - ma.GS.x
            # rel_y = ms_pos.y - ma.GS.y
            # print(f'{loop_count} clicking n', (rel_x, rel_y))
            sleep(.5)
            ma.kill_popups()
            if app_vars.quick_exit:
                break
    except KeyboardInterrupt:
        print('\nDone.')


def main():
    global app_vars
    app_vars = app_config()
    ma.look_for_dos_box()
    print(f"Galaxy cheat?   {app_vars.new_game}")
    if app_vars.new_game:
        ma.start_new_game()
        ma.clear_fleet()
    print(f"Moo Money Cheat?   {app_vars.mo_money}")
    if app_vars.mo_money:
        ma.mo_money(hunreds=21)
    print(f"Galaxy Cheat?   {app_vars.show_galaxy}")
    if app_vars.show_galaxy:
        ma.show_map_all()
    run_game()


if __name__ == "__main__":
    main()