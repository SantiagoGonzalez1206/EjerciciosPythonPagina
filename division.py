numero1=int(input('ingrese el primer numero: '))
numero2=int(input('ingrese el segundo numero: '))

division=(numero1/numero2)
resto=division%1
cociente=int(division)

if division%1==0:

    print(f"""la division es exacta. 
          el cociente es: {cociente} """)
else:
    print(f"""la division no es exacta.
          el cociente es: {cociente} 
          el resto es: {resto}""")