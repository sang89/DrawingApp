import ctypes

def show_message_box(msg, title):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, msg, title, 0)


# We want to map the interval (a, b) one to one to (c, d)
# Returning the coefficients in f(x) = mx + n
def mapIntervals(a, b, c, d):
    m  = (c - d) / (a - b)
    n = c - m * a
    return m, n

