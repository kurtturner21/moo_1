
### external
import argparse
from time import sleep
import pyautogui as pag

### internal
import moo_auto as ma

"""
Other / Standard place for methods at the moment.
"""

# from moo_auto import *

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
        help='Run some features and exit.')
    parser.add_argument('-n', '--new_game',
        action='store_true', 
        default=False,
        help='Run a new game (random).')
    parser.add_argument('-cs', '--check_systems',
        action='store_true', 
        default=False,
        help='Run a new game (random).')
    parser.add_argument('-dn', '--do_not_click',
        action='store_false', 
        default=True,
        help='When looking for dos box, do we click in the game?')
    parser.add_argument('-d', '--debugging',
        action='store_true', 
        default=False,
        help='Show more output.')
    ma.GS.args = parser.parse_args()
    ma.GS.debugging = ma.GS.args.debugging
    ma.GS.dos_box_in_game = ma.GS.args.do_not_click


def clear_fleet():
    """
    Clear the board from the default unwanted ships.
    """
    def get_detail_fleet_view():
        trys = 0
        while True:
            sleep(.5)
            area_cords = (450, 50, 650, 100)
            im = ma.get_screen_shot()
            im_crop = im.crop(area_cords)
            im_crop_gy = ma.get_img_gray(im_crop)
            im_crop_hash = ma.get_image_hash(im_crop_gy)
            if im_crop_hash not in ['7cfc80a4848cff00','6c9f848484dfffdc','7cfc80a48cccff00']:
                pag.press(['esc','esc','f','v'])
                trys += 1
                sleep(1)
            else:
                break
            if trys > 10:
                print('screen res might not be right.')
                ma.sys.exit(20)
    unwanted_ships = {
        "0000fc78f87878f8": "SCOUT",
        "0000fe7efe7e7e7c": "FIGHTER",
        "00007f4e7f7f7f77": "DISTROYER",
        "00007c7c7c7c7c7c": "BOMBER"
        # "COLONY": "00007d7c7f2d7d7d",
    }
    area_cords = (200, 50, 400, 80)
    get_detail_fleet_view()
    while True:
        im = ma.get_screen_shot()
        im_crop = im.crop(area_cords)
        im_crop_gy = ma.get_img_gray(im_crop)
        im_crop_hash = ma.get_image_hash(im_crop_gy)
        if im_crop_hash in unwanted_ships:
            pag.moveTo(ma.GS.x + 530, ma.GS.y + 70, duration=.2)
            pag.click(ma.GS.x + 530, ma.GS.y + 70, clicks=1, button='left',interval=1)
            pag.press('y')
            print(f"Found unwanted ship: {unwanted_ships[str(im_crop_hash)]}   key {im_crop_hash}")
            pag.moveTo(ma.GS.x + 800, ma.GS.y + 500)
            # sleep(.5)
        else:
            break
    pag.press(['esc','esc'])

