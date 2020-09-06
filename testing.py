
import moo_auto as ma

"""
Purpose: Show a part of screen shot for training.
"""


def main():
    ma.app_config()
    ma.look_for_dos_box()
    ma.system_data_read()
    # ma.review_systems()
    ma.kpops.kill_popups_two()


    ### where are the ms cords.
    # while True:
    #     ms_pos = ma.pag.position()
    #     rel_x = ms_pos.x - ma.GS.x
    #     rel_y = ms_pos.y - ma.GS.y
    #     print(rel_x, rel_y)
    #     ma.sleep(1)


    ## idle testing
    # last_hash = ''
    # while True:
    #     idle_game_string = ma.get_idle_game_string()
    #     if idle_game_string == '---':
    #         print(idle_game_string, ' - not normal')
    #     elif last_hash == idle_game_string:
    #         print(idle_game_string, ' - same')
    #     else:
    #         print(idle_game_string, ' - different')
    #         last_hash = idle_game_string
    #     ma.sleep(1)


    # idle_game_string = ma.get_idle_game_string()
    
    # ma.GS.im_app = ma.get_screen_shot()

    # # test_hash=''
    # test_clean_cords=(1270,225,1325,252)
    # test_clean_colors=[(65,183,33)]
    # im_n = ma.GS.im_app.crop((test_clean_cords))
    # im_text, im_text_img = ma.get_image_text(im_n, test_clean_colors)
    # im_n_hash = str(ma.imagehash.phash(im_text_img))
    # # im_n.show()
    # # im_text_img.show()
    # print(im_n_hash, im_text_img.size)

    
    # test_clean_cords=(1153,297,1208,324)
    # test_clean_colors=[(255,218,76)]
    # im_n = ma.GS.im_app.crop((test_clean_cords))
    # # im_n_hash = str(ma.imagehash.phash(im_n))
    # im_text, im_text_img = ma.get_image_text(im_n, test_clean_colors)
    # im_n_hash = str(ma.imagehash.phash(im_text_img))
    # # im_n.show()
    # # im_text_img.show()
    # print(im_n_hash, im_text_img.size)


    # ma.GS.im_app = ma.get_screen_shot()
    # pop_cords = [(1153,297,1208,324), (1270,225,1325,252)]
    # pop_text_colors = [[(255,218,76)], [(65,183,33)]]
    # pop_hashs = []
    # for x in [0,1]:
    #     im_pop_tmp = ma.GS.im_app.crop((pop_cords[x]))
    #     im_pop_text_img = ma.get_image_text(im_pop_tmp, pop_text_colors[x])[1]
    #     im_pop_hash = str(ma.imagehash.phash(im_pop_text_img))
    #     pop_hashs.append(im_pop_hash)
    # ### exclude 8000000000000000
    # print(pop_hashs, pop_hashs[0] == pop_hashs[1])

if __name__ == "__main__":
    main()