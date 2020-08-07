
import argparse
import moo_auto as ma

"""
Purpose: Show a part of screen shot for training.
"""

def app_config(): 
    parser = argparse.ArgumentParser(description='MOO button clicker.')
    parser.add_argument('-x', default=20, type=int)
    parser.add_argument('-y', default=40, type=int)
    parser.add_argument('-w', default=300, type=int)
    parser.add_argument('-hi', default=100, type=int)
    args = parser.parse_args()
    return args


def main():
    global app_vars
    app_vars = app_config()
    ma.look_for_dos_box(do_click=False)
    x = app_vars.x
    y = app_vars.y
    w = app_vars.w
    h = app_vars.hi
    ma.show_region(x, y, w, h)


if __name__ == "__main__":
    main()