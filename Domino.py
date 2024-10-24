import random as r
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import time as t
import matplotlib.pyplot as plt


def montecarlo(valorA, ladoB):
    while True:
        valor = r.random()
        if((valor < 0.14 and ladoB.__contains__(0)) and valorA == 0 ):
            ladoB.remove(0)
            return 0
        elif((valor < 0.28 and ladoB.__contains__(1)) and valorA <= 1 and f'{valorA}.1' not in valor_ficha):
            ladoB.remove(1)
            return 1
        elif((valor < 0.42 and ladoB.__contains__(2)) and valorA <= 2 and f'{valorA}.2' not in valor_ficha):
            ladoB.remove(2)
            return 2
        elif((valor < 0.57 and ladoB.__contains__(3)) and valorA <= 3 and f'{valorA}.3' not in valor_ficha):
            ladoB.remove(3)
            return 3
        elif((valor < 0.71 and ladoB.__contains__(4)) and valorA <= 4 and f'{valorA}.4' not in valor_ficha):
            ladoB.remove(4)
            return 4
        elif((valor < 0.85 and ladoB.__contains__(5)) and valorA <= 5 and f'{valorA}.5' not in valor_ficha):
            ladoB.remove(5)
            return 5
        elif((valor < 1 and ladoB.__contains__(6)) and valorA <= 6 and f'{valorA}.6' not in valor_ficha):
            ladoB.remove(6)
            return 6



def main():
    victorias_p1 = 0
    victorias_p2 = 0
    victorias_p3 = 0
    victorias_p4 = 0
    
    for z in range(num):
        ladoA = [0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,5,6]
        ladoB = [0,1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6]
        global valor_ficha 
        global listaJuego
        global imagenesp1
        global imagenesp2
        global imagenesp3
        global imagenesp4
        global xjuego_A
        global xjuego_B
        global x
        global y
        listaJuego = []
        valor_ficha = []
        p1A = []
        p1B = []
        p1A = []
        p1B = []
        p2A = []
        p2B = []
        p3A = []
        p3B = []
        p4A = []
        p4B = []
        imagenesp1 = []
        imagenesp2 = []
        imagenesp3 = []
        imagenesp4 = []
        actual = 0
        x= 84
        y= 43
        xp1 = 466
        yp2 = 107
        xp3 = 466
        yp4 = 107
        #Repartir las fichas
        while((len(ladoA) == 0 and len(ladoB) == 0) == False):
            #repartir 1 ficha a los 4 jugadores 
            for j in range(4):
                valorA = 0
                valorB = 0
                while True:
                    valor = r.random()
                    if(valor < 0.14 and ladoA.__contains__(0)):
                        ladoA.remove(0)
                        valorA = 0
                        valorB = montecarlo(valorA, ladoB)
                        valor_ficha = valor_ficha + [f'{valorA}.{valorB}']
                        break
                    elif(valor < 0.28 and ladoA.__contains__(1)):
                        ladoA.remove(1)
                        valorA = 1
                        valorB = montecarlo(valorA, ladoB)
                        valor_ficha = valor_ficha + [f'{valorA}.{valorB}']
                        break
                    elif(valor < 0.42 and ladoA.__contains__(2)):
                        ladoA.remove(2)
                        valorA = 2
                        valorB = montecarlo(valorA, ladoB)
                        valor_ficha = valor_ficha + [f'{valorA}.{valorB}']
                        break
                    elif(valor < 0.57 and ladoA.__contains__(3)):
                        ladoA.remove(3)
                        valorA = 3
                        valorB = montecarlo(valorA, ladoB)
                        valor_ficha = valor_ficha + [f'{valorA}.{valorB}']
                        break
                    elif(valor < 0.71 and ladoA.__contains__(4)):
                        ladoA.remove(4)
                        valorA = 4
                        valorB = montecarlo(valorA, ladoB)
                        valor_ficha = valor_ficha + [f'{valorA}.{valorB}']
                        break
                    elif(valor < 0.85 and ladoA.__contains__(5)):
                        ladoA.remove(5)
                        valorA = 5
                        valorB = montecarlo(valorA, ladoB)
                        valor_ficha = valor_ficha + [f'{valorA}.{valorB}']
                        break
                    elif(valor < 1 and ladoA.__contains__(6)):
                        ladoA.remove(6)
                        valorA = 6
                        valorB = montecarlo(valorA, ladoB)
                        valor_ficha = valor_ficha + [f'{valorA}.{valorB}']
                        break
                if(j == 0):
                    imagenPieza =f'{valorA}.{valorB}.png'
                    p1A.append(valorA)
                    p1B.append(valorB)
                    imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                    imagenesp1 = imagenesp1 + [imagen]
                    xp1 = xp1 + x
                    tablero.create_image(xp1,570,image=imagenesp1[len(imagenesp1)-1])
                elif(j == 1):
                    imagenPieza =f'{valorA}.{valorB}.png'
                    p2A.append(valorA)
                    p2B.append(valorB)
                    imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                    imagenesp2 = imagenesp2 + [imagen]
                    yp2 = yp2 + y
                    tablero.create_image(1470,yp2,image=imagenesp2[len(imagenesp2)-1], anchor = 'e')
                elif(j == 2):
                    imagenPieza =f'{valorA}.{valorB}.png'
                    p3A.append(valorA)
                    p3B.append(valorB)
                    imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                    imagenesp3 = imagenesp3 + [imagen]
                    xp3 = xp3 + x
                    tablero.create_image(xp3,5,image=imagenesp3[len(imagenesp3)-1], anchor='n')
                elif(j == 3):
                    imagenPieza =f'{valorA}.{valorB}.png'
                    p4A.append(valorA)
                    p4B.append(valorB)
                    imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                    imagenesp4 = imagenesp4 + [imagen]
                    yp4 = yp4 + y
                    tablero.create_image(30,yp4,image=imagenesp4[len(imagenesp4)-1], anchor='w')
            ventana.update() 
            t.sleep(0.1)
        
        #Primer movimiento
        for i in range(len(p1A)):
            if( p1A[i] == 6 and p1B[i] == 6):
                imagenPieza = f'{p1A[i]}.{p1B[i]}.png'
                imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                listaJuego = listaJuego + [imagen]
                yjuego = 300
                tablero.create_image(1400,yjuego,image=listaJuego[len(listaJuego)-1])
                del imagenesp1[i]
                del p1A[i]
                del p1B[i]
                actual = 1
                ventana.update()
                t.sleep(0.1)
                break
            if( p2A[i] == 6 and p2B[i] == 6):
                imagenPieza = f'{p2A[i]}.{p2B[i]}.png'
                imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                listaJuego = listaJuego + [imagen]
                yjuego = 300
                tablero.create_image(1400,yjuego,image=listaJuego[len(listaJuego)-1])
                del imagenesp2[i]
                del p2A[i]
                del p2B[i]
                ventana.update()
                t.sleep(0.1)
                actual = 2
                break
            if( p3A[i] == 6 and p3B[i] == 6):
                imagenPieza = f'{p3A[i]}.{p3B[i]}.png'
                imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                listaJuego = listaJuego + [imagen]
                yjuego = 300
                tablero.create_image(1400,yjuego,image=listaJuego[len(listaJuego)-1])
                del imagenesp3[i]
                del p3A[i]
                del p3B[i]
                ventana.update()
                t.sleep(0.1)
                actual = 3
                break
            if( p4A[i] == 6 and p4B[i] == 6):
                imagenPieza = f'{p4A[i]}.{p4B[i]}.png'
                imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                listaJuego = listaJuego + [imagen]
                yjuego = 300
                tablero.create_image(1500,yjuego,image=listaJuego[len(listaJuego)-1])
                del imagenesp4[i]
                del p4A[i]
                del p4B[i]
                ventana.update()
                t.sleep(0.1)
                actual = 4
                break
        #demas movimientos
        valorj_A = 6
        valorj_B = 6
        xjuego_A = 1500
        xjuego_B = 1500   
        aux = 0     
        while((len(imagenesp1) == 0  or len(imagenesp2) == 0 or len(imagenesp3) == 0 or len(imagenesp4) == 0) == False):
            if(aux > 100):
                if((len(imagenesp1) < len(imagenesp2) and len(imagenesp1) < len(imagenesp3) and len(imagenesp1) < len(imagenesp4)) == True):
                    imagenesp1.clear()
                elif((len(imagenesp2) < len(imagenesp1) and len(imagenesp2) < len(imagenesp3) and len(imagenesp2) < len(imagenesp4)) == True):
                    imagenesp2.clear()
                elif((len(imagenesp3) < len(imagenesp2) and len(imagenesp3) < len(imagenesp1) and len(imagenesp3) < len(imagenesp4)) == True):
                    imagenesp3.clear()
                elif((len(imagenesp4) < len(imagenesp2) and len(imagenesp4) < len(imagenesp3) and len(imagenesp4) < len(imagenesp1)) == True):
                    imagenesp4.clear()
                else: 
                    imagenesp1.clear()
            if(actual == 1):
                for l in range(len(p2A)):
                    if( p2B[l] == valorj_A):
                        imagenPieza = f'{p2A[l]}.{p2B[l]}.png'
                        imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                        listaJuego = listaJuego + [imagen]
                        xjuego_A = xjuego_A - x
                        tablero.create_image(xjuego_A,300,image=listaJuego[len(listaJuego)-1])
                        valorj_A = p2A[l]
                        del imagenesp2[l]
                        del p2A[l]
                        del p2B[l]
                        ventana.update()
                        t.sleep(0.01)
                        actual = 2
                        break
                    elif(p2A[l] == valorj_A):
                        imagenPieza = f'{p2A[l]}.{p2B[l]}.png'
                        imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                        listaJuego = listaJuego + [imagen]
                        xjuego_A = xjuego_A - x
                        tablero.create_image(xjuego_A,300,image=listaJuego[len(listaJuego)-1])
                        valorj_A = p2B[l]
                        del imagenesp2[l]
                        del p2A[l]
                        del p2B[l]
                        ventana.update()
                        t.sleep(0.01)
                        actual = 2
                        break
                actual = 2
            elif(actual == 2):
                for l in range(len(p3A)):
                    if( p3B[l] == valorj_A):
                        imagenPieza = f'{p3A[l]}.{p3B[l]}.png'
                        imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                        listaJuego = listaJuego + [imagen]
                        xjuego_A = xjuego_A - x
                        tablero.create_image(xjuego_A,300,image=listaJuego[len(listaJuego)-1])
                        valorj_A = p3A[l]
                        del imagenesp3[l]
                        del p3A[l]
                        del p3B[l]
                        ventana.update()
                        t.sleep(0.01)
                        actual = 3
                        break
                    elif(p3A[l] == valorj_A):
                        imagenPieza = f'{p3A[l]}.{p3B[l]}.png'
                        imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                        listaJuego = listaJuego + [imagen]
                        xjuego_A = xjuego_A - x
                        tablero.create_image(xjuego_A,300,image=listaJuego[len(listaJuego)-1])
                        valorj_A = p3B[l]
                        del imagenesp3[l]
                        del p3A[l]
                        del p3B[l]
                        ventana.update()
                        t.sleep(0.01)
                        actual = 3
                        break
                actual = 3
            elif(actual == 3):
                for l in range(len(p4A)):
                    if( p4B[l] == valorj_A):
                        imagenPieza = f'{p4A[l]}.{p4B[l]}.png'
                        imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                        listaJuego = listaJuego + [imagen]
                        xjuego_A = xjuego_A - x
                        tablero.create_image(xjuego_A,300,image=listaJuego[len(listaJuego)-1])
                        valorj_A = p4A[l]
                        del imagenesp4[l]
                        del p4A[l]
                        del p4B[l]
                        ventana.update()
                        t.sleep(0.01)
                        actual = 4
                        break
                    elif(p4A[l] == valorj_A):
                        imagenPieza = f'{p4A[l]}.{p4B[l]}.png'
                        imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                        listaJuego = listaJuego + [imagen]
                        xjuego_A = xjuego_A - x
                        tablero.create_image(xjuego_A,300,image=listaJuego[len(listaJuego)-1])
                        valorj_A = p4B[l]
                        del imagenesp4[l]
                        del p4A[l]
                        del p4B[l]
                        ventana.update()
                        t.sleep(0.01)
                        actual = 4   
                        break
                actual = 4
            elif(actual == 4):
                for l in range(len(p1A)):
                    if( p1B[l] == valorj_A):
                        imagenPieza = f'{p1A[l]}.{p1B[l]}.png'
                        imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                        listaJuego = listaJuego + [imagen]
                        xjuego_A = xjuego_A - x
                        tablero.create_image(xjuego_A,300,image=listaJuego[len(listaJuego)-1])
                        valorj_A = p1A[l]
                        del imagenesp1[l]
                        del p1A[l]
                        del p1B[l]
                        ventana.update()
                        t.sleep(0.01)
                        actual = 1
                        break
                    elif(p1A[l] == valorj_A):
                        imagenPieza = f'{p1A[l]}.{p1B[l]}.png'
                        imagen = ImageTk.PhotoImage(Image.open(imagenPieza))
                        listaJuego = listaJuego + [imagen]
                        xjuego_A = xjuego_A - x
                        tablero.create_image(xjuego_A,300,image=listaJuego[len(listaJuego)-1])
                        valorj_A = p1B[l]
                        del imagenesp1[l]
                        del p1A[l]
                        del p1B[l]
                        ventana.update()
                        t.sleep(0.01)
                        actual = 1
                        break
                actual = 1
            aux += 1
        if(len(imagenesp1) == 0):
            victorias_p1 += 1
        elif(len(imagenesp2) == 0):
            victorias_p2 += 1
        elif(len(imagenesp3) == 0):
            victorias_p3 += 1
        else:
            victorias_p4 += 1
    victorias = [victorias_p1, victorias_p2, victorias_p3, victorias_p4]
    porcentaje_victoriasp1 = int((victorias_p1 / num)*100)
    porcentaje_victoriasp2 = int((victorias_p2 / num)*100)
    porcentaje_victoriasp3 = int((victorias_p3 / num)*100)
    porcentaje_victoriasp4 = int((victorias_p4 / num)*100)
    print(f'Porcentaje de victorias del jugador 1 {porcentaje_victoriasp1}')
    print(f'Porcentaje de victorias del jugador 2 {porcentaje_victoriasp2}')
    print(f'Porcentaje de victorias del jugador 3 {porcentaje_victoriasp3}')
    print(f'Porcentaje de victorias del jugador 4 {porcentaje_victoriasp4}')
    plt.pie(victorias, labels=['jugador 1', 'jugador 2', 'jugador 3' , 'jugador 4'])
    plt.show()

num = int(input("Cuantas veces quiere hacer la simulación: "))
ventana = tk.Tk()
ventana.title("DOMINO")
ventana.geometry("1500x680")
boton = tk.Button(ventana, text= "Empzar", command=main)
tablero = tk.Canvas(ventana, bg="green",width='1500', height="600")
tablero.pack()
boton.pack()
boton.place()
ventana.mainloop()
