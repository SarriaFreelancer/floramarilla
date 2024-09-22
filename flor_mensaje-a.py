from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0, -40)

# Dibujar hojas
for i in range(16):
    for j in range(18):
        color('#FFA216')
        #color('#FFFFFF')
        right(90)
        circle(150 - j * 6, 90)
        left(90)
        circle(150 - j * 6, 90)
        right(180)
    circle(40, 24)

# Dibujar centro de la flor
color('black')
shape('circle')
shapesize(0.5)
fillcolor('#884513')
golden_ang = 137.508
phi = golden_ang * (pi / 180)

for i in range(140):
    r = 4 * sqrt(i)
    theta = i * phi
    x = r * cos(theta)
    y = r * sin(theta)
    penup()
    goto(x, y)
    setheading(i * golden_ang)
    pendown()
    stamp()

# Definir puntos para dibujar letras
def point(x, y):
    penup()
    goto(x, y)
    pendown()
    color('black')
    fillcolor('#FFA216')
    begin_fill()
    circle(4)
    end_fill()

# Función para dibujar la letra 'T'
def draw_T(x, y):
    positions_t = [(x, y + 30), (x + 5, y + 30), (x + 12, y + 30), (x + 18, y + 30),
                   (x + 24, y + 30), (x + 12, y + 30), (x + 12, y + 24), (x + 12, y + 18),
                   (x + 12, y + 12), (x + 12, y + 6), (x + 12, y)]
    for pos in positions_t:
        point(*pos)

# Función para dibujar la letra 'U'
def draw_U(x, y):
    positions_u = [(x, y + 30), (x, y + 24), (x, y + 18), (x, y + 12), (x, y + 6),
                   (x + 3, y + 3), (x + 6, y), (x + 12, y - 1), (x + 18, y),
                   (x + 21, y + 3), (x + 24, y + 6), (x + 24, y + 12), (x + 24, y + 18),
                   (x + 24, y + 24), (x + 24, y + 30), (x + 12, y + 36), (x + 16, y + 40)]
    for pos in positions_u:
        point(*pos)

# Dibujar las letras 'TU'
draw_T(-27, -20)
draw_U(7, -28)

# Escribir el mensaje centrado
penup()
goto(0, -270)  # Ajusta la posición según sea necesario
pendown()
color("white")
write("Esta flor no creció en un jardín, pero fue creada con el corazón.", align="center", font=("Arial", 16, "italic"))  # Primera línea
penup()
goto(0, -290)  # Ajusta para el segundo párrafo
pendown()
write("¡Feliz día de las flores amarillas Valentina Crespa. ", align="center", font=("Arial", 16, "italic"))  # Segunda línea

penup()
goto(0, -310)  # Ajusta para el segundo párrafo
pendown()
write("De parte de Brayan su futuro...", align="center", font=("Arial", 16, "italic"))  # Segunda línea

# Dibujar un corazón rojo del tamaño de las letras, centrado debajo del texto
def draw_heart(x, y):
    penup()
    goto(x, y)
    pendown()
    color('red')
    begin_fill()
    left(140)
    forward(10)  # Tamaño reducido
    circle(-5, 200)  # Parte izquierda
    left(120)
    circle(-5, 200)  # Parte derecha
    forward(10)  # Vuelta al punto inicial
    end_fill()

# Ajustar posición del corazón centrado debajo del último párrafo
draw_heart(270, -180)
draw_heart(-270, 180)


hideturtle()
done()
