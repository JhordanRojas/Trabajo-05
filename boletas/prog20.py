#INPUT
nombre_de_turista=input("ingrese el nombre del turista:")
precio_del_pasaje=int(input("ingrese el pasaje:"))
precio_del_almuerzo=int(input("ingrese el precio del almuerzo:"))
precio_de_entrada_al_museo=int(input("ingrese el precio de entrada al museo:"))

#PROCESSING
total=(precio_del_pasaje + precio_de_entrada_al_museo + precio_del_almuerzo)

#verificador
barato=(total<4000)

#OUTPUT
print("################################")
print("#AGENCIA DE VIAJES TURISTICOS - PERU")
print("################################")
print("#nombre del turista            :", nombre_de_turista)
print("#precio del pasaje             :", precio_del_pasaje)
print("#precio del almuerzo           :", precio_del_almuerzo)
print("#precio de la entrada al museo :", precio_de_entrada_al_museo)
print("#total                         :", total)
print("################################")
print("El viaje salio barato:",barato)
