# this practice is to alternate the colors
# while increaseing the brightness
import numpy as np
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)


def r(n):
    r = 10*n + 5
    return r

# equation to solve: r(n) = 10n + 5 (linear)
for n in range (n):
    red = r(n)
# the % sign is a modulus moderator,
# it gives the remander when you divide two numbers
# n%2 == 0 is the same as "if n/2 = 0 then..."
    if n%2 == 0:
        pixels[n] = (red, 0, 0)
# else; means everything else in this example
    else:
        pixels[n] = (0,0,red)
    print(n,red)
