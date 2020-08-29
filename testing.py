
import moo_auto as ma

"""
Purpose: Show a part of screen shot for training.
"""


def main():
    ma.app_config()
    ma.look_for_dos_box()
    ma.review_systems()
    # ma.kill_popups_two()

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
    
    # test_hash=''
    # test_clean_cords=(1340,290,1420,340)
    # test_clean_colors=[(255,218,76)]
    # ma.GS.im_app = ma.get_screen_shot()
    # im_n = ma.GS.im_app.crop((test_clean_cords))
    # im_n_hash = str(ma.imagehash.phash(im_n))
    # im_text, im_text_img = ma.get_image_text(im_n, test_clean_colors)
    # im_n.show()
    # im_text_img.show()
    # print(im_n_hash, im_text)


if __name__ == "__main__":
    main()