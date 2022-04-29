from numpy import *
#Registro colores del Cubo:
def registro(arregloCara, colorCara):
    size = arregloCara.size
    i=0
    fila=0
    while i < size:
        i=i+1
        while fila < 3:
            columna=0
            while columna < 3:
                color = str(input("Color [{},{}] de la cara {}:".format(fila+1, columna+1, colorCara)))
                arregloCara[fila,columna]= color
                columna=columna+1
            fila=fila+1
    print("\nLa cara {} es:\n{}\n".format(colorCara, arregloCara))
#Movimientos del Cubo:
def up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
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
def up_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
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
def down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
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
def down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
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
def front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
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
def front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
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
def back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
    w[2,0]= bx[0,0]
    w[2,1]= bx[1,0]
    w[2,2]= bx[2,0]
        
    y[0,0]= gx[0,2]
    y[0,1]= gx[1,2]
    y[0,2]= gx[2,2]

    o[0,0]= ox[2,0]
    o[0,1]= ox[1,0]
    o[0,2]= ox[0,0]
    o[1,0]= ox[2,1]
    o[1,2]= ox[0,1]
    o[2,0]= ox[2,2]
    o[2,1]= ox[1,2]
    o[2,2]= ox[0,2]

    b[0,0]= yx[0,2]
    b[1,0]= yx[0,1]
    b[2,0]= yx[0,0]

    g[0,2]= wx[2,2]
    g[1,2]= wx[2,1]
    g[2,2]= wx[2,0]
#############################
def back_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
    w[2,0]= gx[2,2]
    w[2,1]= gx[1,2]
    w[2,2]= gx[0,2]

    y[0,0]= bx[2,0]
    y[0,1]= bx[1,0]
    y[0,2]= bx[0,0]
        
    o[0,0]= ox[0,2]
    o[0,1]= ox[1,2]
    o[0,2]= ox[2,2]
    o[1,0]= ox[0,1]
    o[1,2]= ox[2,1]
    o[2,0]= ox[0,0]
    o[2,1]= ox[1,0]
    o[2,2]= ox[2,0]

    b[0,0]= wx[2,0]
    b[1,0]= wx[2,1]
    b[2,0]= wx[2,2]

    g[0,2]= yx[0,0]
    g[1,2]= yx[0,1]
    g[2,2]= yx[0,2]
#############################
def right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
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
def right_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
    w[0,2]= rx[0,2]
    w[1,2]= rx[1,2]
    w[2,2]= rx[2,2]
    
    r[0,2]= yx[0,2]
    r[1,2]= yx[1,2]
    r[2,2]= yx[2,2]
    
    y[0,2]= ox[0,2]
    y[1,2]= ox[1,2]
    y[2,2]= ox[2,2]
    
    o[0,2]= wx[0,2]
    o[1,2]= wx[1,2]
    o[2,2]= wx[2,2]

    g[0,0]= gx[0,2]
    g[0,1]= gx[1,2]
    g[0,2]= gx[2,2]
    g[1,0]= gx[0,1]
    g[1,2]= gx[2,1]
    g[2,0]= gx[0,0]
    g[2,1]= gx[1,0]
    g[2,2]= gx[2,0]
#############################
def left(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
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

    b[0,0]= bx[2,0]
    b[0,1]= bx[1,0]
    b[0,2]= bx[0,0]
    b[1,0]= bx[2,1]
    b[1,2]= bx[0,1]
    b[2,0]= bx[2,2]
    b[2,1]= bx[1,2]
    b[2,2]= bx[0,2]
#############################
def left_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx):
    w[0,0]= ox[0,0]
    w[1,0]= ox[1,0]
    w[2,0]= ox[2,0]
    
    r[0,0]= wx[0,0]
    r[1,0]= wx[1,0]
    r[2,0]= wx[2,0]
    
    y[0,0]= rx[0,0]
    y[1,0]= rx[1,0]
    y[2,0]= rx[2,0]
    
    o[0,0]= yx[0,0]
    o[1,0]= yx[1,0]
    o[2,0]= yx[2,0]

    b[0,0]= bx[0,2]
    b[0,1]= bx[1,2]
    b[0,2]= bx[2,2]
    b[1,0]= bx[0,1]
    b[1,2]= bx[2,1]
    b[2,0]= bx[0,0]
    b[2,1]= bx[1,0]
    b[2,2]= bx[2,0]
#Registro de movimientos del Cubo:
def registro_movimientos(w, r, y, o, b, g):
    movimiento = ""
    while movimiento != "terminar":
        movimiento = str(input("\n\nMovimiento: "))
        wx = array(w)
        rx = array(r)
        yx = array(y)
        ox = array(o)
        bx = array(b)
        gx = array(g)
        #######################
        if movimiento == "u":
            up(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
            #######################
        elif movimiento == "up":
            up_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        #######################
        elif movimiento == "d":
            down(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        #######################
        elif movimiento == "dp":
            down_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        #######################
        elif movimiento == "f":
            front(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        #######################
        elif movimiento == "fp":
            front_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        #######################
        elif movimiento == "b":
            back(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        #######################
        elif movimiento == "bp":
            back_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        #######################        
        elif movimiento == "r":
            right(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        #######################      
        elif movimiento == "rp":
            right_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        #######################
        elif movimiento == "l":
            left(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
        #######################
        elif movimiento == "lp":
            left_prima(w, r, y, o, b, g, wx, rx, yx, ox, bx, gx)
            #######################
        else:
            print("\n\nMovimiento no valido, si ya terminaste escribe (terminar)") 
    print("\n\n Caras anteriores son:\n{}\n{}\n{}\n{}\n{}\n{}".format(wx, rx, yx, ox, bx, gx))
    print("\n\nLa cara blanca (w) es:\n", w)    
    print("\n\nLa cara roja (r) es:\n", r)  
    print("\n\nLa cara amarilla (y) es:\n", y) 
    print("\n\nLa cara naranja (o) es:\n", o)
    print("\n\nLa cara azul (b) es:\n", b)  
    print("\n\nLa cara verde (g) es:\n", g)