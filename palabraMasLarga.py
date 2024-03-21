palabra1=input('ingrese la palabra 1: ')
palabra2=input('ingrese la palabra 2: ')

letrasPalabra1=len(palabra1)
letrasPalabra2=len(palabra2)
diferencia=letrasPalabra2-letrasPalabra1

if letrasPalabra2==letrasPalabra1:
    print('las dos palabras tienen el mismo largo.')
elif letrasPalabra1>letrasPalabra2:
    if diferencia<0:
        diferencia=-(diferencia)
        print(f"la palabra {palabra1} tiene {diferencia} letras más que {palabra2}")
else :
    if diferencia<0:
        diferencia=-(diferencia)
        print(f"la palabra {palabra2} tiene {diferencia} letras más que {palabra1}")