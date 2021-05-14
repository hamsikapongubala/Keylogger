from multiprocessing import Process, freeze_support
from PIL import ImageGrab

screenshot_file = "screenshot.png"

def screenshot():
    im = ImageGrab.grab()
    im.save(screenshot_file)

screenshot()
