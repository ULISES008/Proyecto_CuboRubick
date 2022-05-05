import VirtualRubiksCube
from numpy import *

#Cruz blanco + rojo:
def pz_blanco_rojo(w, r, y, o, b, g):
    if w[1,2] == "w" and g[2,1] == "r":
        print("dp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif w[2,1] == "w" and o[0,1] == "r":
        print("2d")
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
        VirtualRubiksCube.down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif w[1,0] == "w" and b[2,1] == "r":
        print("d")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif w[0,1] == "r" and r[2,1] == "w":
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
    elif w[1,2] == "r" and g[2,1] == "w":
        print("r, f")
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
    elif w[2,1] == "r" and o[0,1] == "w":
        print("b, r, dp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif w[1,0] == "r" and b[2,1] == "w":
        print("lp, fp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[1,2] == "r" and g[1,0] == "w":
        print("f")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[1,2] == "w" and g[1,0] == "r":
        print("rp, dp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[1,0] == "r" and b[1,2] == "w":
        print("fp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[1,0] == "w" and b[1,2] == "r":
        print("l, d")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif g[1,2] == "r" and o[1,2] == "w":
        print("r, dp")
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
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif g[1,2] == "w" and o[1,2] == "r":
        print("2r, f")
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
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[1,0] == "r" and o[1,0] == "w":
        print("lp, d")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[1,0] == "w" and o[1,0] == "r":
        print("2l, fp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif y[2,1] == "w" and r[0,1] == "r":
        print("2f")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif y[2,1] == "r" and r[0,1] == "w":
        print("u, l, fp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif y[1,2] == "w" and g[0,1] == "r":
        print("u, 2f")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif y[1,2] == "r" and g[0,1] == "w":
        print("rp, f")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif y[1,0] == "w" and b[0,1] == "r":
        print("up, 2f")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif y[1,0] == "r" and b[0,1] == "w":
        print("l, fp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif y[0,1] == "w" and o[2,1] == "r":
        print("2u, 2f")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif y[0,1] == "r" and o[2,1] == "w":
        print("u, rp, f")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    else:
        print("pz_blanca_rojo ya en lugar")


#Cruz blanco + verde:
def pz_blanco_verde(w, r, y, o, b, g):
    if g[2,1] == "w" and w[1,2] == "g":
        print("dp, fp, d, rp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.right_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif o[0,1] == "g" and w[2,1] == "w":
        print("f, dp, fp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif o[0,1] == "w" and w[2,1] == "g":
        print("b, r")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[2,1] == "g" and w[1,0] == "w":
        print("f, d, d, fp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[2,1] == "w" and w[1,0] == "g":
        print("f, d, fp, rp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif g[1,0] == "g" and r[1,2] == "w":
        print("rp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif g[1,0] == "w" and r[1,2] == "g":
        print("f, d, fp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif o[1,2] == "w" and g[1,2] == "g":
        print("r")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif o[1,2] == "g" and g[1,2] == "w":
        print("d, bp, dp")
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
        VirtualRubiksCube.back_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[1,0] == "g" and o[1,0] == "w":
        print("2b, r")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[1,0] == "w" and o[1,0] == "g":
        print("d, b, dp")
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
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[1,0] == "g" and b[1,2] == "w":
        print("fp, d, f")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[1,0] == "w" and b[1,2] == "g":
        print("lp, 2u, 2r")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif g[0,1] == "g" and y[1,2] == "w":
        print("2r")
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
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif g[0,1] == "w" and y[1,2] == "g":
        print("up, bp, r")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif o[2,1] == "g" and y[0,1] == "w":
        print("u, 2r")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif o[2,1] == "w" and y[0,1] == "g":
        print("bp, r")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[0,1] == "g" and y[1,0] == "w":
        print("2u, 2r")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[0,1] == "w" and y[1,0] == "g":
        print("u, bp, r")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[0,1] == "g" and y[2,1] == "w":
        print("up, 2r")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[0,1] == "w" and y[2,1] == "g":
        print("f, rp, fp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    else:
        print("pz_blanca_verde ya en lugar")


#Cruz blanco + naranja:
def pz_blanco_naranja(w, r, y, o, b, g):
    if o[0,1] == "w" and w[2,1] == "o":
        print("bp, d, lp, dp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.left_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[2,1] == "o" and w[1,0] == "w":
        print("dp, b, d, bp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.back_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[2,1] == "w" and w[1,0] == "o":
        print("l, b")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        


    elif g[1,0] == "o" and r[1,2] == "w":
        print("dp, rp, d")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif g[1,0] == "w" and r[1,2] == "o":
        print("2d, f, 2d")
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
        VirtualRubiksCube.down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif o[1,2] == "w" and g[1,2] == "o":
        print("dp, r, d")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
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
        VirtualRubiksCube.down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif o[1,2] == "o" and g[1,2] == "w":
        print("bp")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[1,0] == "o" and o[1,0] == "w":
        print("d, lp, dp")
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
        VirtualRubiksCube.left_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[1,0] == "w" and o[1,0] == "o":
        print("b")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[1,0] == "o" and b[1,2] == "w":
        print("2l, b")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[1,0] == "w" and b[1,2] == "o":
        print("d, l, dp")
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
        VirtualRubiksCube.left(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)


    elif g[0,1] == "o" and y[1,2] == "w":
        print("up, 2b")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif g[0,1] == "w" and y[1,2] == "o":
        print("r, bp, rp")
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
        VirtualRubiksCube.back_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.right_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif o[2,1] == "o" and y[0,1] == "w":
        print("2b")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif o[2,1] == "w" and y[0,1] == "o":
        print("up, lp, b")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[0,1] == "o" and y[1,0] == "w":
        print("u, 2b")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif b[0,1] == "w" and y[1,0] == "o":
        print("lp, b")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[0,1] == "o" and y[2,1] == "w":
        print("2u, 2b")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    elif r[0,1] == "w" and y[2,1] == "o":
        print("u, lp, b")
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.left_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        VirtualRubiksCube.back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
    else:
        print("pz_blanca_naranja ya en lugar")