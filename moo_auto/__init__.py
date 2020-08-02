
import os
import pyautogui
from PIL import Image 
import imagehash
from time import sleep

class GS:
    x = 0
    y = 0
    w = 1440
    h = 930

### app config    
app_cor = {}


def look_for_dos_box():
    """
    Look for the doxbox logo at the top left of the running application.
    """
    while True:
        fn_p =  os.path.join('search_imgs', 'dos_box.PNG')
        dos_box_pos = pyautogui.locateOnScreen(fn_p)
        if dos_box_pos:
            print('found dos box')
            pyautogui.click(dos_box_pos.left+10, dos_box_pos.top+30,clicks=1, button='left',interval=1)
            GS.x = dos_box_pos.left
            GS.y = dos_box_pos.top
            app_cor = {'x': dos_box_pos.left + 10, 'y': dos_box_pos.top + 30}
            break


def show_map_all():
    pyautogui.keyDown('altleft')
    pyautogui.press(['g','a','l','a','x','y'])
    pyautogui.keyUp('altleft')


def mo_money(hunreds=1):
    fn_p =  os.path.join('search_imgs', 'planets_col_1.PNG')
    if not pyautogui.locateOnScreen(fn_p):
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


def kill_popups():
    """
    Kill popups after each turn.
    """
    build_a_new_colony_x, build_a_new_colony_y = 1040, 290
    build_a_new_colony_hash = ['060f2feffc103030','203c3c2009ff7e02','a03c3c0049ff7e02',
        'a03c3c240fdf7e00','793079ffff0707bf','203c3c2009fffe02']
    build_a_new_colony = (
        build_a_new_colony_x, 
        build_a_new_colony_y, 
        build_a_new_colony_x + 320, 
        build_a_new_colony_y + 90) 
    im = pyautogui.screenshot(region=(GS.x, GS.y, GS.w, GS.h))
    im_gs = im.convert('LA')
    ### new colony
    im_crop = im_gs.crop(build_a_new_colony)
    im_crop_hash = imagehash.average_hash(im_crop)
    print(im_crop_hash)
    for h in build_a_new_colony_hash:
        if h == str(im_crop_hash):
            print(f'Start a new colony?  {im_crop_hash}')
            pyautogui.press('y', interval=0)
            sleep(2)
            pyautogui.press('esc', interval=0)
            pyautogui.press('esc', interval=0)
            break

