import VirtualRubiksCube
from numpy import *

#Cruz blanco + rojo:
def pz_blanco_rojo(w, r, y, o, b, g):
    if w[0,1] == "w" and r[2,1] == "r":
        print("d, r, f")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        print("\n\nLa cara blanca (w) es:\n", w)    
        print("\n\nLa cara roja (r) es:\n", r)
