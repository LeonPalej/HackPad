import board
from kb import MyKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

from kmk.extensions.rgb import RGB

import busio
import displayio
import terminalio
from adafruit_display_text import label  # this might showup as an error, thats becaus this is a .mpy, the controler can read it but the IDE cant, it will still work
import adafruit_displayio_ssd1306

keyboard = MyKeyboard()

# Rotary encoder setup
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D9, board.D10, None),) # Pin A, Pin B, Switch Pin (In Matrix)
encoder_handler.map = [((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN),)]

# Key map setup
keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
        KC.N7, KC.N8, KC.MUTE
    ]
]

# RGB setup
rgb = RGB(
    pixel_pin=board.D7, # Pin for the RGB diodes data in
    num_pixels=8,       # Number of RGB diodes in the strip
    val_limit=100,      # Limit the brightness of the RGB diodes to 100/255
    animation_speed=3,
)
keyboard.extensions.append(rgb)

# Display setup
displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 32
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
splash = displayio.Group()
display.show(splash)

text_area = label.Label(terminalio.FONT, text="Hello World!", color=0xFFFFFF, x=10, y=15)
splash.append(text_area)

if __name__ == '__main__':
    keyboard.go()