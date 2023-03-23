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
import turtle

car = path('car.gif')
#tiles = list(range(32)) * 2 ##Quitamos la lista ya que creamos una distinta. 
state = {'mark': None}
hide = [True] * 64
nt = 0 #Se define la variable para el numbero de taps destapadas
p = 0  #Se defina la variable para el numero de parejas descubiertas
lista = ['œ','æ','®','†','¥','u','π','å','∫','∂','ƒ','','™','¶','§','l','∑','©','√','ß','µ','|','@','#','¢','∞','8','≠','!','LL','DD','EE']*2 #Nueva lista creada con nuevos elementos. 


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
    if mark is None or mark == spot or lista[mark] != lista[spot]:
        state['mark'] = spot
    
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global p #Variable global p
        p += 1   #Sumarle 1 a p cada que se descubra una pareja
    #number of taps...
    global nt #Utilizar variable global
    nt += 1   #Sumarle un 1 cada que se destapa la tapa
    print("Taps opened: "+ str(nt)) #Imprimir la variable en pantalla

    if p == 32:             #Condicion de que ya se destaparon todas las parejas
        print("Ganaste") #Desplegar mensaje de victoria
    

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    global p
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
            
    mark = state['mark']
    
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y+7) #Se puso x+25 y y +7 para centrar todavia mejor los elemtnos de la lista. 
        color('black')
        write(lista[mark], font=('Arial', 30, 'normal'), align = "center")#Se puso un align para poder centrar
    update()
    ontimer(draw, 100)
     
shuffle(lista)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)

onscreenclick(tap)

draw()
done()