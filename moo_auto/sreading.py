
"""
For reading the screen.
"""

import moo_auto as ma
import pyautogui as pag
import imagehash
import pytesseract
import os

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
        needed_region = (ma.GS.x, ma.GS.y, ma.GS.w, ma.GS.h)
    else:
        needed_region = cord_dict_to_tuple(cord_dict)
    im = pag.screenshot(region=needed_region)
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
        fn_p =  os.path.join('search_imGS', 'dos_box.PNG')
        dos_box_pos = pag.locateOnScreen(fn_p)
        if dos_box_pos:
            print('found dos box')
            if ma.GS.dos_box_in_game:
                pag.click(dos_box_pos.left+10, dos_box_pos.top+30,clicks=1, button='left',interval=1)
            else:
                pag.click(dos_box_pos.left+30, dos_box_pos.top+10,clicks=1, button='left',interval=1)
            ma.GS.x = dos_box_pos.left
            ma.GS.y = dos_box_pos.top
            break

