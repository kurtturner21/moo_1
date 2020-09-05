
"""
Managing system data.
"""

import pyautogui as pag
import os
import json
from time import sleep
import imagehash

import moo_auto as ma


def get_idle_game_string():
    """
    Return a string of the game bar img hash and the mouse pointer.
    """
    ma.GS.mouse_pos = str(pag.position())
    ma.GS.im_app = ma.get_screen_shot()
    game_bar_hash = 'c88cafe3b7008a3f'
    game_bar_cords = (50,830,1100,910)
    game_bar_img = ma.GS.im_app.crop((game_bar_cords))
    game_bar_current_hash = str(imagehash.phash(game_bar_img))
    if game_bar_current_hash != game_bar_hash:
        return '---'
    else:
        return game_bar_current_hash + '-' + ma.GS.mouse_pos


def system_data_delete():
    system_data_path = os.path.join('data', 'system_data.json')
    if os.path.isfile(system_data_path):
        os.remove(system_data_path)


def system_data_write():
    system_data_path = os.path.join('data', 'system_data.json')
    with open(system_data_path, 'w') as fo:
        json.dump(ma.GS.system_data, fo, sort_keys=True, indent=4)


def system_data_read():
    system_data_path = os.path.join('data', 'system_data.json')
    if os.path.isfile(system_data_path):
        with open(system_data_path, 'r') as fi:
            ma.GS.system_data = json.load(fi)
    max_base_level_review()


def system_data_count():
    sys_count = 0
    for GS_key in ma.GS.system_data.keys():
        if not ma.GS.system_data[GS_key]['is_lost']:
            sys_count += 1
    return sys_count


def max_base_level_review():
    sys_count = len(ma.GS.system_data)
    if sys_count:
        new_bases_level = int(system_data_count() * 1)
        if new_bases_level < 2:
            new_bases_level = 2
        ma.GS.max_bases_per_system = new_bases_level


def max_base_level_report():
    print(f"max_bases_per_system = {ma.GS.max_bases_per_system}")
    print(f"max_bases_to_prune = {ma.GS.max_bases_to_prune}")


def gen_popup_report():
    print('=======================')
    print('POPUP MESSAGE REPORT:')
    for m in ma.GS.popup_msgs:
        print(f'{m:<20} {ma.GS.popup_msgs[m]}')
    print('=======================')


def review_systems():
    def check_for_population_diff():
        pop_cords = [(1153,297,1208,324), (1270,225,1325,252)]
        pop_text_colors = [[(255,218,76)], [(65,183,33)]]
        pop_hashs = []
        for x in [0,1]:
            im_pop_tmp = ma.GS.im_app.crop((pop_cords[x]))
            im_pop_text_img = ma.get_image_text(im_pop_tmp, pop_text_colors[x])[1]
            im_pop_hash = str(imagehash.phash(im_pop_text_img))
            pop_hashs.append(im_pop_hash)
        if '000000000000' in pop_hashs[1]:
            return False    ### the MAX is missing
        elif pop_hashs[0] == pop_hashs[1]:
            return False    ### they are the same
        else:
            return True   ### they are different
    def check_for_shield_building():
        shield_hash='f07f8b5aa28ec4a1'
        none_hash='c47f986d8285c39b'
        sys_clean_cords=(1280,440,1400,480)
        im_n = ma.GS.im_app.crop((sys_clean_cords))
        im_n_hash = str(imagehash.phash(im_n))
        if im_n_hash == none_hash:
            return 0
        if im_n_hash == shield_hash:
            return 1
        else:
            return 2
    def get_system_name():
        ### name
        system_name_dict = ma.hashdata.sysnames()
        im_n_hash = '00000000000'
        while im_n_hash == '00000000000':
            ma.GS.im_app = ma.get_screen_shot()
            im_n = ma.GS.im_app.crop((sys_name_cords))
            im_text, im_n_bw = ma.get_image_text(im_n, sys_name_colors)
            im_n_hash = str(imagehash.phash(im_n_bw))
        if im_n_hash in system_name_dict:
            im_text = system_name_dict[im_n_hash]
        else:
            im_n_bw.save(f'.\\tmp\\{im_n_hash}.PNG')
        return im_n_hash, im_text
    def return_base_count():
        base_hash_dict = ma.hashdata.bases()
        base_ct_cords=(1340,290,1420,340)
        base_ct_colors=[(255,218,76)]
        ma.GS.im_app = ma.get_screen_shot()
        base_im = ma.GS.im_app.crop((base_ct_cords))
        im_t_img = ma.get_image_text(base_im, base_ct_colors)[1]
        base_hash = str(imagehash.phash(im_t_img))
        if base_hash in base_hash_dict:
            return base_hash_dict[base_hash]
        else:
            im_t_img.save(f'.\\tmp\\{base_hash}.PNG')
            return 100
    def review_ship_builders():
        """If any amount of ship building, then push almost all RD to ships."""
        is_ship_building_hash='9887e638c1e4c6ee'
        is_ship_building_cords=(1050,390,1145,430)
        ma.GS.im_app = ma.get_screen_shot()
        im = ma.GS.im_app.crop((is_ship_building_cords))
        im_hash = str(imagehash.phash(im))
        if im_hash == is_ship_building_hash:
            pag.moveTo(ma.GS.x + 1170, ma.GS.y + 615, duration=.1)
            pag.click(ma.GS.x + 1170, ma.GS.y + 615, clicks=1, button='left',interval=.1)
            return True
        else:
            return False
    def get_if_wasted():
        sys_waste_hash='f01e8a71625e792d'
        sys_clean_cords=(1280,530,1400,580)
        ma.GS.im_app = ma.get_screen_shot()
        im_n = ma.GS.im_app.crop((sys_clean_cords))
        im_n_hash = str(imagehash.phash(im_n))
        if im_n_hash == sys_waste_hash:
            return True
        else:
            return False
    def get_clean_baby():
        sleep(.1)
        while get_if_wasted():
            pag.moveTo(ma.GS.x + 1270, ma.GS.y + 560, duration=.1)
            pag.click(ma.GS.x + 1270, ma.GS.y + 560, clicks=1, button='left',interval=.1)
    def set_base_investment(base_count):
        """Click the sweat spot for building bases."""
        if base_count >= ma.GS.max_bases_per_system:
            x = 1145
        else:
            x = ma.GS.click_bases[0]
        y = ma.GS.click_bases[1]
        pag.moveTo(ma.GS.x + x, ma.GS.y + y, duration=.1)
        pag.click(ma.GS.x + x, ma.GS.y + y, clicks=1, button='left',interval=.1)
        sleep(.1)
    def base_count_n_control():
        # x = 316 is 0%
        # x = 432 is 50%
        # x = 544 is 100%
        base_ct = return_base_count()
        while True:
            if base_ct > ma.GS.max_bases_to_prune:
                pag.press('b', interval=0)
                pag.moveTo(ma.GS.x + 335, ma.GS.y + 415, duration=.1)
                pag.click(ma.GS.x + 335, ma.GS.y + 415, clicks=1, button='left',interval=.1)
                pag.moveTo(ma.GS.x + 640, ma.GS.y + 500, duration=.1)
                pag.click(ma.GS.x + 640, ma.GS.y + 500, clicks=1, button='left',interval=.1)
                base_ct = return_base_count()
            else:
                break
        return base_ct
    def boost_pop_investment():
        pag.moveTo(ma.GS.x + 1230, ma.GS.y + 560, duration=.1)
        pag.click(ma.GS.x + 1230, ma.GS.y + 560, clicks=1, button='left',interval=.1)
    system_data_read()
    max_base_level_review()
    print('=======================')
    print('Running system review.')
    max_base_level_report()
    this_run_systems = set()  ### preventing endless runs.
    sys_name_cords=(1050,60,1400,120)
    sys_name_colors=[(232,205,135),(227,183,81),(215,162,31),(244,229,194)]
    sys_ct = 0
    pics_list = []
    while True:
        ### loop control stuff
        pag.press('f2', interval=0)
        sleep(.5)
        system_hash, system_name = get_system_name()
        if system_hash in this_run_systems:
            break
        sys_ct += 1
        this_run_systems.add(system_hash)
        #### do stuff with system
        is_population_diff = check_for_population_diff()
        is_building_shild = check_for_shield_building()
        base_ct = base_count_n_control()
        if is_population_diff:
            boost_pop_investment()
        if is_building_shild != 1:
            set_base_investment(base_ct)
        get_clean_baby()
        a_builder = review_ship_builders()
        print(f'{sys_ct:<4} {system_name:<10} Syards:{int(a_builder):<2} B:{base_ct:<3}{is_building_shild:<3}')
        ma.GS.system_data.update({system_hash: {
                "name": system_name,
                "base_ct": base_ct,
                "is_building_shild": is_building_shild,
                "is_population_diff": is_population_diff,
                "is_lost": 0
            }
        })
    # for i in pics_list:
    #     i.show()
    ma.GS.lost_system_keys.clear()
    for GS_key in ma.GS.system_data.keys():
        if GS_key not in this_run_systems:
            print(f'>>>>>>{GS_key} was a lost system {ma.GS.system_data[GS_key]}')
            ma.GS.lost_system_keys.add(GS_key)
            ma.GS.system_data[GS_key]['is_lost'] = 1
    ma.move_pointer_to_home()
    system_data_write()
    print(f'we have {system_data_count()} systems.')
    print('=======================')

