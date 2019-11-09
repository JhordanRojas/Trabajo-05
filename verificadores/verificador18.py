#ejercicio 18: calcular la presion hidrostatica
presion_hidrostatica, densidad_del_liquido, gravedad3, altura4=0.0, 0.0, 0.0, 0.0
#asignacion de valores
densidad_del_liquido=0.8
gravedad3=9.84
altura4=14
#calculo
presion_hidrostatica=(densidad_del_liquido*gravedad3*altura4)
#mostrar valores
print("densidad_del_liquido=", densidad_del_liquido)
print("gravedad3=", gravedad3)
print("altura4=", altura4)
print("presion_hidrostatica=", presion_hidrostatica)

#verficador 18
presion_del_mar=(presion_hidrostatica<=110.208)
print("presion del mar:", presion_del_mar)
