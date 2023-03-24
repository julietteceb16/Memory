"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
"""Variable para el número de taps"""
tp = 0 
"""Variable para el número de parejas descubiertas"""
pa = 0 
"""Lista de las figuras del memorama"""
tiles = ['🐶','🐱','🐭','🐹','🐰','🐻','🧸','🐼','🐘','🐨','🐯',
         '🦁','🐮','🐷','🐸','🐵','🦍','🦧','🐔','🐧','🐦','🐺',
         '🦝','🦓','🦫','🐛','🐙','🐢','🐊','🐁','🦨','🦖'] * 2

state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y,):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        """Variable global pa"""
        global pa 
        """Sumar 1 a pa cada que se descubra una pareja"""
        pa += 1   
    """Variable global tp"""
    global tp 
    """"Se suma 1 cada que se destapa una tapa"""
    tp += 1   
    """Se imprime la variable en pantalla"""
    print("Taps opened: "+ str(tp)) 
    """Condición para saber si ya se destaparon todas las parejas posibles"""
    if pa == 32:             
        print("YOU WIN!!!") 


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
         """Se cambia la alineación de las figuras"""
        write(tiles[mark], align='left', font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
