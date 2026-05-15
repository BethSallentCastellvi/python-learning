print("Bienvenido a tu calculadora")
print("Operaciones disponibles: +, -, *, /")

continuar = "si"
while continuar == "si":
    print()
    operacion = input("Elige una operación ")
    num1 = float(input("Escribe el primer número "))
    num2 = float(input("Escribe el segundo número "))
    print()

    if operacion == "+":
        print(f"{num1} + {num2} = {num1+num2}")
    elif operacion == "-":
        print(f"{num1} - {num2} = {num1-num2}")
    elif operacion == "*":
        print(f"{num1} * {num2} = {num1*num2}")
    elif operacion == "/" and num2 == 0:
        print("No se puede dividir entre 0")
    elif operacion == "/":
        print(f"{num1} / {num2} = {num1/num2}")
    else:
        print("Operación no válida. Solo disponemos de: +, -, *, /")

    print()
    continuar = input("¿Quieres hacer otro cálculo? si/no ").lower()
    print()

print("Hasta luego.")

