estatura = float(input('ingrese su estatura en metros '))
edad = int(input('ingrese su edad: '))
peso = float(input('ingrese su peso en kg: '))

IMC = peso / (estatura**2)
round(IMC, 2)

if edad<45:
    if IMC < 22:
        print(f"su riesgo es ", round(IMC,2) ," Su riesgo es bajo.")
    elif IMC>=22:
        print(f"su riesgo es ", round(IMC,2) ," Su riesgo es medio")
elif edad>=45:
    if IMC < 22:
        print(f"su riesgo es ", round(IMC,2) ," Su riesgo es medio.")
    elif IMC>=22:
        print(f"su riesgo es ", round(IMC,2) ," Su riesgo es alto")