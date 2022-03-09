import time
from pynput.mouse import Controller

mouse = Controller()

# Read pointer position
def mouse_position():
    global position
    position = ('Mouse Position is {0}'.format(mouse.position))
    print(position, end="")
    time.sleep(0.1)
    print("\r", end="")

while True:
    mouse_position()
