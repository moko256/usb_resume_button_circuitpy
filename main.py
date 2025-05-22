import board
import neopixel
import time
import usb_hid

from digitalio import DigitalInOut, Direction, Pull

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


kbd = Keyboard(usb_hid.devices)

btn = DigitalInOut(board.SWITCH)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

pressing = False

while True:
    new_pressing = btn.value
    if pressing != new_pressing:
        pressing = new_pressing

        if new_pressing:
            pixels.fill((2, 4, 6))
            kbd.send(Keycode.CONTROL)
        else:
            pixels.fill((0, 0, 0))
    if pressing:
        time.sleep(0.064)
    else:
        time.sleep(0.5)
