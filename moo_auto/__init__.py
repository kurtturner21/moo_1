
import os
import sys
import pyautogui
from PIL import Image 
import imagehash
from time import sleep
import random

class GS:
    x = 0
    y = 0
    w = 1440
    h = 930
    race_screen = False

### app config    
app_cor = {}


##############
# READING THE SCREEN
##############
def get_default_screen_shot_gs():
    im = pyautogui.screenshot(region=(GS.x, GS.y, GS.w, GS.h))
    im_gs = im.convert('LA')
    return im_gs


def get_default_crop_gs(area_cords, im_gs=None):
    if not im_gs:
        im_gs = get_default_screen_shot_gs()
    im_crop = im_gs.crop(area_cords)
    im_crop_hash = imagehash.average_hash(im_crop)
    return str(im_crop_hash)


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
            app_cor = {'x': dos_box_pos.left + 10, 'y': dos_box_pos.top + 30}
            break


def kill_popups():
    """
    Kill popups after each turn.
    """
    found_ct = 1
    while found_ct > 0:
        found_ct = 0
        found_ct += kill_popups_new_colony()
        found_ct += kill_popups_type_1()
        

def kill_popups_new_colony():
    match_hash_list = ['060f2feffc103030','203c3c2009ff7e02','a03c3c0049ff7e02',
        'a03c3c240fdf7e00','203c3c2009fffe02','f8fc3c01dfff1a00','203c3c0009df7e02',
        '283c3c2009ff7e02', '203c3c3019ff7e02','203c3c3001ff7e12','283c3c2009df7e02']
    x, y, w, h = 1040, 290, 320, 90
    area_cords = (x, y, x + w, y + h) 
    im_crop_hash = get_default_crop_gs(area_cords)
    for h in match_hash_list:
        if h == str(im_crop_hash):
            print(f'Start a new colony?  {im_crop_hash}')
            pyautogui.press('y', interval=0)
            sleep(2)
            pyautogui.press('esc', interval=0)
            pyautogui.press('esc', interval=0)
            return 1
    return 0


def kill_popups_type_1():
    match_hash_list = [
            [1040, 650, 320, 90, 'c380c08280d72783', 'Missle Base.', 'esc'],
            [530, 100, 300, 200, 'ff81817f00ff83a3', 'Identify Ship Class.', 'esc'],
            [280, 520, 500, 100, '3f3f1a0000ffffd0', 'News Cast.', 'esc'],
            [280, 240, 500, 50, '0000507e7e7e7e00', 'Fleet Production.', 'esc'],
            [280, 520, 500, 100, 'ff00ff0000ff011f', 'Middle Notice.', 'esc'],
            [100, 600, 320, 90, 'e0e0e0e0e0e0e0e0', 'Voting.', 'esc'],
            [700, 400, 400, 90, 'ffff6cdbd280db00', 'Yes to Ratio!', '2'],
            [1300, 150, 100, 400, '0131313133c30393', 'New Tech?', 'esc'],
            [1300, 150, 100, 400, '0131313133c30313', 'New Tech?', 'esc'],
            [800, 800, 500, 100, '38383c3cd8d8d8f8', 'New Tech?', 'esc'],
            [1300, 150, 100, 400, '01fffc0000000000', 'Race Talks', 'esc']
        ]
    for h in match_hash_list:
        x, y, w, h, m_hash, msg, key_act = h
        area_cords = (x, y, x + w, y + h) 
        im_crop_hash = get_default_crop_gs(area_cords)
        if m_hash == im_crop_hash:
            print(f'{msg} - {im_crop_hash}')
            pyautogui.press(key_act, interval=0)
            sleep(1)
            if m_hash == '01fffc0000000000':
                GS.race_screen = True
                print(f'Overall security.')
                pyautogui.press('esc', interval=0)
                pyautogui.press('r', interval=0)
                pyautogui.click(GS.x + 1130, GS.y + 665,
                    clicks=1, button='left',interval=1)
                pyautogui.press('o', interval=0)
            return 1
    return 0


def show_region(x=40, y=40, w=300, h=100):
    area_cords = (x, y, x + w, y + h) 
    im_gs = get_default_screen_shot_gs()
    im_crop = im_gs.crop(area_cords)
    im_crop_hash = get_default_crop_gs(area_cords, im_gs=im_gs)
    print(f'hash: {im_crop_hash}')
    im_crop.show()


##############
# STD PROCESSES
##############
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
            im_crop_hash = get_default_crop_gs(area_cords)
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
        im_crop_hash = get_default_crop_gs(area_cords)
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
    im_gs = get_default_screen_shot_gs()
    im_crop = im_gs.crop(area_cords)
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
