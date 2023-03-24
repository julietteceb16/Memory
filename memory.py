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
"""Lista de las figuras del memorama"""
tp = 0 #Variable para el número de taps
pa = 0 #Variable para el número de parejas descuebiertas 
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
        global pa #Variable global pa
        pa += 1   #Le suma 1 a pa cada que se descubra una pareja
    #number of taps...
    global tp #Utilizar variable global
    tp += 1   #Se suma 1 cada que se destapa la tapa
    print("Taps opened: "+ str(tp)) #Se imprime la variable en pantalla

    if pa == 32:             #Esta es la condicion de que ya se destaparon todas las parejas posibles
        print("YOU WIN!!!") #Mensaje de victoria


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
        write(tiles[mark], font=('Arial', 30, 'normal'))

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