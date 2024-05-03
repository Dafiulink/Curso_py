print("BIENVENIDOS A MI APLICACIÓN CALCULATOR")
print("PARA SALIR ESCRIBE SALIR")
Titulo = "Las operacion para usar son la suma, resta, multiplicación y divición"
print(Titulo.upper())
resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese Número: ")
        if resultado.lower() == "Salir":
            break
        resultado = int(resultado)

    op = input("Ingresa Operación: ")
    if op.lower() == "Salir":
        break

    n2 = input("Ingresa El Siguiente Número: ")
    if n2.lower() == "Salir":
        break

    n2 = int(n2)

    if op.lower() == "Suma":
        resultado += n2

    elif op.lower() == "resta":
        resultado -= n2

    elif op.lower() == "multiplicación":
        resultado += n2
    elif op.lower() == "divición":
        resultado /= n2
    else:
        print("Operación No Valida ")
        break
    print(f"El Resultado Es {resultado}")
