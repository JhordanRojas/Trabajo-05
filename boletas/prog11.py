#INPUT
comprador=input("ingrese el nombre del comprador:")
cantidad=int(input("ingrese el numero de productos:"))
pp=float(input("ingrese el precio de cada producto:"))

#PROCESSING
total=(cantidad * pp)

#verificador
gasto_alto=(total>12000)

#OUTPUT
print("#######################################")
print("#            TIENDA - LINARES         #")
print("#######################################")
print("#")
print("# Comprador               :     ", comprador)
print("# cantidad de productos   :     ", cantidad)
print("# Precio de cada producto : s/  ", pp)
print("# Total                   : s/  ", total)
print("#######################################")
print("Ud. gasto mucho dinero:",gasto_alto)
