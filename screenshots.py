from multiprocessing import Process, freeze_support
from PIL import ImageGrab

file_path = "/Users/hamsikapongubala"  # Enter the file path you want your files to be saved to
extend = "/"
screenshot_file = "screenshot.png"

def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_file)

screenshot()
