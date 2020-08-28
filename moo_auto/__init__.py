
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

class GS:
    x = 0
    y = 0
    w = 1440
    h = 930
    race_screen = False
    pop_up_sleep_time = 0 #.3
    debugging = False
    args = None
    systems = set()
    new_col = False
    click_bases = [1155, 460]
    time_stale_game = 0
    time_last_popup = 0
    time_last_stat = 0
    time_last_base = 0
    time_start = 0
    popup_msgs = {}
    im_app = None               # standard app windows image

pyautogui.FAILSAFE = True
screen_cords = [
    { 
        "cords_dict": {"x": 270, "y": 240, "w": 500, "h": 50},
        "hashes": ["0000507e7e7e7e00"],
        "msg": "Fleet Production",
        "text_color": [],
        "search_text": [],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": .1
    },
    { 
        "cords_dict": {"x": 220, "y": 270, "w": 600, "h": 350},
        "hashes": [],
        "msg": "Planetary Shield",
        "text_color": [(195,195,195)],
        "search_text": ["lanetary Shield"],
        "keys_press": [],
        "mv_to_click": GS.click_bases,
        "mv_to_click_after_press": ["esc"],
        "sleap_after": .5
    },
    {
        "cords_dict": {"x": 850, "y": 400, "w": 300, "h": 100},
        "hashes": ["ffff77ee88ee0000"],
        "msg": "Select Ratio",
        "text_color": [],
        "search_text": [],
        "keys_press": [],
        "mv_to_click": [920, 460],
        "mv_to_click_after_press": [],
        "sleap_after": .4
    },
    { 
        "cords_dict": {"x": 1020, "y": 300, "w": 380, "h": 400},
        "hashes": ["00503e7e7e7e0000"],
        "msg": "Space Combat",
        "text_color": [(239,239,239)],
        "search_text": ["Space Combat"],
        "keys_press": ["c"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": .1
    },
    { 
        "cords_dict": {"x": 220, "y": 270, "w": 600, "h": 350},
        "hashes": [],
        "msg": "Middle notice",
        "text_color": [(195,195,195)],
        "search_text": [
            "be chonged at this time.",
            "transports attempting To land on ",
            "Your transports attemptina to land on",
            "transports attempting to land on"
            ],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": .1
    },
    { 
        "cords_dict": {"x": 155, "y": 640, "w": 1100, "h": 270},
        "hashes": [],
        "msg": "Deplimate Talks",
        "text_color": [(0,0,0), (132,12,0)],
        "search_text": [
            "bring you an offer of peace",
            "Both our races have suffered greatly",
            "We can mo longer sustain this horrible war"
            ],
        "keys_press": ["up","return"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": .1
    },
    { 
        "cords_dict": {"x": 155, "y": 640, "w": 1100, "h": 270},
        "hashes": [],
        "msg": "Deplimate Talks - two",
        "text_color": [(0,0,0), (132,12,0)],
        "search_text": [
            "Your attacks against the insidious",
            "We shall make an example",
            "bears greetings from the most",
            "bear greetings from the most wise",
            "It would seem that our empires",
            "Hail glorious Emperor",
            "Greetings from",
            "Our patience is exhausted. Continue to expand and it will be war.",
            "You have spread like a plague throughout the galaxy. Cease your reckless expansion or we will be forced to eliminate your threat once and for all.",
            "star system an unprovoked act of war.",
            "Let us work for a mutually beneficial relationship.",
            "empire is tired of playing diplomatic games.",
            "We have known all along that the",
            "empire wishes mo contact with the filthy",
            "and hopes that you will prosper under our rule"
            ],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": .1
    },
    {
        "cords_dict": {"x": 850, "y": 400, "w": 300, "h": 100},
        "hashes": ["ffff77ee88ee0000"],
        "msg": "Select Ratio",
        "text_color": [],
        "search_text": [],
        "keys_press": [],
        "mv_to_click": [920, 460],
        "mv_to_click_after_press": [],
        "sleap_after": .4
    },
    {
        "cords_dict": {"x": 680, "y": 180, "w": 600, "h": 300},
        "hashes": ['840040400080ffff'],
        "msg": "Reduce Usage - YES.",
        "text_color": [],
        "search_text": [],
        "keys_press": [],
        "mv_to_click": [1140, 466],
        "mv_to_click_after_press": [],
        "sleap_after": .4
    },
    {
        "cords_dict": {"x": 1250, "y": 250, "w": 150, "h": 200},
        "hashes": ["090d0d0d091df9f1","0101010d0d0d8dd9"],
        "msg": "Inital tEcH.",
        "text_color": [],
        "search_text": [],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": .4
    },
    {
        "cords_dict": {"x": 700, "y": 180, "w": 700, "h": 60},
        "hashes": [],
        "msg": "Select next tech.",
        "text_color": [(65,183,33)],
        "search_text": ["Technology"],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": .4
    },
    {
        "cords_dict": {"x": 1030, "y": 280, "w": 360, "h": 100},
        "hashes": [],
        "msg": "Orbital Bombardment",
        "text_color": [(192,151,112), (239,239,239)],
        "search_text": ["Bombardment"],
        "keys_press": ["c"],
        "mv_to_click": [],
        "sleap_after": .1
    },
    {
        "cords_dict": {"x": 250, "y": 600, "w": 500, "h": 50},
        "hashes": ["fff8f0080809099e"],
        "msg": "News",
        "text_color": [],
        "search_text": [],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": .1
    },
    {
        "cords_dict": {"x": 100, "y": 250, "w": 700, "h": 50},
        "hashes": ["41c3c3c0c3c3c3c3"],
        "msg": "Voting - esc",
        "text_color": [],
        "search_text": [],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": .1
    },
    {
        "cords_dict": {"x": 1040, "y": 290, "w": 320, "h": 90},
        "hashes": ['060f2feffc103030','203c3c2009ff7e02','a03c3c0049ff7e02',
            'a03c3c240fdf7e00','203c3c2009fffe02','f8fc3c01dfff1a00','203c3c0009df7e02',
            '283c3c2009ff7e02', '203c3c3019ff7e02','203c3c3001ff7e12','283c3c2009df7e02',
            '203c3c2009df7e02', '203c3c3009ff7e02'],
        "msg": "Start a new colony?",
        "text_color": [],
        "search_text": [],
        "keys_press": ["Y", "", "", "esc", "esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": .1
    },
    { 
        "cords_dict": {"x": 650, "y": 100, "w": 150, "h": 150},
        "hashes": ["ffcf0120ff8080ff"],
        "msg": "Name that SHIP?",
        "text_color": [],
        "search_text": [],
        "keys_press": ["esc"],
        "mv_to_click": [],
        "mv_to_click_after_press": [],
        "sleap_after": .1
    },
]


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
    parser.add_argument('-d', '--debugging',
        action='store_true', 
        default=False,
        help='Show more output.')
    GS.args = parser.parse_args()
    GS.debugging = GS.args.debugging


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


def look_for_dos_box(do_click=True):
    """
    Look for the doxbox logo at the top left of the running application.
    """
    while True:
        fn_p =  os.path.join('search_imgs', 'dos_box.PNG')
        dos_box_pos = pyautogui.locateOnScreen(fn_p)
        if dos_box_pos:
            print('found dos box')
            if do_click:
                pyautogui.click(dos_box_pos.left+10, dos_box_pos.top+30,clicks=1, button='left',interval=1)
            GS.x = dos_box_pos.left
            GS.y = dos_box_pos.top
            break


#####
# Kill the popups
#####
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
    sleep(1)


def kill_popups_two():
    GS.im_app = get_screen_shot() # get screan shot of app
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
            sleep(so['sleap_after'])
        else:
            pyautogui.press(so['keys_press'], interval=0)
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


def is_game_visible():
    """
    This will tell you if the game bar is visible. 
    """
    game_bar_hash = 'd487abe8bb04a42f'
    game_bar_cords = (50,830,1400,910)
    game_bar_img = GS.im_app.crop((game_bar_cords))
    game_area_current_hash = str(imagehash.phash(game_bar_img))
    if game_area_current_hash == game_bar_hash:
        return True
    else:
        return False


def review_systems():
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
    first_hash = None
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
        if not first_hash:
            first_hash = im_n_hash
        elif im_n_hash == first_hash:
            break
        if im_n_hash not in GS.systems:
            GS.systems.add(im_n_hash)
            is_new = True
        else:
            is_new = False
        ### system work needed.
        sys_ct += 1
        set_base_investment()
        get_clean_baby()
        a_builder = review_ship_builders()
        # print(f'{sys_ct:<4} {is_new} P:{im_n_hash}  N:{im_text:<15} B:{a_builder}')
        print(f'{sys_ct:<4} {is_new} N:{im_text:<10} B:{a_builder}')
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
