numero=1
numero1=1
numero2=1
numeros=[]
numeros1=[]
numeros2=[]

for i in range(2):
    numeroIngresado=int(input(f"ingrese el numero :{numero} "))
    numero=numero+1
    numeros.append(numeroIngresado)

    numerosOrdenados=sorted(numeros)
print(f"los numeros ordenados de menor a mayor serian : {numerosOrdenados}")


for i in range(3):
    numeroIngresado1=int(input(f"ingrese el numero :{numero1} "))
    numero1=numero1+1
    numeros1.append(numeroIngresado1)

    numerosOrdenados1=sorted(numeros1)
print(f"los numeros ordenados de menor a mayor serian : {numerosOrdenados1}")



for i in range(4):
    numeroIngresado2=int(input(f"ingrese el numero :{numero2} "))
    numero2=numero2+1
    numeros2.append(numeroIngresado2)

    numerosOrdenados2=sorted(numeros2)
print(f"los numeros ordenados de menor a mayor serian : {numerosOrdenados2}")