# Postulado de la máquina de Galton:
# Una distribución binomial se acerca a la normal: "Teorema del límite central"

import sys 

import numpy as np
import matplotlib.pyplot as plt
from random import randint

def main():

  def isNumeric(s):
          try:
              int(s)
              return True
          except ValueError:
              return False

  def distribuir_balines(años):

    for h in range((años)**2*100):                   # Distribuye el total de los
      stored = -1                                       # balines en los recipientes definidos 
      for j in range(años):                          # con la variable años.
        stored += randint(0, 1)                         # Esta función lo que hace es añadir un 1 o un 0 
      recipientes[stored] += 1                          # con una probabilidad de ½. Esto representa lo que hacen las bolas al tropezar con uno de los pivotes, 
                                                        # donde pueden ir a la derecha o a la izquierda con una probabilidad del 50%.
                                                        # Si una bola baja 10 años y va a la derecha en seis ocasiones y a la izquierda en cuatro ocasiones, el valor de la variable stored sería 6.

  def graficar(X, recipientes, gwidth):
    ax.set_ylabel('Balines')
    ax.set_title('Casilleros o Recipientes')
    plt.suptitle('Tablero de Galton')
    ax.set_facecolor('yellow')
    plt.bar(X, recipientes, width=gwidth)    # width es el ancho de las barras
    plt.show()

  print("")
  print("\033[0;33m"+"Bienvenidos al simulador de la Máquina de Galton !!"+'\033[0;m')
  print("")

  # Para poder apreciar el efecto del algoritmo se pide un rango de 4 a 20

  control = False

  while control == False :

    while True:
        años = ''
        años = input("Cuántos años deseas simular?(min 4 máx 20) ")
        #if años.isnumeric():
        s = años
        if isNumeric(s) :
            años = int(años)
            if años >= 4 and años <= 20:
                recipientes = [0]*(años)    # Primera posición de recipientes por años
                break
            else:
                print("\033[;36m"+"El nivel no puede ser menor a 4 ni mayor a 20."+'\033[0;m')
                continue
        else:
            print("\033[;36m"+"El nivel debe ser numérico."+'\033[0;m')
            continue

    distribuir_balines(años)

    print((años)**2*100, "balines usados en total")  # Se despliegan los resultados, previo a graficar
    print("\033[;35m"+"Distribución de los balines en los recipientes: "+'\033[0;m')
    print(f"\033[;36m"+str(recipientes)+'\033[0;m')
    input("\033[;32m"+"Oprima una tecla para continuar."+'\033[0;m')
    X = np.arange(-((len(recipientes)/2)-.5), (len(recipientes)/2)+.5) # Función en numpy, que devuelve valores uniformemente espaciados dentro de un intervalo dado
    fig, ax = plt.subplots()
    # Crea 2 objetos: una Figure fig (figura) que es un contenedor de todo 
    # lo que verás en el gráfico y los Axes ax (ejes) que contienen la información 
    # a graficar. En este caso los datos se graficarán de manera distinta, solo se 
    # utilizarán las etiquetas para identificar cada uno de los ejes.
    
    graficar(X, recipientes, 0.80)

    ########################################
    # Control de repeticiones

    continuar = " "

    while continuar == " " :
        continuar = input("¿Deseas ver la distribución y grafica de otros años (S/N)?")
        continuar_up = continuar.upper()

        if continuar_up == "S" :
            continuar = "S"
        elif continuar_up == "N" :
            control = True
            continuar = "N"
            break            
        else :
            print("Debe responder S para si y N para no")
            continuar = " "

    # Fin repeticiones

  print("\033[;31m"+"Fin del programa. Hasta la próxima !!"+'\033[0;m')
  print("\n")
if __name__ == "__main__":
    main()