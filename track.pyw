'''Tracks mouse coordinates and flushes to file'''
from subprocess import PIPE, Popen
from datetime import datetime
import platform
import os

OS = platform.system()
DIRECTORY_NAME = './data/'

try:
    os.makedirs(DIRECTORY_NAME)
except OSError:
    pass

def get_date():
    return datetime.now().strftime('%d-%b-%Y_%H-%M-%S-%f')

def get_mouse_win():
    '''gets current mouse coordinates from Windows'''
    try:
        return map(str, win32gui.GetCursorPos())
    except ImportError, error:
        print error
        return (None, None)

def get_mouse_linux():
    """get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]

def get_mouse_osx():
    '''gets current mouse coordinates from Macintosh'''
    result = Popen(CMD,
                   stdin=PIPE,
                   stdout=PIPE,
                   bufsize=1).stdout.read().strip()
    return result.split('\n')


if OS == 'Darwin':
    CMD = './MouseTools -location'.split()
    MOUSEFN = get_mouse_osx
elif OS == 'Windows':
    import win32gui
    from pywintypes import error as os_errors
    MOUSEFN = get_mouse_win
elif OS == 'Linux':
    try:
        from Xlib import display
    except ImportError:
        errmsg = "Please install Xlib library for python \n"
        errmsg += "sudo apt-get install python-xlib"
        errmsg += "\n or try \n"
        errmsg += "conda install --channel https://conda.anaconda.org/erik \
                   python-xlib"
        raise Exception(errmsg)
    MOUSEFN = get_mouse_linux

if __name__ == '__main__':
    try:
        DATA = []
        OLDX, OLDY = 0, 0
        FNAME = get_date()
        FNAME = ''.join([DIRECTORY_NAME, 'mousecoords_', FNAME, '.csv'])
        print "writing to: ", FNAME
        with open(FNAME, 'w') as f:
            while True:
                try:
                    NEWX, NEWY = MOUSEFN()
                    # logs mouse coordinates if mouse moves
                    if not (NEWX == OLDX and NEWY == OLDY):
                        TIMESTAMP = get_date()
                        DATA = ','.join(map(str, [TIMESTAMP, NEWX, NEWY, '\n']))
                        f.write(DATA)
                        OLDX, OLDY = NEWX, NEWY
                except Exception as err:
                    print err
                    pass
    except (KeyboardInterrupt, SystemExit), error:
        print "Exited : ", datetime.now(), error
        exit
