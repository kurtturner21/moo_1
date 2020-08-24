
import moo_auto as ma

"""
Purpose: Show a part of screen shot for training.
"""


def main():
    ma.app_config()
    ma.look_for_dos_box(do_click=True)
    # ma.monitor_systems()
    ma.kill_popups_two()
    # while True:
    #     ms_pos = ma.pyautogui.position()
    #     rel_x = ms_pos.x - ma.GS.x
    #     rel_y = ms_pos.y - ma.GS.y
    #     ma.pyautogui.moveTo(ma.GS.x + 1140, ma.GS.y + 465, duration=.2)
    #     print(f'clicking n', (rel_x, rel_y))
    #     ma.sleep(1)


if __name__ == "__main__":
    main()