# python-tf-mod3
Máquina de Galton

La Máquina o Tablero de Galton, es un dispositivo inventado por Francis Galton para demostrar el teorema del límite central, en particular que, con una muestra lo suficientemente grande, la distribución binomial se aproxima a la distribución normal. Wikipedia
Una distribución binomial se acerca a la normal: "Teorema del límite central"
 

Las características del programa:
•	En el presente programa simulamos una máquina de Galton desde 1,600 hasta 40,000 canicas o balines.
•	Se tiene hasta 20 niveles de obstáculos decidiendo si va a caer a un lado o al otro desde 4 hasta 20 veces.
•	El resultado final será un histograma que represente la cantidad de canicas en cada contenedor, se asignó nombre a los ejes y un título al gráfico. 

Se emplearán las siguientes funciones:

o	La primera función isNumeric(), valida que se introduzcan datos numéricos.
o	La segunda función distribuir_balines(), es para distribuir el total de los
    balines o canicas en los recipientes definidos con la variable años. 
o	La función randint() añade un 1 o un 0, con una probabilidad de 0.5. Esto 
    representa lo que hacen las canicas o balines al tropezar con uno de los pivotes, donde pueden ir a la derecha o a la izquierda con una probabilidad del 50%. Si una bola baja 10 años y va a la derecha en seis ocasiones y a la izquierda en cuatro ocasiones, el valor de la variable stored sería 6.
o	La tercera función graficar(), es para la graficar el histograma. 

Se agregaron los siguientes módulos o funciones:

o	import sys 
	Este módulo provee acceso a algunas variables usadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete. Siempre está disponible.

o	import numpy as np
	Es una biblioteca para Python que da soporte para crear vectores y matrices grandes multidimensionales, junto con una gran colección de funciones matemáticas de alto nivel, para operar con ellas.
o	import matplotlib.pyplot as plt
	Matplotlib es una librería de Python especializada en la creación de gráficos en dos dimensiones. Permite crear y personalizar los tipos de gráficos más comunes, entre ellos: Diagramas de barras.
o	from random import randint
	La biblioteca random contiene una serie de funciones relacionadas con los valores aleatorios. La función randint(a, b) genera un número entero entre a y b, ambos incluidos. a debe ser inferior o igual a b.
