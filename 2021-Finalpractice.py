import numpy as np
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)


def r(n):
    r = 10*n + 5
    return r

# equation to solve: r(n) = 10n + 5 (linear)
for n in range (20):
    red = r(n)
    pixels[n] = (red, 0, 0)
    print(n,red)
