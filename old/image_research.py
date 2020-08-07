import pyautogui
import pytesseract
from PIL import Image 
from time import sleep
import os
import math
pyautogui.FAILSAFE = True

# pend_star = tuple([0,0,0,0,0,0,0,0,0])           ### three black pixels
# pend_star = tuple(tuple([105]*3*9))           ### gray pixels
DARK_STAR = tuple([89]*3*2) + tuple([105]*3*13)           ### Dark start
STAR_PATTERNS = [
    {'name': 'DARK_STAR', 'pattern': DARK_STAR}
]

def main():
    global map_data
    map_data = {}
    def new_start_test(x2, y2):
        MIN_DIST_NEEDED = 50
        for ext_star in map_data:
            x1 = map_data[ext_star]['x']
            y1 = map_data[ext_star]['y']
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if distance < MIN_DIST_NEEDED:
                return False
        return True
    ### read map
    fn_p_in =  os.path.join('tmp', 'map.PNG')
    fn_p_out =  os.path.join('tmp', 'map_out.PNG')
    im = Image.open(fn_p_in) 
    im_new = im.load()
    width, height = im.size
    print(im.size)
    ### star search
    for pend_star in STAR_PATTERNS:
        pend_star_pattern = pend_star['pattern']
        pend_star_name = pend_star['name']
        pend_star_pixel_size = len(pend_star_pattern)/3
        pix_x_s = int(pend_star_pixel_size/2)
        pix_x_e = int(pend_star_pixel_size) - pix_x_s
        print(f'Start searching for {pend_star_name}')
        print(f'pend_star len = {len(pend_star_pattern)}  pend_star_pixel_size = {pend_star_pixel_size}')
        print(f'pix_x_s={pix_x_s}  pix_x_e={pix_x_e} ')
        pix_count = 0
        for y in range(height):
            for x in range(10, width-10):
                pix_count += 1
                pix_set = []
                pix_key = f'{x}_{y}'
                for pos in range(-pix_x_s, pix_x_e):
                    pix_set += list(im.getpixel((x + pos,y))[:3])
                pix_set = tuple(pix_set)
                if pend_star_pattern == pix_set:
                    if new_start_test(x, y):
                        map_data.update({pix_key: {
                            'x':x, 
                            'y':y,
                            'type': pend_star_name
                            }})
                        print(f'NEW STAR AT x={x}, y={y}')
                        im_new[x, y] = (255, 255, 255)
    print(len(map_data))
    im.save(fn_p_out) 



if __name__ == "__main__":
    main()