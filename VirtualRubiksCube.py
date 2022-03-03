
from numpy import *
###################################################################
#Down
w = array([["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]])
#Front
r = array([["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]])
#Up
y = array([["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]])
#Back
o = array([["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]])
#Left
b = array([["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]])
#Right
g = array([["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]])
"""###################################################################
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
###################################################################"""
wx = array(w)
rx = array(r)
yx = array(y)
ox = array(o)
bx = array(b)
gx = array(g)
###################################################################
print("\n\nLa cara blanca (w) es:\n", w)    
print("\n\nLa cara roja (r) es:\n", r)  
print("\n\nLa cara amarilla (y) es:\n", y) 
print("\n\nLa cara naranja (o) es:\n", o)  
print("\n\nLa cara azul (b) es:\n", b)  
print("\n\nLa cara verde (g) es:\n", g)
##############################################################################################
#Movimientos del Cubo:
def up():
    r[0,0]= gx[0,0]
    r[0,1]= gx[0,1]
    r[0,2]= gx[0,2]
    
    y[0,0]= yx[2,0]
    y[0,1]= yx[1,0]
    y[0,2]= yx[0,0]
    y[1,0]= yx[2,1]
    y[1,2]= yx[0,1]
    y[2,0]= yx[2,2]
    y[2,1]= yx[1,2]
    y[2,2]= yx[0,2]
    
    o[2,0]= bx[0,2]
    o[2,1]= bx[0,1]
    o[2,2]= bx[0,0]

    b[0,0]= rx[0,0]
    b[0,1]= rx[0,1]
    b[0,2]= rx[0,2]

    g[0,0]= ox[2,2]
    g[0,1]= ox[2,1]
    g[0,2]= ox[2,0]
#############################  
def up_prima():
    r[0,0]= bx[0,0]
    r[0,1]= bx[0,1]
    r[0,2]= bx[0,2]

    y[0,0]= yx[0,2]
    y[0,1]= yx[1,2]
    y[0,2]= yx[2,2]
    y[1,0]= yx[0,1]
    y[1,2]= yx[2,1]
    y[2,0]= yx[0,0]
    y[2,1]= yx[1,0]
    y[2,2]= yx[2,0]
    
    o[2,0]= gx[0,2]
    o[2,1]= gx[0,1]
    o[2,2]= gx[0,0]

    b[0,0]= ox[2,2]
    b[0,1]= ox[2,1]
    b[0,2]= ox[2,0]

    g[0,0]= rx[0,0]
    g[0,1]= rx[0,1]
    g[0,2]= rx[0,2]
#############################    
def down():
    w[0,0]= wx[2,0]
    w[0,1]= wx[1,0]
    w[0,2]= wx[0,0]
    w[1,0]= wx[2,1]
    w[1,2]= wx[0,1]
    w[2,0]= wx[2,2]
    w[2,1]= wx[1,2]
    w[2,2]= wx[0,2]
    
    r[2,0]= bx[2,0]
    r[2,1]= bx[2,1]
    r[2,2]= bx[2,2]
    
    o[0,0]= gx[2,2]
    o[0,1]= gx[2,1]
    o[0,2]= gx[2,0]

    b[2,0]= ox[0,2]
    b[2,1]= ox[0,1]
    b[2,2]= ox[0,0]

    g[2,0]= rx[2,0]
    g[2,1]= rx[2,1]
    g[2,2]= rx[2,2]
#############################
def down_prima():
    w[0,0]= wx[0,2]
    w[0,1]= wx[1,2]
    w[0,2]= wx[2,2]
    w[1,0]= wx[0,1]
    w[1,2]= wx[2,1]
    w[2,0]= wx[0,0]
    w[2,1]= wx[1,0]
    w[2,2]= wx[2,0]
    
    r[2,0]= gx[2,0]
    r[2,1]= gx[2,1]
    r[2,2]= gx[2,2]
    
    o[0,0]= bx[2,2]
    o[0,1]= bx[2,1]
    o[0,2]= bx[2,0]

    b[2,0]= rx[2,0]
    b[2,1]= rx[2,1]
    b[2,2]= rx[2,2]

    g[2,0]= ox[0,2]
    g[2,1]= ox[0,1]
    g[2,2]= ox[0,0]
#############################
def front():
    w[0,0]= gx[2,0]
    w[0,1]= gx[1,0]
    w[0,2]= gx[0,0]
        
    r[0,0]= rx[2,0]
    r[0,1]= rx[1,0]
    r[0,2]= rx[0,0]
    r[1,0]= rx[2,1]
    r[1,2]= rx[0,1]
    r[2,0]= rx[2,2]
    r[2,1]= rx[1,2]
    r[2,2]= rx[0,2]
    
    y[2,0]= bx[2,2]
    y[2,1]= bx[1,2]
    y[2,2]= bx[0,2]

    b[0,2]= wx[0,0]
    b[1,2]= wx[0,1]
    b[2,2]= wx[0,2]

    g[0,0]= yx[2,0]
    g[1,0]= yx[2,1]
    g[2,0]= yx[2,2]
#############################
def front_prima():
    w[0,0]= bx[0,2]
    w[0,1]= bx[1,2]
    w[0,2]= bx[2,2]
        
    r[0,0]= rx[0,2]
    r[0,1]= rx[1,2]
    r[0,2]= rx[2,2]
    r[1,0]= rx[0,1]
    r[1,2]= rx[2,1]
    r[2,0]= rx[0,0]
    r[2,1]= rx[1,0]
    r[2,2]= rx[2,0]
    
    y[2,0]= gx[0,0]
    y[2,1]= gx[1,0]
    y[2,2]= gx[2,0]

    b[0,2]= yx[2,2]
    b[1,2]= yx[2,1]
    b[2,2]= yx[2,0]

    g[0,0]= wx[0,2]
    g[1,0]= wx[0,1]
    g[2,0]= wx[0,0]
#############################
def back():
    g[2,0]= wx[0,0]
#############################
def back_prima():
    g[2,0]= wx[0,0]
#############################
def right():
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

    g[0,0]= gx[2,0]
    g[0,1]= gx[1,0]
    g[0,2]= gx[0,0]
    g[1,0]= gx[2,1]
    g[1,2]= gx[0,1]
    g[2,0]= gx[2,2]
    g[2,1]= gx[1,2]
    g[2,2]= gx[0,2]
#############################
def right_prima():
    g[2,0]= wx[0,0]
#############################
def left():
    g[2,0]= wx[0,0]
#############################
def left_prima():
    g[2,0]= wx[0,0]
##############################################################################################
#Registro de movimientos del Cubo:
movimiento = ""
while movimiento != "terminar":
    movimiento = str(input("\n\nMovimiento: "))
    #######################
    if movimiento == "u":
        up()
    #######################
    elif movimiento == "up":
        up_prima()
    #######################
    elif movimiento == "d":
        down()
    #######################
    elif movimiento == "dp":
        down_prima()
    #######################
    elif movimiento == "f":
        front()
    #######################
    elif movimiento == "fp":
        front_prima()
    #######################
    elif movimiento == "b":
        back()
    #######################
    elif movimiento == "bp":
        back_prima()
    #######################        
    elif movimiento == "r":
        right()
    #######################      
    elif movimiento == "rp":
        right_prima()
    #######################
    elif movimiento == "l":
        left()
    #######################
    elif movimiento == "lp":
        left_prima()
    #######################
    else:
      print("\n\nMovimiento no valido, si ya terminaste escribe (terminar)") 

print("\n\n Caras anteriores")
print(wx)
print(rx)
print(yx)
print(ox)
print(bx)
print(gx)
print("\n\nLa cara blanca (w) es:\n", w)    
print("\n\nLa cara roja (r) es:\n", r)  
print("\n\nLa cara amarilla (y) es:\n", y) 
print("\n\nLa cara naranja (o) es:\n", o)  
print("\n\nLa cara azul (b) es:\n", b)  
print("\n\nLa cara verde (g) es:\n", g)  