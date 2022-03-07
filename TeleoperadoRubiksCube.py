import VirtualRubiksCube
from numpy import *

###################################################################r
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
VirtualRubiksCube.registro_movimientos(white, red, yellow, orange, blue, green)