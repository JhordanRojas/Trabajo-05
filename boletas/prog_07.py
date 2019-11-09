#input
longitud=float(input("Ingrese la longitud inicial de la barra en metros:"))
coef=float(input("Ingrese el valor del coeficiente de dilatacion lineal:"))
variacion_temp=float(input("Ingrese el valor de la variacion de temperatura(Cº):"))

#processing
dilatacion_lineal=longitud*coef*variacion_temp
longitud_final=longitud+dilatacion_lineal

#verificador
mucha_dilatacion=(dilatacion_lineal>10)

#output
print("                                                          ")
print("##########################################################")
print("#           CALCULADORA DE DILATACION LINEAL             #")
print("##########################################################")
print("# El valor de la longitud inicial de la varilla es:",longitud,"m")
print("# El valor de la variacion de la temperatura es:",variacion_temp,"Cº")
print("# El valor del coeficiente de dilatacion es:",coef)
print("#----------------------------------------------------------")
print("# La dilatacion de la varilla es:",dilatacion_lineal,"m")
print("# La longitud final de la varilla es:",longitud_final,"m")
print("##########################################################")
print("La dilatacion es muy alta:",mucha_dilatacion)
