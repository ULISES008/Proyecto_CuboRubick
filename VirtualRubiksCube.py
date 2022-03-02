
from numpy import *
#Down
w = array([["W", "W", "W"], ["W", "W", "W"], ["W", "W", "W"]])
#Front
r = array([["R", "R", "R"], ["R", "R", "R"], ["R", "R", "R"]])
#Up
y = array([["Y", "Y", "Y"], ["Y", "Y", "Y"], ["Y", "Y", "Y"]])
#Back
o = array([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]])
#Left
b = array([["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]])
#Right
g = array([["G", "G", "G"], ["G", "G", "G"], ["G", "G", "G"]])



x = str(input("\n\nMovimiento: "))

if x == "r":
    
    wx = array(w)
    rx = array(r)
    yx = array(y)
    ox = array(o)
    bx = array(b)
    gx = array(g)
    
    w[0,2]= ox[0,2]
    w[1,2]= ox[1,2]
    w[2,2]= ox[2,2]
    
    r[0,2]= wx[0,2]
    r[1,2]= wx[1,2]
    r[2,2]= wx[2,2]
    
    y[0,2]= rx[0,2]
    y[1,2]= rx[1,2]
    y[2,2]= rx[2,2]
    
    o[0,2]= yx[0,2]
    o[1,2]= yx[1,2]
    o[2,2]= yx[2,2]

    b[0,0]= bx[0,0]
    b[0,1]= bx[0,1]
    b[0,2]= bx[0,2]
    b[1,0]= bx[1,0]
    b[1,2]= bx[1,2]
    b[2,0]= bx[2,0]
    b[2,1]= bx[2,1]
    b[2,2]= bx[2,2]

    g[0,0]= gx[2,0]
    g[0,1]= gx[1,0]
    g[0,2]= gx[0,0]
    g[1,0]= gx[2,1]
    g[1,2]= gx[0,1]
    g[2,0]= gx[2,2]
    g[2,1]= gx[1,2]
    g[2,2]= gx[0,2]

    print("\n\n ")
    print(wx)
    print(rx)
    print(yx)
    print(ox)
    print(bx)
    print(gx)
    print("\n\n ")
    print(w)
    print(r)
    print(y)
    print(o)
    print(b)
    print(g)
    
else:
    print("no")
    