horaActual=int(input("Ingresa la hora actual: "))
cantidadDeHoras=int(input("numero de horas que desea avanzar: "))
horaFinal=(horaActual+cantidadDeHoras)%24
print("En", cantidadDeHoras,"horas, el reloj marcará las ", horaFinal)