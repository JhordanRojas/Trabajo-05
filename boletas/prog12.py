#INPUT
nombre=input("Ingrese el nombre de usuario:")
precio=float(input("ingrese el precio del celular:"))
precio_de_envio=int(input("Ingrese el precio de envio:"))
IGV=float(input("ingrese el IGV:"))

#PORCESSING
Total=(precio + precio_de_envio + IGV)

#verifacdor
gama_alta=(Total>5000)

#OUTPUT
print("#############################")
print("# Distribuidor de celulares")
print("#############################")
print("#")
print("#Nombre            :", nombre)
print("#Precio          s/:", precio)
print("#Precio de envio s/:", precio_de_envio)
print("#IGV             s/:", IGV)
print("#Total             :", Total)
print("#############################")
print("Te compraste un gama alta:",gama_alta)
