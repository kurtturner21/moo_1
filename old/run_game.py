import pyautogui
import pytesseract
from PIL import Image 
from time import sleep
import json
import os
import math
from time import time
import numpy as np
# pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True
# GS = {'x': 1440, 'y': 930}

class GS:
    x = 0
    y = 0
    w = 1440
    h = 930

# DARK_STAR = tuple([89]*3*2) + tuple([105]*3*12)           ### Dark star
DARK_STAR2 = tuple([89]*3*2) + tuple([105]*3*4) 
HOME_STAR = tuple([45,32,23]*4) + tuple([115,75,29]*5) + tuple([45,32,23]*4) + tuple([0]*3*2)
HOME_STAR = tuple([115,75,29]*5) + tuple([45,32,23]*4) + tuple([0]*3*2)
STAR_PATTERNS = [
    # {'name': 'DARK_STAR', 'pattern': DARK_STAR},
    {'name': 'DARK_STAR2', 'pattern': DARK_STAR2},
    {'name': 'HOME_STAR', 'pattern': HOME_STAR}
]

### TODO
# 1. Manage new worlds
# 2. Speed up excape screens
# 3. Send scouts to other unkwown

def load_escape_imgs():
    global g_imgs
    g_imgs = {}
    file_names = [
        ('tech_reduce', 'yes_click'),
        ('tech_inds_increase', '2_click'),
        ('planet_rates', 'click'),
        ('fleet_prod', 'click'),
        ('tech2', 'esc'),
        ('news', 'esc'),
        ('vote', 'esc'),
        ('vote2', 'esc'),
        ('trade', 'esc'),
        ('manual_check', 'esc')
        ]
    ### setup custom types
    for fn in file_names:
        fn_p =  os.path.join('search_imgs', f'{fn[0]}.PNG')
        im = Image.open(fn_p)
        g_imgs.update({
            fn[0]:{
                'im': im,
                'path': fn_p,
                'type': fn[1]
            }
        })
    ### load everything else based on name.
    for walk_data in os.walk("search_imgs"):
        for filename in walk_data[2]:
            fn = os.path.splitext(filename)[0]
            if fn not in g_imgs:
                fn_p =  os.path.join('search_imgs', filename)
                im = Image.open(fn_p)
                g_imgs.update({
                    fn:{
                        'im': im,
                        'path': fn_p,
                        'type': None
                    }
                })


def look_for_basics():
    global g_imgs, app_cor
    while True:
        dos_box_pos = pyautogui.locateOnScreen(g_imgs['dos_box']['im'])
        if dos_box_pos:
            print('found dos box')
            pyautogui.click(dos_box_pos.left+10, dos_box_pos.top+30,clicks=1, button='left',interval=1)
            GS.x = dos_box_pos.left
            GS.y = dos_box_pos.top
            app_cor = {'x': dos_box_pos.left + 10, 'y': dos_box_pos.top + 30}
            break  

def build_angle_array(my_v_item, items):
    """
    used to find degrees between items
    """
    x2, y2 = my_v_item.split('_')
    my_agls = []
    for v_item in items:
        x1 = items[v_item]['x']
        y1 = items[v_item]['y']
        radians = math.atan2(y1-int(y2), x1-int(x2))
        degrees = math.ceil(math.degrees(radians))
        if not degrees:
            continue
        if degrees not in my_agls:
            my_agls.append(degrees)
    return my_agls

def screen_for_esc_images():
    global g_imgs
    esc_imgs = [
        'planet_rates',
        'fleet_prod',
        'tech_reduce',
        'tech_inds_increase',
        'tech2',
        'news',
        'vote',
        'vote2',
        'manual_check',
        'trade']
    pyautogui.click(100, 100,clicks=1, button='left',interval=0)
    while True:
        pyautogui.click(100, 700,clicks=1, button='left',interval=0)
        found_img = 0
        for im in esc_imgs:
            im_pos = pyautogui.locateOnScreen(g_imgs[im]['im'])
            if im_pos:
                found_img += 1
                if g_imgs[im]['type'] == 'click':
                    print('found - click.', im, im_pos)
                    pyautogui.click(200, 700,clicks=1, button='left',interval=0)
                elif g_imgs[im]['type'] == 'esc':
                    print('found - esc.', im, im_pos)
                    pyautogui.press('esc',interval=0) 
                elif g_imgs[im]['type'] == 'yes_click':
                    print('found - yes click.', im, im_pos)
                    pyautogui.typewrite('y', interval=0)
                    pyautogui.click(200, 700,clicks=1, button='left',interval=0)
                elif g_imgs[im]['type'] == '2_click':
                    print('found - 2 click.', im, im_pos)
                    pyautogui.typewrite('2', interval=0)
                    pyautogui.click(200, 700,clicks=1, button='left',interval=0)
                break
            else:
                print('did not find', im)
        if found_img == 0:
            break


def mo_money(hunreds=1):
    global g_imgs
    if not pyautogui.locateOnScreen(g_imgs['planets_col_1']['im']):
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


def search_tech_tform():
    global g_imgs
    pyautogui.press('esc', interval=0)
    pyautogui.click(100, 100,clicks=1, button='left',interval=0)
    if pyautogui.locateOnScreen(g_imgs['tech_tform']['im']):
        print('need to set tech tform')
        pyautogui.press('esc',interval=0) 
    else:
        return
    for x in range(6):
        pyautogui.press('right',interval=0)
    for x in range(5):
        pyautogui.press('up',interval=0)
    for x in range(4):
        pyautogui.press('down',interval=0)
    pyautogui.click(interval=0)
    pyautogui.click(100, 100,clicks=1, button='left',interval=0)


def check_fact_reserv():
    global g_imgs
    pyautogui.press('esc', interval=0)
    pyautogui.click(100, 100,clicks=1, button='left',interval=0)
    if pyautogui.locateOnScreen(g_imgs['fact_reserv']['im']):
        print('need to clear factory reserve')
        for x in range(6):
            pyautogui.press('right',interval=0)
        for x in range(5):
            pyautogui.press('up',interval=0)
        for x in range(3):
            pyautogui.press('down',interval=0)
        pyautogui.press('left',interval=0)
        for x in range(50):
            pyautogui.click(interval=0)
        pyautogui.click(100, 100,clicks=1, button='left',interval=0)


def check_missle_bases():
    global g_imgs
    pyautogui.press('esc', interval=0)
    pyautogui.click(100, 100,clicks=1, button='left',interval=0)
    miss_pos = pyautogui.locateOnScreen(g_imgs['missle_bases']['im'])
    if miss_pos:
        print('need to set missle bases', miss_pos)
        pyautogui.click(miss_pos.left + 140, miss_pos.top + 25, clicks=1, button='left',interval=0)


def map_current_view():
    global map_data, view_map_data
    print('starting view map stuff')
    def new_star_test(x2, y2, pkey):
        MIN_DIST_NEEDED = 50
        for ext_star in view_map_data:
            x1 = view_map_data[ext_star]['x']
            y1 = view_map_data[ext_star]['y']
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if distance < MIN_DIST_NEEDED:
                return False
        found_ship = find_space_ships(x2, y2)
        view_map_data.update({pkey: {
            'x':x2, 
            'y':y2,
            'type': '',
            'is_selected': False,
            'is_ship': found_ship
            }})
        return True
    def new_selected_pix(x, y):
        selected_data.append((x, y))
    def centroid_of_selected():
        MIN_CENTROID = 30
        if selected_data:
            x = [p[0] for p in selected_data]
            y = [p[1] for p in selected_data]
            centroid = (sum(x) / len(selected_data), sum(y) / len(selected_data))
            ### mark selected
            for ext_star in view_map_data:
                x1 = view_map_data[ext_star]['x']
                y1 = view_map_data[ext_star]['y']
                distance = math.sqrt((centroid[0] - x1)**2 + (centroid[1] - y1)**2)
                if distance < MIN_CENTROID:
                    # print(ext_star, x1, y1, distance, 'FOUND IT...')
                    view_map_data[ext_star]['is_selected'] = True
                # else:
                #     print(ext_star, x1, y1, distance)
            return centroid
        else:
            return None
    def find_space_ships(g_x, g_y):
        size = 5
        min_pix_bw_ct = 8
        my_color_mix = {}
        bw_pixels = 0
        bw_color_key = [(255, 255, 255)]
        found_ship = False
        for x in range(g_x - size, g_x + size):
            for y in range(g_y - size, g_y + size):
                tpix = im.getpixel((x, y))
                if tpix in bw_color_key:
                    bw_pixels += 1
                # print(x, y, tpix)
                if tpix not in my_color_mix:
                    my_color_mix.update({tpix: 1})
                else:
                    my_color_mix[tpix] += 1
                im_new[x, y] = (0, 0, 255)
        if bw_pixels >= min_pix_bw_ct and len(my_color_mix) < 4:
            found_ship = True
        # print(len(my_color_mix), bw_pixels, found_ship)
        return found_ship
    def mark_view_map_tmp_img(x, y, color_tuple):
        for x_rng in range(-3, 3):
            for r_rng in range (-3, 3):
                im_new[x + x_rng, y + r_rng] = color_tuple
    stime = time()
    color_mix = {}
    pix_two_replace = [
        ### grays
        (0,0,0), (44,44,44), (32,32,32), (28,28,28), (105,105,105), (25, 12, 0), (19, 16, 11),
        (77, 77, 77), (211, 211, 211), (42, 7, 3), (0, 60, 0), (11, 13, 32), 
        ### pinks
        (167, 25, 159), (123, 19, 117), (97, 15, 81), (68, 10, 66), (37, 5, 36), (63, 13, 7),
        (201, 215, 231), (244, 229, 194), (48, 26, 15), (74, 42, 73)
        ] 
    planet_values = [(183, 226, 185), (245, 200, 203), (237, 194, 235), (151, 180, 210), 
        (232, 205, 135), (201, 215, 231), (244, 229, 194), (195, 195, 195), (166, 166, 166),
        (227, 183, 81), (28, 71, 114)
        ]
    selected_values = [(52, 109, 84), (32, 85, 65), (72, 133, 103)]
    view_map_data = {}
    selected_data = []
    selected_centroid = None
    pyautogui.click(GS.x+1000+35, GS.y+70, clicks=1, button='left', interval=0)
    pyautogui.press(['esc', 'esc'], interval=0)
    sleep(1)
    im = pyautogui.screenshot(region=(GS.x+30, GS.y+58, 975, 765))
    im.save(os.path.join('tmp', 'view_map.PNG'), "PNG")
    fn_p_out =  os.path.join('tmp', 'view_map_out.PNG')
    im_new = im.load()
    width, height = im.size
    ### clean up back ground
    for y in range(5, height-5):
        for x in range(5, width-5):
            pix_key = f'{x}_{y}'
            pix = im.getpixel((x, y))
            if pix in pix_two_replace:
                im_new[x, y] = (255, 255, 255)
            if pix in selected_values:
                new_selected_pix(x, y)
                for x_rng in range(-3, 3):
                    im_new[x + x_rng, y] = (0, 255, 0)
    ### scan night sky for objects
    for y in range(5, height-5):
        for x in range(5, width-5):
            pix_key = f'{x}_{y}'
            pix = im.getpixel((x, y))
            if pix in planet_values:
                if new_star_test(x, y, pix_key):
                    # is_ship = view_map_data[pix_key]['is_ship']
                    print(f'found object at {x}, {y} with color {pix}')
                    mark_view_map_tmp_img(x, y, (255, 0, 0))
                    # if is_ship:
                    #     print(f'found planet at {x}, {y} with color {pix}')
                    #     mark_view_map_tmp_img(x, y, (0, 255, 0))
                    # else:
                    #     # print(f'found ship   at {x}, {y} with color {pix}')
                    #     mark_view_map_tmp_img(x, y, (255, 0, 0))
    im.save(fn_p_out) 
    process_time = round(time() - stime, 3)
    selected_centroid = centroid_of_selected()
    print(f'process_time = {process_time}.')
    print(f'found {len(view_map_data)} objects on veiw map.')
    print(f'found {len(selected_data)} selection pixs on veiw map & the centroid is {selected_centroid}.')
    for v_item in view_map_data:
        star_agls = build_angle_array(v_item, view_map_data)
        view_map_data[v_item].update({'star_agls': star_agls})


def save_map_data():
    global map_data
    with open(os.path.join('data', 'map_data.json'), 'w') as fp:
        json.dump(map_data, fp)


def load_map_data():
    global map_data
    with open(os.path.join('data', 'map_data.json'), 'r') as fp:
        map_data = json.load(fp)


def map_the_galaxy():
    global g_imgs, app_cor, map_data
    print('starting map stuff')
    if os.path.isfile(os.path.join('data', 'map_data.json')):
        load_map_data()
        return
    def new_start_test(x2, y2):
        MIN_DIST_NEEDED = 20
        for ext_star in map_data:
            x1 = map_data[ext_star]['x']
            y1 = map_data[ext_star]['y']
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if distance < MIN_DIST_NEEDED:
                return False
        return True
    pyautogui.click(GS.x+1000+35, GS.y+70, clicks=1, button='left', interval=0)
    pyautogui.press(['esc', 'esc', 'm', 'e'], interval=0)
    sleep(1)
    im = pyautogui.screenshot(region=(GS.x+35, GS.y+62, 1000, 830))
    im.save(os.path.join('tmp', 'map.PNG'), "PNG")
    fn_p_out =  os.path.join('tmp', 'map_out.PNG')
    im_new = im.load()
    width, height = im.size
    # print(im.size)
    ### star search
    for pend_star in STAR_PATTERNS:
        pend_star_pattern = pend_star['pattern']
        pend_star_name = pend_star['name']
        pend_star_pixel_size = len(pend_star_pattern)/3
        pix_x_s = int(pend_star_pixel_size/2)
        pix_x_e = int(pend_star_pixel_size) - pix_x_s
        # print(f'Start searching for {pend_star_name}')
        # print(f'pend_star len = {len(pend_star_pattern)}  pend_star_pixel_size = {pend_star_pixel_size}')
        # print(f'pix_x_s={pix_x_s}  pix_x_e={pix_x_e} ')
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
                        # print(f'NEW {pend_star_name} AT x={x}, y={y}')
                        ### creating a dot on the found star
                        for nex_y in range(-2,2):
                            for nex_x in range(-2,2):
                                im_new[x+nex_x, y+nex_y] = (255, 255, 255)
    for m_item in map_data:
        star_agls = build_angle_array(m_item, map_data)
        map_data[m_item].update({'star_agls': star_agls})
    im.save(fn_p_out)
    save_map_data()


def move_a_scout():
    # ship_scout ship_double_left ship_destination_is_out_of ship_eta, shut_accept, ship_fleep_deployment
    global g_imgs
    pyautogui.click(100, 100, clicks=1, button='left', interval=0)
    pyautogui.press('F6')
    pyautogui.press(['F5', 'F5'])
    sleep(.5)
    ship_left_most = pyautogui.locateOnScreen(g_imgs['ship_fleep_deployment']['im']).left
    ## clear counts
    db_left_pos = pyautogui.locateAllOnScreen(g_imgs['ship_double_left']['im'])
    for db_arw in db_left_pos:
        pyautogui.moveTo(db_arw.left + 20, db_arw.top + 20, duration=0)
        pyautogui.click()
    ## select one
    scout_pos = pyautogui.locateOnScreen(g_imgs['ship_scout']['im'])
    print(scout_pos)
    pyautogui.moveTo(scout_pos.left+140, scout_pos.top+80, duration=0)
    pyautogui.click()
    ## find planets
    left_iter = 0
    found_dest = False
    while True:
        pyautogui.press(['left','left','left','left','left','left'])
        if left_iter > 0:
            pyautogui.press('down')
        left_iter += 1
        pyautogui.press('enter')
        sleep(.5)
        while True:
            ship_dest_oor = pyautogui.locateOnScreen(g_imgs['ship_destination_is_out_of']['im'])
            ship_eta = pyautogui.locateOnScreen(g_imgs['ship_eta']['im'])
            currentMouseX, currentMouseY = pyautogui.position()
            print(currentMouseX, currentMouseY)
            if ship_eta:
                print('ship_eta', ship_eta)
                pyautogui.click(g_imgs['shut_accept']['path'])
                found_dest = True
                break
            elif ship_dest_oor:
                print('ship_dest_oor', ship_dest_oor)
                pyautogui.press('right')
                pyautogui.press('enter')
            elif currentMouseX > ship_left_most:
                print('over too far')
                break
        if found_dest:
            break


def find_unknwon_system_on_view():
    global view_map_data
    for s_ct, s in enumerate(view_map_data, start=1):
        s_x = GS.x + 23 + view_map_data[s]['x']
        s_y = GS.y + 50 + view_map_data[s]['y']
        # print(s_ct, s, view_map_data[s])
        if s_ct == 1 and view_map_data[s]['is_selected']:
            continue
        pyautogui.moveTo(s_x, s_y, duration=0)
        pyautogui.click()
        sleep(.5)



def run_game():
    global g_imgs, map_data, view_map_data
    planet_check_inter = 5
    moola_count_inter = 10
    loop_count = 0
    try:
        while True:
            loop_count += 1
            ### continue with screen scanning   
            ms_pos = pyautogui.position()
            map_current_view()
            # print(view_map_data)
            ## moola cheat every 10 rounds
            # if loop_count % moola_count_inter == 0:
            #     mo_money(hunreds=20)
            ### check all planet settings
            # if loop_count % planet_check_inter == 0:
            #     search_tech_tform()
            #     check_missle_bases()
            #     check_fact_reserv()
            print(f'{loop_count} clicking n', ms_pos)
            pyautogui.typewrite('n')
            # sleep(3)
            # screen_for_esc_images()
            # if loop_count > 5:
            break
    except KeyboardInterrupt:
        print('\nDone.')


def match_current_to_galaxy():
    global map_data, view_map_data
    def mark_view_map_tmp_img(cord_key, img_pnt, color_tuple):
        size = 15
        x, y = cord_key.split('_')
        for r in range(-size, size):
            for s in range(3):
                img_pnt[int(x) + r, int(y) + s] = color_tuple
                img_pnt[int(x) + s, int(y) + r] = color_tuple
    ### load images
    map_p =  os.path.join('tmp', 'map_out.PNG')
    map_im = Image.open(map_p)
    map_im_new = map_im.load()
    view_p =  os.path.join('tmp', 'view_map_out.PNG')
    view_im = Image.open(view_p)
    view_im_new = view_im.load()
    ### find matching points
    for m_item in map_data:
        m_agls = set(map_data[m_item]['star_agls'])
        for v_item in view_map_data:
            v_agls = set(view_map_data[v_item]['star_agls'])
            matching_angles = m_agls & v_agls
            if len(matching_angles) >= 4:
                mark_view_map_tmp_img(m_item, map_im_new, (0, 255, 0))
                mark_view_map_tmp_img(v_item, view_im_new, (0, 0, 0))
                print(m_item, v_item, matching_angles)
    ### save images
    map_im.save(map_p) 
    view_im.save(view_p)

def main():
    global g_imgs, map_data
    map_data = {}
    load_escape_imgs()
    look_for_basics()
    map_the_galaxy()
    map_current_view()
    # find_unknwon_system_on_view()
    match_current_to_galaxy()
    # mo_money(hunreds=20)
    # run_game()


if __name__ == "__main__":
    main()