
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
    rx = array(o)
    yx = array(y)
    ox = array(r)
    
    w[0,0]= rx[0,0]
    w[1,0]= rx[1,0]
    w[2,0]= rx[2,0]
    
    r[0,0]= yx[0,0]
    r[1,0]= yx[1,0]
    r[2,0]= yx[2,0]
    
    y[0,0]= ox[0,0]
    y[1,0]= ox[1,0]
    y[2,0]= ox[2,0]
    
    o[0,0]= wx[0,0]
    o[1,0]= wx[1,0]
    o[2,0]= wx[2,0]
    
else:
    print("no")
    
    
    print("\n\n ")
    print(wx)
    print(rx)
    print(yx)
    print(bx)
    print("\n\n ")
    print(w)
    print(r)
    print(y)
    print(b)
