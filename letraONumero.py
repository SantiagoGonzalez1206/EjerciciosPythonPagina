dato=input('ingrese el dato: ')

if dato.isalpha():

    if dato.isupper():
        print(f"el dato {dato} es una letra mayuscula")
    else:
        print(f"el dato {dato} es una letra minuscula")

elif dato.isdigit():
    print(f"el dato ingresado {dato} es un numero.")
else:
    print('No es letra ni numero')