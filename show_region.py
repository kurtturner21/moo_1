
import moo_auto as ma

"""
Purpose: Show a part of screen shot for training.
"""


def main():
    ma.app_config()
    ma.look_for_dos_box(do_click=True)
    ma.monitor_systems()


if __name__ == "__main__":
    main()