
import moo_auto as ma

"""
Purpose: Show a part of screen shot for training.
"""


def main():
    ma.app_config()
    ma.look_for_dos_box(do_click=True)
    # ma.kill_popups_two()
    ma.review_systems()

    
    # test_hash='9887e638c1e4c6ee'
    # test_clean_cords=(1050,390,1145,430)
    # ma.GS.im_app = ma.get_screen_shot()
    # im_n = ma.GS.im_app.crop((test_clean_cords))
    # im_n_hash = str(ma.imagehash.phash(im_n))
    # im_n.show()
    # print(im_n_hash)


if __name__ == "__main__":
    main()