#INPUT
cantidad_de_productos=input("Ingrese la cantidad de productos:")
precio_del_producto1=int(input("Ingrese el precio del producto1:"))
precio_del_producto2=int(input("Ingrese el precio del producto2:"))
precio_del_producto3=int(input("Ingrese el precio del producto3:"))

#PROCESSING
Total=(precio_del_producto1 + precio_del_producto2 + precio_del_producto3)

#verificador
gasto_alto=(Total>150000)

#OUTPUT
print("##################################")
print("#       FERRETERIA - OLANO        ")
print("##################################")
print("#")
print("#cantidad de productos     s/ :", cantidad_de_productos)
print("#precio del producto1      s/ :", precio_del_producto1)
print("#precio del producto2      s/ :", precio_del_producto2)
print("#precio del producto3      s/ :", precio_del_producto3)
print("#Total                     s/ :", Total)
print("###################################")
print("Nos a gustado su compra:",gasto_alto)
