'''Tracks mouse coordinates and flushes to file'''
from subprocess import PIPE, Popen
from datetime import datetime
import platform


OS = platform.system()


def get_date():
    return datetime.now().strftime('%d-%b-%Y_%H-%M-%S-%f')

if OS == 'Darwin':
    CMD = './MouseTools -location'.split()
    MOUSEFN = 'get_mouse_osx'
elif OS == 'Windows':
    import win32gui
    MOUSEFN = 'get_mouse_win'


def get_mouse_win():
    '''gets current mouse coordinates from Windows'''
    try:
        return map(str, win32gui.GetCursorPos())
    except ImportError, error:
        print error
        return (None, None)


def get_mouse_osx():
    '''gets current mouse coordinates from Macintosh'''
    result = Popen(CMD,
                   stdin=PIPE,
                   stdout=PIPE,
                   bufsize=1).stdout.read().strip()
    return result.split('\n')

if __name__ == '__main__':
    try:
        DATA = []
        OLDX, OLDY = 0, 0
        FNAME = get_date()
        FNAME = ''.join(['mousecoords_', FNAME, '.csv'])
        with open(FNAME, 'w') as f:
            while True:
                NEWX, NEWY = eval('%s()' % MOUSEFN)
                # logs mouse coordinates if mouse moves
                if not (NEWX == OLDX and NEWY == OLDY):
                    TIMESTAMP = get_date()
                    DATA = ','.join([TIMESTAMP, NEWX, NEWY, '\n'])
                    f.write(DATA)
                    OLDX, OLDY = NEWX, NEWY
                    print NEWX, NEWY
    except (KeyboardInterrupt, SystemExit), error:
        print datetime.now(), error
