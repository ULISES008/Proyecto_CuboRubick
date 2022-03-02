
from numpy import *
###################################################################
#Down
w = array([["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]])
#Front
r = array([["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]])
#Up
y = array([["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]])
#Back
o = array([["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]])
#Left
b = array([["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]])
#Right
g = array([["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]])

###################################################################
#Asignar colores a w:
s = w.size
i=0
n=0
while i < s:
    i=i+1
    while n < 3:
        m=0
        while m < 3:
            print("\n\nColor [",n,",",m,"] de la cara blanca:")
            color = str(input())
            w[n,m]= color
            m=m+1
        n=n+1

###################################################################
#Asignar colores a r:
s = r.size
i=0
n=0
while i < s:
    i=i+1
    while n < 3:
        m=0
        while m < 3:
            print("\n\nColor [",n,",",m,"] de la cara roja:")
            color = str(input())
            r[n,m]= color
            m=m+1
        n=n+1

###################################################################
#Asignar colores a y:
s = y.size
i=0
n=0
while i < s:
    i=i+1
    while n < 3:
        m=0
        while m < 3:
            print("\n\nColor [",n,",",m,"] de la cara amarilla:")
            color = str(input())
            y[n,m]= color
            m=m+1
        n=n+1

###################################################################
#Asignar colores a o:
s = o.size
i=0
n=0
while i < s:
    i=i+1
    while n < 3:
        m=0
        while m < 3:
            print("\n\nColor [",n,",",m,"] de la cara naranja:")
            color = str(input())
            o[n,m]= color
            m=m+1
        n=n+1

###################################################################
#Asignar colores a b:
s = b.size
i=0
n=0
while i < s:
    i=i+1
    while n < 3:
        m=0
        while m < 3:
            print("\n\nColor [",n,",",m,"] de la cara azul:")
            color = str(input())
            b[n,m]= color
            m=m+1
        n=n+1

###################################################################
#Asignar colores a g:
s = g.size
i=0
n=0
while i < s:
    i=i+1
    while n < 3:
        m=0
        while m < 3:
            print("\n\nColor [",n,",",m,"] de la cara verde:")
            color = str(input())
            g[n,m]= color
            m=m+1
        n=n+1
        
###################################################################
print("\n\nLa cara blanca (w) es:")    
print(w)
print("\n\nLa cara roja (r) es:")    
print(r)
print("\n\nLa cara amarilla (y) es:")    
print(y)
print("\n\nLa cara naranja (o) es:")    
print(o)
print("\n\nLa cara azul (b) es:")    
print(b)
print("\n\nLa cara verde (g) es:")    
print(g)
###################################################################

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
    