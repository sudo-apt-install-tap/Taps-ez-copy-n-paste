from kmk.extensions.peg_oled_display import Oled, OledData, OledDisplayMode
import time

frames = [
    [
        "   /\\_/\\      ",
        "  ( o.o )>>>  ",
        "   > ^ <      ",
    ],
    [
        "   /\\_/\\      ",
        "  ( o.o ) >>> ",
        "   > ^ <      ",
    ],
    [
        "   /\\_/\\      ",
        "  ( o.o )  >>>",
        "   > ^ <      ",
    ],
]

oled_data = OledData()

oled = Oled(
    oled_data,
    oWidth=128,
    oHeight=32,
    toDisplay=OledDisplayMode.TXT,
)

keyboard.extensions.append(oled)

def animate():
    while True:
        for f in frames:
            oled.set_lines(f)
            time.sleep(0.1)

keyboard.before_matrix_scan.append(lambda: animate())
