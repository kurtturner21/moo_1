
### external
import argparse
import os
import sys
import pyautogui
import pytesseract
from PIL import Image 
import imagehash
from time import sleep
from time import time
import random

### internal
import moo_auto.popupdata


class GS:
    x = 0
    y = 0
    w = 1440
    h = 930
    debugging = False           # bool from cli
    args = None                 # args from cli app execution
    systems = set()             # set of system hashes from base review
    click_bases = [1155, 460]   # happy spot for base investment
    time_stale_game = 0         # epoch from last stale game detected 
    time_last_popup = 0         # epoch from last pop killed
    time_last_base = 0          # epoch from last base review
    time_start = 0              # epoch from the start of the game
    popup_msgs = {}
    im_app = None               # current app window image
    mouse_pos = None            # current app mouse location
    stale_next_secs = 10         # after bening stale click next
    dos_box_in_game = True     # do we do the click when search for the dos box?


#####
# Strat up stuff
#####
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
    GS.args = parser.parse_args()
    GS.debugging = GS.args.debugging
    GS.dos_box_in_game = GS.args.do_not_click


#####
# READING THE SCREEN
#####
def cord_dict_to_tuple(cord_dict):
    return (
        cord_dict['x'], 
        cord_dict['y'], 
        cord_dict['x'] + cord_dict['w'], 
        cord_dict['y'] + cord_dict['h']) 


def get_screen_shot(cord_dict=None):
    """
    Gets a screen shot of the entire game window.
    """
    if not cord_dict:
        needed_region = (GS.x, GS.y, GS.w, GS.h)
    else:
        needed_region = cord_dict_to_tuple(cord_dict)
    im = pyautogui.screenshot(region=needed_region)
    return im


def get_img_gray(img):
    """
    Return the standard gray for this app.
    """
    im_gray = img.convert('L')
    return im_gray


def get_image_hash(img):
    """
    Return a hash of a supplied image.
    """
    return str(imagehash.average_hash(img))


def get_image_text(img, text_color):
    """
    Update supplied image with to two pixels and then run OCR.
    """
    img_for_text = img.copy()
    width, height = img_for_text.size
    pixels = img_for_text.load()
    for y in range(0, height):
        for x in range(0, width):
            pix = pixels[x,y]
            if pix not in text_color:
                pixels[x,y] = (255, 255, 255) ### replace with white
            else:
                pixels[x,y] = (0, 0, 0)       ### replace with black
    ocr_text = pytesseract.image_to_string(img_for_text)
    for bad_char in ['\n', '\r']:
        ocr_text = ocr_text.replace(bad_char,  ' ')
    return ocr_text, img_for_text


def look_for_dos_box():
    """
    Look for the doxbox logo at the top left of the running application.
    """
    while True:
        fn_p =  os.path.join('search_imgs', 'dos_box.PNG')
        dos_box_pos = pyautogui.locateOnScreen(fn_p)
        if dos_box_pos:
            print('found dos box')
            if GS.dos_box_in_game:
                pyautogui.click(dos_box_pos.left+10, dos_box_pos.top+30,clicks=1, button='left',interval=1)
            else:
                pyautogui.click(dos_box_pos.left+30, dos_box_pos.top+10,clicks=1, button='left',interval=1)
            GS.x = dos_box_pos.left
            GS.y = dos_box_pos.top
            break


#####
# Kill the popups
#####
def move_pointer_to_home():
    sleep(.1)
    pyautogui.moveTo(GS.x + 50, GS.y + 50, duration=.1)
    sleep(.1)


def kill_popups():
    """
    Kill popups after each turn.
    """

    while True:
        found_ct = kill_popups_two()
        if not found_ct:
            break
        else:
            GS.time_last_popup = time()


def kill_popups_two():
    GS.im_app = get_screen_shot() # get screan shot of app
    screen_cords = popupdata.screen_cords(GS.click_bases)
    def do_action(so):
        """If the condiciton is med below, then do one of the following."""
        da_msg = s_cord['msg']
        if da_msg in GS.popup_msgs:
            GS.popup_msgs[da_msg] += 1
        else:
            GS.popup_msgs.update({da_msg:1})
        print(f"{da_msg}")
        if so['mv_to_click']:
            x = so['mv_to_click'][0]
            y = so['mv_to_click'][1]
            pyautogui.moveTo(GS.x + x, GS.y + y, duration=.2)
            pyautogui.click(GS.x + x, GS.y + y, clicks=1, button='left',interval=1)
            if so['mv_to_click_after_press']:
                sleep(so['sleap_after'])
                pyautogui.press(so['mv_to_click_after_press'], interval=0)
            move_pointer_to_home()
            sleep(so['sleap_after'])
        else:
            pyautogui.press(so['keys_press'], interval=0)
            move_pointer_to_home()
            sleep(so['sleap_after'])
    for s_cord in screen_cords:
        ### process cropped image
        needed_region = cord_dict_to_tuple(s_cord['cords_dict'])
        im = GS.im_app.crop(needed_region)
        im_gray = get_img_gray(im)
        im_hash = get_image_hash(im_gray)
        ### OCR process
        if s_cord['search_text']:
            im_text = get_image_text(im, s_cord['text_color'])[0]
        else:
            im_text = '---'
        ### test each case
        if im_hash in s_cord['hashes']:
            do_action(s_cord)
            return 1
        elif s_cord['search_text']:
            for s_text in s_cord['search_text']:
                if s_text in im_text:
                    do_action(s_cord)
                    print('\nsearch_text', s_cord['cords_dict'], im_hash, im_text)
                    return 1
        if GS.debugging:
            # im.show()
            print('\nelse loop', s_cord['msg'], s_cord['cords_dict'], im_hash, im_text)
    return 0


#####
# Monitor Systems
#####
def gen_popup_report():
    print('POPUP MESSAGE REPORT:')
    for m in GS.popup_msgs:
        print(f'{m:<20} {GS.popup_msgs[m]}')


def get_idle_game_string():
    """
    Return a string of the game bar img hash and the mouse pointer.
    """
    GS.mouse_pos = str(pyautogui.position())
    GS.im_app = get_screen_shot()
    game_bar_hash = 'c88cafe3b7008a3f'
    game_bar_cords = (50,830,1100,910)
    game_bar_img = GS.im_app.crop((game_bar_cords))
    game_bar_current_hash = str(imagehash.phash(game_bar_img))
    if game_bar_current_hash != game_bar_hash:
        return '---'
    else:
        return game_bar_current_hash + '-' + GS.mouse_pos


def review_systems():
    def return_base_count():
        base_ct_cords=(1340,290,1420,340)
        base_ct_colors=[(255,218,76)]
        GS.im_app = get_screen_shot()
        base_im = GS.im_app.crop((base_ct_cords))
        im_text, im_t_img = get_image_text(base_im, base_ct_colors)
        # im_t_img.show()
        return im_text
    def review_ship_builders():
        """If any amount of ship building, then push all RD to ships."""
        is_ship_building_hash='9887e638c1e4c6ee'
        is_ship_building_cords=(1050,390,1145,430)
        GS.im_app = get_screen_shot()
        im = GS.im_app.crop((is_ship_building_cords))
        im_hash = str(imagehash.phash(im))
        if im_hash == is_ship_building_hash:
            pyautogui.moveTo(GS.x + 1145, GS.y + 615, duration=.1)
            pyautogui.click(GS.x + 1145, GS.y + 615, clicks=1, button='left',interval=.1)
            return True
        else:
            return False
    def get_if_wasted():
        sys_waste_hash='f01e8a71625e792d'
        sys_clean_cords=(1280,530,1400,580)
        GS.im_app = get_screen_shot()
        im_n = GS.im_app.crop((sys_clean_cords))
        im_n_hash = str(imagehash.phash(im_n))
        if im_n_hash == sys_waste_hash:
            return True
        else:
            return False
    def get_clean_baby():
        sleep(.5)
        while get_if_wasted():
            print(f'clean up your crap')
            pyautogui.moveTo(GS.x + 1270, GS.y + 560, duration=.1)
            pyautogui.click(GS.x + 1270, GS.y + 560, clicks=1, button='left',interval=.1)
    def set_base_investment():
        """Click the sweat spot for building bases."""
        x = GS.click_bases[0]
        y = GS.click_bases[1]
        pyautogui.moveTo(GS.x + x, GS.y + y, duration=.1)
        pyautogui.click(GS.x + x, GS.y + y, clicks=1, button='left',interval=.1)
        sleep(.1)
    this_run_systems = set()  ### preventing endless runs.
    sys_name_cords=(1050,60,1400,120)
    sys_name_colors=[(232,205,135),(227,183,81),(215,162,31),(244,229,194)]
    sys_ct = 0
    while True:
        ### next
        pyautogui.press('f2', interval=0)
        GS.im_app = get_screen_shot()
        ### name
        im_n = GS.im_app.crop((sys_name_cords))
        im_n_hash = imagehash.phash(im_n)
        im_text = get_image_text(im_n, sys_name_colors)[0]
        if im_n_hash in this_run_systems:
            break
        elif im_n_hash not in GS.systems:
            GS.systems.add(im_n_hash)
            this_run_systems.add(im_n_hash)
            is_new = True
        else:
            is_new = False
        ### system work needed.
        sys_ct += 1
        set_base_investment()
        get_clean_baby()
        a_builder = review_ship_builders()
        base_ct = return_base_count()
        # print(f'{sys_ct:<4} {is_new} P:{im_n_hash}  N:{im_text:<15} B:{a_builder} B:{base_ct}')
        print(f'{sys_ct:<4} {is_new} N:{im_text:<10} B:{a_builder} B:{base_ct}')
    move_pointer_to_home()
    sleep(.2)
    print(f'we have {len(GS.systems)} systems.')


#####
# STD PROCESSES
#####
def start_new_game():
    """
    Assumes we are on the main menu.
    """
    pyautogui.press(['esc','esc'])
    pyautogui.press('n')
    sleep(1)
    pyautogui.click(GS.x + 850, GS.y + 730, clicks=1, button='left',interval=1)
    sleep(2)
    ### race
    num1 = random.randint(5, 30)
    for x in range(num1):
        pyautogui.press('up')
    sleep(1)
    pyautogui.press('return')
    sleep(1)
    ### color
    num1 = random.randint(3, 15)
    for x in range(num1):
        pyautogui.press('up')
    pyautogui.press('return')
    sleep(1)
    pyautogui.press('return')
    sleep(1)
    pyautogui.press('return')
    sleep(10)


def clear_fleet():
    """
    Clear the board from the default unwanted ships.
    """
    def get_detail_fleet_view():
        while True:
            area_cords = (450, 50, 650, 100)
            im = get_screen_shot()
            im_crop = im.crop(area_cords)
            im_crop_gy = get_img_gray(im_crop)
            im_crop_hash = get_image_hash(im_crop_gy)
            if im_crop_hash != '7cfc80a4848cff00':
                pyautogui.press(['esc','esc','f','v'])
                sleep(1)
            else:
                break
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
        im = get_screen_shot()
        im_crop = im.crop(area_cords)
        im_crop_gy = get_img_gray(im_crop)
        im_crop_hash = get_image_hash(im_crop_gy)
        if im_crop_hash in unwanted_ships:
            pyautogui.moveTo(GS.x + 530, GS.y + 70, duration=.2)
            pyautogui.click(GS.x + 530, GS.y + 70, clicks=1, button='left',interval=1)
            pyautogui.press('y')
            print(f"Found unwanted ship: {unwanted_ships[str(im_crop_hash)]}   key {im_crop_hash}")
            pyautogui.moveTo(GS.x + 800, GS.y + 500)
            # sleep(.5)
        else:
            break
    pyautogui.press(['esc','esc'])


##############
# CHEATS
##############
def show_map_all():
    pyautogui.keyDown('altleft')
    pyautogui.press(['g','a','l','a','x','y'])
    pyautogui.keyUp('altleft')


def mo_money(hunreds=1):
    area_cords = (50, 750, 300, 50) 
    im = get_screen_shot()
    im_crop = im.crop(area_cords)
    im_crop_hash = imagehash.average_hash(im_crop)
    if "ebdee1d5f1c0ecec" != str(im_crop_hash):
        pyautogui.press('esc',interval=0) 
    pyautogui.press('p', interval=0)
    for x in range(hunreds):
        pyautogui.keyDown('alt')
        pyautogui.typewrite('moola', interval=0)
        pyautogui.keyUp('alt')
    pyautogui.typewrite('t', interval=0)
    pyautogui.press('up', interval=0)
    pyautogui.press('enter', interval=0)
    pyautogui.press('down', interval=0)
    pyautogui.press('right', interval=0)
    pyautogui.press('right', interval=0)
    ### each click is 2%
    for x in range(50):
        pyautogui.click(interval=0)
    pyautogui.press('space', interval=0)
    pyautogui.press('esc', interval=0)
