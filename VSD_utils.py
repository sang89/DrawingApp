import ctypes

def show_message_box(msg, title):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, msg, title, 0)


