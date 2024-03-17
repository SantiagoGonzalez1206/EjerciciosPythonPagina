nota1=float(input("ingrese la nota del certamen 1: "))
nota2=float(input("ingrese la nota del certamen 2: "))
lab=float(input("ingrese la nota del laboratorio: "))
promedioNotas=(nota1+nota2+lab)/3
notaFaltante=(60-(promedioNotas*0.7))/3

print("La nota necesaria es la siguiente: ",round(notaFaltante,2))