#input
velocidad_inicial=int(input("Ingrese el valor de la velocidad inicial:"))
aceleracion=int(input("Ingrese el valor de la aceleracion:"))
tiempo=int(input("Ingrese el valor del tiempo:"))

#processing
velocidad_final=velocidad_inicial+(aceleracion*tiempo)

#verificador
alta_velocidad=(velocidad_final>200)

#output
print("                                            ")
print("############################################")
print("# CALCULADORA DE VELOCIDAD FINAL DE UN MOVIL")
print("############################################")
print("#Velocidad inicial    :",velocidad_inicial)
print("#Aceleracion          :",aceleracion)
print("#Tiempo               :",tiempo)
print("--------------------------------------------")
print("#Velocidad final del auto :  ",velocidad_final,"km/h")
print("############################################")
print("El coche va a alta velocidad:",alta_velocidad)
