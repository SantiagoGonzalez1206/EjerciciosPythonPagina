from math import sqrt
c1=int(input("Escriba el primer cateto: "))
c2=int(input("Escriba el segundo cateto: "))
hipotenusa = round(sqrt(c1**2 + c2**2), 2)
print("la hipotenusa es ", hipotenusa)

