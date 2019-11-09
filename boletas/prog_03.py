#input
velocidad_inicial=float(input("Ingrese el valor de la velocidad inicial:"))
gravedad=float(input("Ingrese el valor de la gravedad:"))
import math
y=float(input("ingrese el angulo en grados:"))
x=math.radians(y)

#processing
tiempo_vuelo=(2*velocidad_inicial*math.sin(x))/gravedad

#verificador
vuelo_corto=(tiempo_vuelo<5)

#output
print("                                                   ")
print("###################################################")
print("# CALCULADORA DE TIEMPO DE VUELO DE UN PROYECTIL   ")
print("###################################################")
print("#El valor de la velocidad inicial: ",velocidad_inicial,"m/s")
print("#El valor de la gravedad es: ",gravedad,"m/sº2")
print("#El valor del seno del angulo",y,"es:",math.sin(x))
print("---------------------------------------------------")
print("#El tiempo de vuelo del proyectil es:",tiempo_vuelo,"s")
print("###################################################")
print("El tiempo de vuelo es corto:",vuelo_corto)
print("                                                   ")

