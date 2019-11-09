#INPUT
distribuidor=input("ingrese el nombre del distribuidor:")
precio_de_los_zapatos=int(input("ingrese el precio de los zapatos:"))
precio_de_las_zapatillas=int(input("ingrese el precio de las zapatillas:"))
precio_de_los_tacones=int(input("ingrese el precio de los tacones:"))
cantidad_de_calzado_vendido=int(input("ingrese la cantidad de calzado vendido:"))

#PROCESSING
total=((precio_de_las_zapatillas + precio_de_los_tacones + precio_de_los_zapatos)*cantidad_de_calzado_vendido)

#verificador
desc=(total>=1000)

#OUTPUT
print("#########################")
print("#TIENDAS DE CALZADO - BATA")
print("#########################")
print("#nombre del distribuidor     :", distribuidor)
print("#precio de los zapatos     S/:", precio_de_los_zapatos)
print("#precio de las zapatillas  S/:", precio_de_las_zapatillas)
print("#precio de los tacones     S/:", precio_de_los_tacones)
print("#cantidad de calzado vendido :", cantidad_de_calzado_vendido)
print("#total                     S/:", total)
print("#########################")
print("Se lleva nuestro descuento por consumo:",desc)
