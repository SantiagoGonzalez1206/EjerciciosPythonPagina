operando1=int(input("Ingrese el dato 1: "))
operando2=int(input("Ingrese el dato 2: "))
operacion=int(input(f"""
                    
                1. Suma
                2. Resta
                3. Multiplicacion
                4. Division
                5. Potenciacion
                
                Ingrese el numero de la operación que desea realizar: """))

if operacion == 1:
    resultado = operando1+operando2
    print(f"{operando1} + {operando2} = {resultado}")
    
elif operacion == 2:
    resultado = operando1-operando2
    print(f"{operando1} - {operando2} = {resultado}")
    
elif operacion == 3:
    resultado = operando1*operando2
    print(f"{operando1} * {operando2} = {resultado}")
    
elif operacion == 4:
    resultado = round((operando1/operando2), 2)
    print(f"{operando1} / {operando2} = {resultado}")
    
elif operacion == 5:
    resultado = operando1**operando2
    print(f"{operando1} ** {operando2} = {resultado}")

else:
    print("El dato no es valido")