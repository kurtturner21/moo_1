
"""
Methods for the two cheats that are currently known for this app.
"""

import pyautogui as pag

### internal
from .sreading import *

def show_map_all():
    pag.keyDown('altleft')
    pag.press(['g','a','l','a','x','y'])
    pag.keyUp('altleft')


def mo_money(hunreds=1):
    area_cords = (50, 750, 300, 50) 
    im = get_screen_shot()
    im_crop = im.crop(area_cords)
    im_crop_hash = imagehash.average_hash(im_crop)
    if "ebdee1d5f1c0ecec" != str(im_crop_hash):
        pag.press('esc',interval=0) 
    pag.press('p', interval=0)
    for x in range(hunreds):
        pag.keyDown('alt')
        pag.typewrite('moola', interval=0)
        pag.keyUp('alt')
    pag.typewrite('t', interval=0)
    pag.press('up', interval=0)
    pag.press('enter', interval=0)
    pag.press('down', interval=0)
    pag.press('right', interval=0)
    pag.press('right', interval=0)
    ### each click is 2%
    for x in range(50):
        pag.click(interval=0)
    pag.press('space', interval=0)
    pag.press('esc', interval=0)

