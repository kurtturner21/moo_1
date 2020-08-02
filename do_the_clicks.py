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
    parser.add_argument(
        '--momoney',
        action='store_true', 
        default=False,
        help='Run the mo money cheet.')
    parser.add_argument(
        '--sgalax',
        action='store_true', 
        default=False,
        help='Run the galaxy map cheet.')
    args = parser.parse_args()
    return args


def run_game():
    global app_vars
    loop_count = 0
    try:
        while True:
            loop_count += 1
            ms_pos = pyautogui.position()
            print(f'{loop_count} clicking n', ms_pos)
            sleep(1)
            ma.kill_popups()
            break
    except KeyboardInterrupt:
        print('\nDone.')


def main():
    global app_vars
    app_vars = app_config()
    ma.look_for_dos_box()
    print(f"Moo Money Cheet?   {app_vars.momoney}")
    if app_vars.momoney:
        ma.mo_money(hunreds=21)
    print(f"Galaxy cheet?   {app_vars.sgalax}")
    if app_vars.sgalax:
        ma.show_map_all()
    run_game()


if __name__ == "__main__":
    main()