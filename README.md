# XWindows
Linux python client for Xserver to access windows information and automate keypresses

### Table of contents
____

* [About the package](#about-the-package)
    * [Problems](#problems)
    * [Solutions](#solutions)
* [Resources](#resources)
* [Documentation](#documentation)
    * [Installing](#installation)
    * [Importing](#importing)
    * [Initialising](#initialising)
* [Methods](#methods)
    * [Get Active Windows](#get-active-windows)
    * [Get Window Screen](#get-window-screen)
    * [Get Window Slice](#get-window-slice)
    * [Press Key](#press-key)
* [Author](#author)
* [Features Planned to add](#features-planned-to-add)

### About the package
I created this package mainly to solve some problems I faced using __opencv__ on linux.

### Problems

---------

* Obtaining Window screen in fast and efficient way
    * Every time we want to capture screen we have to take screen shot 
    with 3rd party packages like __pyautogui__ and then convert into opencv image which is both slow and inefficient.
* No modules like pywin32 for linux to access internal apis

### Solutions

-----

* This package provides native Xserver interaction from python using [__python-xlib__](https://pypi.org/project/python-xlib/) package.
* This package provides the following features
    * Get active windows (active means all the visual application windows)
    * Get geometry of a particular window (height, width, x, y coordinates)
    * Get screenshot of a particular window in raw bytes or PIL image format
    * Automate keypresses
> Since all these operations are done using native apis you will experience increase in performance

### Resources

* [native xlib documentation](https://tronche.com/gui/x/xlib/)
    * This documentation is written for C / C++ language and you need to have a bit of knowledge to understand this documentation.
    * No availability of lot of examples makes it even harder for beginners to understand the documentation.
* [python-xlib documentation](https://python-xlib.github.io/)
    * The documentation is still not completed but the devs are updating it continuosly.
* [My Notes](https://www.notion.so/Linux-get-Window-python-dfe7093c5a3d49bda03b0d880b9c0d53)
    * I have noted down some important topics to understand XServer and xlib library documentation. Hope it helps :)

### Documentation

### Installation

```bash
pip install XWindows
```

If you use python3, then use following command

```bash
pip3 install XWindows
```


### Importing

```python
import XWindows

# If you want to import seperate components

from XWindows import windows
from XWindows import keys

# If you want to import seperate components and functionality
# This way of importing is preffered cause you don't have to add whole namespace again and again
# This will be used to explain the features further

from XWindows.windows import Windows
from XWindows.keys import Keys
```

### Initialising

```python
# intialising windows object
windows = Windows()

# dispose windows object
windows.dispose()
```

### Methods

#### Get Active windows
* Here active indicates the visual application windows

```python
activeWindows = windows.getActiveWindows()
print(activeWindows)

# The result will be list of tuples of (window_id, window_title)
# [
#   (29360135, 'firstPy'), 
#   (33554442, 'python3'), 
#   (39845895, b'windows.py - firstPy - Visual Studio Code'), 
#   (39845920, b'test.py - XWindows - Visual Studio Code'), 
#   (52428803, b'Linux get Window (python) \xe2\x80\x94 Mozilla Firefox')
# ]

# These window_id's change everytime you close and open a particular window
```

#### Get Window geometry

```python
# Syntax windows.getWindowGeometry(window_id)

geometry = windows.getWindowGeometry(29360135)
print(geometry)

# returns a tuple of (x, y, width, height)
# (302, 141, 1375, 691)
```

#### Get Window Screen

```python
# syntax: windows.getWindowScreen(window_id, bytes_format=False)
# syntax: windows.getWindowScreen(window_id, bytes_format=True) for raw data

# returns image in PIL Image format
screen = windows.getWindowScreen(29360135)

# returns tuple of (image in bytes, image width, image height)
screen_bytes_format = windows.getWindowScreen(29360135, bytes_format=True)
```

#### Get Window Slice

* Use this to get certain portion of a screen

```python
# syntax: windows.getWindowSlice(window_id, x, y, width, height)
# syntax: windows.getWindowSlice(window_id, x, y, width, height, bytes_format=True)

window_id = 29360135
(x, y, width, height) = windows.getWindowGeometry(window_id)

# returns data in PIL Image format
window_slice = windows.getWindowSlice(window_id, x, y, width, height)

# return image data in bytes format
window_slice_bytes_format = windows.getWindowSlice(window_id, x, y, width, height)
```

#### Press Key

```python
# syntax: windows.pressKey([keysyms,], window_id)
# all keysyms are accessible using windows.keys

# this below sends A keys pressed signal to window with id window_id
windows.pressKey([windows.keys.A], window_id)
```

*  [keysyms,] - list of keys you want to simulate
*  send the keys in the order you would press in keyboard
*  for example [windows.keys.A,] = [windows.keys.Shift_L, windows.keys.a]

### Author

sleepingsaint @github

> Contributions or PR's of any kind are appreciated 

### Features Planned to add

[ ] Automate mouse movements<br>
[ ] Get windows with title rather than window_id