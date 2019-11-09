#INPUT
nombre_del_cliente=input("ingrese el nombre del cliente:")
precio_de_cerveza=int(input("ingrese el precio de cerveza:"))
precio_de_plato_de_pato=int(input("ingrese el precio del plato de pato:"))
precio_del_postre=int(input("ingrese  el precio del postre:"))

#PROCESSING
total=(precio_de_plato_de_pato + precio_de_cerveza + precio_del_postre)

#verificador
comio_bien=(total>=500)

#OUTPUT
print("##################################")
print("#       RESTAURANTE DOÑA ROSA    #")
print("##################################")
print("#")
print("#nombre del cliente         :", nombre_del_cliente)
print("#precio de la cerveza     S/:", precio_de_cerveza)
print("#precio del plato de pato s/:", precio_del_postre)
print("#precio del postre        S/:", precio_del_postre)
print("#total                    s/:", total)
print("##################################")
print("Usted comio bien taipa:",comio_bien)
