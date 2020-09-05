# MOO automation using python

This is my attept to automate Masters of Orion.  It is not complete.

# Setup

1. Screen scaling.

    - Change the size of text, apps and other items: 100%
    - Display resolution: 1920 x 1080

2. Install Steam
3. Install Masters of Orion 1 - MOO
    Steam emulates the MS Dos environment this with DOS Box.  At the time of this document the applicate for the MOO app was located here:

     - C:\Program Files (x86)\Steam\steamapps\common\Master of Orion 1

    Once Installed, make these changes in dosboxMOO1.conf.

    - fullscreen=false
    - windowresolution=1600x800
    - output=ddraw
    - autolock=false
    - core=auto
    - cycles=max

    Onwers Manual: C:\Program Files (x86)\Steam\steamapps\common\Master of Orion 1\manual.pdf
    
4. Download this REPO. I installed it at (c:\dev\moo_1).
5. Install python.

    ```dos
    C:\dev\moo_1>python --version
    Python 3.8.1
    ```

6. Install these pip packages (as administrator).

    - pip install pyautogui
    - pip install imagehash
    - pip install pytesseract

    Maybe later I will explore putting it into a virtual environment.

7. Download and install tesseract.  I used this source. 

    - https://github.com/UB-Mannheim/tesseract/wiki

    Make sure to put the application path in the "Environment Vars - Path" for the system.  In my case it was:

    - C:\Program Files\Tesseract-OCR

fv

## Helpful Links

- https://github.com/UB-Mannheim/tesseract/wiki
- https://github.com/UB-Mannheim/tesseract/wiki
- https://realpython.com/setting-up-a-simple-ocr-server/
- https://pillow.readthedocs.io/en/stable/reference/Image.html
- https://readthedocs.org/projects/pyautogui/downloads/pdf/latest/
- https://pypi.org/project/ImageHash/
- https://www.codementor.io/@isaib.cicourel/image-manipulation-in-python-du1089j1u
