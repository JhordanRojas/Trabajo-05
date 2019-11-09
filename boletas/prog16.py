#INPUT
nombre_del_depositador=input("ingrese el nombre del depositador:")
cantidad_de_dinero_depositado=int(input("ingrese la cantidad de dinero depositado:"))
cobro_por_depositos=int(input("ingrese el cobro por deposito:"))
numero_de_personas=int(input("ingrese el numero de personas:"))

#PROCESSING
total=((cantidad_de_dinero_depositado + cobro_por_depositos)*numero_de_personas)

#verificador
dep=(total==950)

#OUTPUT
print("###############################################################")
print("#BANCO DE LA NACION")
print("###############################################################")
print("#")
print("#nombre del positador          :", nombre_del_depositador)
print("#cantidad de dinero depositado :", cantidad_de_dinero_depositado)
print("#cobro por depositos           :", cobro_por_depositos)
print("#numero de personas            :", numero_de_personas)
print("#total                         :", total)
print("################################################################")
print("Su deposito equivale a un sueldo minimo:",dep)
