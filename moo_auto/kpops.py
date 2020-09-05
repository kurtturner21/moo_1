
"""
For killing popups in the game to make game play faster.
"""

from time import sleep
import pyautogui as pag
from time import time

### internal
import moo_auto as ma

def move_pointer_to_home():
    sleep(.1)
    pag.moveTo(ma.GS.x + 50, ma.GS.y + 50, duration=.1)
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
            ma.GS.time_last_popup = time()


def kill_popups_two():
    ma.GS.im_app = ma.get_screen_shot() # get screan shot of app
    screen_cords = ma.screen_cords(ma.GS.click_bases)
    def do_action(so):
        """If the condiciton is med below, then do one of the following."""
        da_msg = s_cord['msg']
        if da_msg in ma.GS.popup_msgs:
            ma.GS.popup_msgs[da_msg] += 1
        else:
            ma.GS.popup_msgs.update({da_msg:1})
        print(f"{da_msg}")
        if so['mv_to_click']:
            x = so['mv_to_click'][0]
            y = so['mv_to_click'][1]
            pag.moveTo(ma.GS.x + x, ma.GS.y + y, duration=.2)
            pag.click(ma.GS.x + x, ma.GS.y + y, clicks=1, button='left',interval=1)
            if so['mv_to_click_after_press']:
                sleep(so['sleap_after'])
                pag.press(so['mv_to_click_after_press'], interval=0)
            sleep(so['sleap_after'])
        else:
            pag.press(so['keys_press'], interval=0)
            sleep(so['sleap_after'])
    for s_cord in screen_cords:
        ### process cropped image
        needed_region = ma.cord_dict_to_tuple(s_cord['cords_dict'])
        im = ma.GS.im_app.crop(needed_region)
        im_gray = ma.get_img_gray(im)
        im_hash = ma.get_image_hash(im_gray)
        ### OCR process
        if s_cord['search_text']:
            im_text = ma.get_image_text(im, s_cord['text_color'])[0]
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
        if ma.GS.debugging:
            # im.show()
            print('\nelse loop', s_cord['msg'], s_cord['cords_dict'], im_hash, im_text)
    return 0

