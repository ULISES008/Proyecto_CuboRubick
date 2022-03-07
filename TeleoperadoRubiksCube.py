
import VirtualRubiksCube
from numpy import *

###################################################################
#Down
white = array([["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]])
#Front
red = array([["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]])
#Up
yellow = array([["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]])
#Back
orange = array([["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]])
#Left
blue = array([["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]])
#Right
green = array([["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]])
###################################################################
VirtualRubiksCube.registro(white, "blanco")
VirtualRubiksCube.registro(red, "rojo")
VirtualRubiksCube.registro(yellow, "amarillo")
VirtualRubiksCube.registro(orange, "naranja")
VirtualRubiksCube.registro(blue, "azul")
VirtualRubiksCube.registro(green, "verde")
##############################################################################################
#Registro de movimientos del Cubo:
movimiento = ""
while movimiento != "terminar":
    movimiento = str(input("\n\nMovimiento: "))
    whitex = array(white)
    redx = array(red)
    yellowx = array(yellow)
    orangex = array(orange)
    bluex = array(blue)
    greenx = array(green)
    #######################
    if movimiento == "u":
        VirtualRubiksCube.up(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################
    elif movimiento == "up":
        VirtualRubiksCube.up_prima(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################
    elif movimiento == "d":
        VirtualRubiksCube.down(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################
    elif movimiento == "dp":
        VirtualRubiksCube.down_prima(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################
    elif movimiento == "f":
        VirtualRubiksCube.front(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################
    elif movimiento == "fp":
        VirtualRubiksCube.front_prima(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################
    elif movimiento == "b":
        VirtualRubiksCube.back(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################
    elif movimiento == "bp":
        VirtualRubiksCube.back_prima(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################        
    elif movimiento == "r":
        VirtualRubiksCube.right(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################      
    elif movimiento == "rp":
        VirtualRubiksCube.right_prima(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################
    elif movimiento == "l":
        VirtualRubiksCube.left(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################
    elif movimiento == "lp":
        VirtualRubiksCube.left_prima(white, red, yellow, orange, blue, green, whitex, redx, yellowx, orangex, bluex, greenx)
    #######################
    else:
      print("\n\nMovimiento no valido, si ya terminaste escribe (terminar)") 
print("\n\n Caras anteriores son:\n{}\n{}\n{}\n{}\n{}\n{}".format(whitex, redx, yellowx, orangex, bluex, greenx))
print("\n\nLa cara blanca (w) es:\n", white)    
print("\n\nLa cara roja (r) es:\n", red)  
print("\n\nLa cara amarilla (y) es:\n", yellow) 
print("\n\nLa cara naranja (o) es:\n", orange)  
print("\n\nLa cara azul (b) es:\n", blue)  
print("\n\nLa cara verde (g) es:\n", green) 