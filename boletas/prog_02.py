#input
base_mayor=int(input("Ingrese el valor de la base mayor:"))
base_menor=int(input("Ingrese el valor de la base menor:"))
altura=int(input("Ingrese el valor de la altura:"))

#processing
area=((base_mayor+base_menor)*altura)/2

#verificador
area_pequenia=(area<100)

#output
print("                                       ")
print("#######################################")
print("# CALCULADORA DEL AREA DE UN TRAPECIO  ")
print("#######################################")
print("# Base mayor:", base_mayor)
print("# Base menor:", base_menor)
print("# Altura    :", altura)
print("#--------------------------------------")
print("#El valor del area del trapecio es:", area)
print("##########################################")
print("El valor del area es pequeña:",area_pequenia)
