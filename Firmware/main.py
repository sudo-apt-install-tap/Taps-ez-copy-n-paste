import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.extensions.RGB import RGB
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

# 1. SCANNER SETUP
# pull=True is vital for XIAO to stop 'ghost' keypresses crashing the board
keyboard.matrix = KeysScanner(
    pins=[board.RX, board.SCK, board.MISO, board.MOSI],
    value_when_pressed=False,
    pull=True
)

# 2. RGB SETUP
rgb = RGB(pixel_pin=board.TX, num_pixels=1, val_limit=50)
keyboard.extensions.append(rgb)

# 3. DISPLAY SETUP
i2c_bus = busio.I2C(board.SCL, board.SDA)
driver = SSD1306(i2c=i2c_bus, device_address=0x3C)

# We define the labels as a list first
my_labels = [
    TextEntry(x=0, y=0, text='SS    | COPY'),
    TextEntry(x=0, y=12, text='-----------'),
    TextEntry(x=0, y=22, text='CUT   | PASTE'),
]

# Create the extension
# setting 'show_all_details=False' helps hide the "DeviceReport" logs
display_ext = Display(
    display=driver,
    entries=my_labels,
    width=128,
    height=32,
    dim_time=0, # Prevents screen from turning off
)
keyboard.extensions.append(display_ext)

# 4. KEYMAP
keyboard.keymap = [[
    KC.LWIN(KC.LSHIFT(KC.S)),
    KC.LCTRL(KC.C),
    KC.LCTRL(KC.X),
    KC.LCTRL(KC.V),
]]

if __name__ == '__main__':
    keyboard.go()
