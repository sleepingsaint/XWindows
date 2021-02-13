from Xlib import display, XK
from Xlib.Xatom import WINDOW
from Xlib.X import ZPixmap, CurrentTime, NONE, RevertToParent, KeyPress, KeyRelease
from Xlib.ext import xtest
from .keys import Keys

class Windows:
    def __init__(self):
        self.display = display.Display()
        self.root = self.display.screen().root
        self.keys = Keys()
    
    # returns geometry of the window
    # (x, y, width, height)
    def getWindowGeometry(self, id):
        win = self.display.create_resource_object('window', id)
        geometry = win.get_geometry()
        return (geometry.x, geometry.y, geometry.width, geometry.height)
    
    # list all the active windows along with their ids
    # active indicates all the windows opened
    def getActiveWindows(self):
        activeWindows = []
    
        query = self.root.get_full_property(self.display.intern_atom('_NET_CLIENT_LIST', 0), WINDOW)
        activeWindowsIds = query.value
        for winId in activeWindowsIds:
            win = self.display.create_resource_object('window', winId)
            
            title = win.get_wm_name()
            if len(title) == 0:
                titleQuery = win.get_full_property(self.display.intern_atom('_NET_WM_NAME'), 0)
                if titleQuery is not None:
                    title = titleQuery.value
            
            activeWindows.append((winId, title))
        
        return activeWindows
    
    # returns the image of the window selected
    # if bytes_format is True, return the image in bytes format
    # else return the image as PIL Image object
    def getWindowScreen(self, id, bytes_format=False):
        win = self.display.create_resource_object('window', id)
        geo = win.get_geometry()
        raw = win.get_image(0, 0, geo.width, geo.height, ZPixmap, 0xffffffff)

        if bytes_format:
            return (raw.data, geo.width, geo.height)

        from PIL import Image
        image = Image.frombytes("RGB", (geo.width, geo.height), raw.data, "raw", "BGRX")
        return image
   
    # gets specified region of the window
    # if bytes_format is True, return the image in bytes format
    # else return the image as PIL Image object  
    def getWindowSlice(self, id, x, y, width, height, bytes_format=False):
        win = self.display.create_resource_object('window', id)
        raw = win.get_image(x, y, width, height, ZPixmap, 0xffffffff)

        if bytes_format:
            return raw.data
        
        from PIL import Image
        image = Image.frombytes("RGB", (width, height), raw.data, "raw", "BGRX")
        return image

    def dispose(self):
        self.display.flush()


    # adding key press events
    # reference link
    # http://paulsrandomcontent.blogspot.com/2013/10/for-project-i-wanted-to-send-key.html
    def pressKey(self, keysyms, id):
        keycodes = []
        for keysym in keysyms:
            keycode = self.display.keysym_to_keycode(keysym)
            keycodes.append(keycode)

        win = self.display.create_resource_object('window', id)

        currentFocusedWindow = self.display.get_input_focus()
        self.display.set_input_focus(win, RevertToParent, CurrentTime)
        
        for keycode in keycodes:
            xtest.fake_input(self.display, KeyPress, keycode)
        for keycode in keycodes:
            xtest.fake_input(self.display, KeyRelease, keycode)
        
        self.display.set_input_focus(currentFocusedWindow.focus, RevertToParent, CurrentTime)

        self.display.sync()