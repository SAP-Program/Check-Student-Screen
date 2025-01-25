# by parsasafaie
# this function returns complete title of active window

import pygetwindow as gw

def get_window_name():
    active_window = gw.getActiveWindow()
    return active_window.title
    