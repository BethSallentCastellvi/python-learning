# Práctica 1: Aprender a usar el print, poner nombre, ciudad, operaciones matemáticas y espacios entre líneas.
print("")
print("Hola, Mundo")
print("")

# Datos de usuario
print("Me llamo Beth")
print("Vivo en Barcelona")
print("")

# Operaciones matemáticas
print(2 + 2)
print(7 * 6)
print("")

print("Ejercicio 1 de la práctica 1")
print("")

# Práctica 2: Variables, tipos de variables y usar f-string

# Variables
nombre = "Beth"
edad = 16
ciudad = "BCN"
altura = 1.64
estudia_python = True

# Buscar tipos de variables
print(type(nombre))
print(type(edad))
print(type(ciudad))
print(type(altura))
print(type(estudia_python))

# Frase con f-string con todas las variables
print(f"{nombre} tiene {edad} años, vive en {ciudad}, mide {altura}m. ¿Y estudia Python? {estudia_python}")
print("")
print("")

# Práctica 3, usar el input(), sirve para pedir datos al usuario y que el código sea interactivo.

# Pedir un dato al usuario
nombre = input("¿Cómo te llamas?")
print(f"¡Hola, {nombre}!")
print("")  # Esto genera espacios en el código

# Para pedir un número tenemos que cambiar el input() a float si es decimal o a int si es entero.
edad = int(input("¿Cuántos años tienes?"))
print("")

# Calcula en qué año nació: su edad menos el año actual 2026.
año_nacimiento = (2026 - edad)  # No usar {}, ya que edad es una variable por sí sola.
print("")

# Frase con f-string con los datos del usuario
print(f"{nombre} tiene {edad} años y nació en el año {año_nacimiento}")
print("")
print("")

# Práctica 4: Operaciones matemáticas. Usaremos los 7 operadores matemáticos.

# Teoría práctica 4:
a = 10
b = 3

print("")  # Al hacer las operaciones no pongas "" porque a y b son variables, si las pones pasarán de int a str.
print(a - b)   # 7
print(a + b)   # 13
print(a * b)   # 30
print(a / b)   # 3.33333
print(a // b)  # 3, si pones dos // se eliminan los decimales de la división.
print(a % b)   # 1, te da el resto de la división.
print(a ** b)  # 1000, si usas ** elevas el número, es decir 10 elevado a 3.
print("")

# Ejercicio práctica 4:
km = float(input("¿Cuántos kilómetros has recorrido?"))
consumo = float(input("¿Cuánto ha consumido tu coche en estos kilómetros?"))

litros = round(km * consumo / 100, 2)  # Aquí no hace falta paréntesis porque determina el valor de la variable, pero al querer redondear el resultado los tienes que poner después del round.

precio_combustible = float(input("¿Cuánto cuesta por litro el combustible?"))
precio_total_combustible = litros * precio_combustible

personas = int(input("¿Cuántas personas van en el coche?"))

if personas > 0:
    precio_persona = round(precio_total_combustible / personas, 2)  # Se pone la coma y el 2 para indicar cuántos decimales queremos.
    print(precio_persona)
else:
    print("No puede haber 0 personas")

# Con todas las operaciones hechas hacemos la frase f-string.
print("")
print(f"Han recorrido {km} kilómetros, han consumido {litros} litros, es decir, cada persona tiene que pagar {precio_persona} euros.")
print("")
print("")

# Práctica 5 (if, else y elif es la abreviación de "else if" — se usa para añadir más casos entre el if y el else.)

# Teoría práctica 5:
# El if permite que tu programa tome decisiones: "si se cumple esto, haz aquello; si no, haz otra cosa".
# == igual a, != distinto de, > mayor que, < menor que, >= mayor o igual, <= menor o igual.

# Ejemplo 1:
edad = int(input("¿Cuántos años tienes?"))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("")

# Ejemplo 2: (Con elif)
nota = int(input("¿Qué nota has sacado?"))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")

# Ejercicios práctica 5, ejercicio 1:
print("")
print("")

temperatura = float(input("¿A cuántos grados estamos?"))

if temperatura <= 0:
    print("Bajo cero, hielo")
elif temperatura <= 15:
    print("Frío")
elif temperatura <= 25:
    print("Agradable")
else:
    print("Calor")

print("")

# Ejercicio 2, par o impar:
print("")

numero = int(input("Escribe un número: "))

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")
    print("")
    print("")

# Práctica 6:

# Teoría: And, or y not: sirven para comprobar varias cosas a la vez, con estos tres podemos combinar condiciones en una sola línea.

# Ejemplo 1 (and, las dos se tienen que cumplir):
edad = int(input("¿Cuántos años tienes?"))
dinero = int(input("¿Cuánto dinero llevas?"))

if edad >= 18 and dinero >= 10:
    print("Puedes entrar en la discoteca")
else:
    print("No puedes entrar")

print("")

# Ejemplo 2 (or, es decir con uno es suficiente)
es_socio = True
tiene_invitacion = False

if es_socio or tiene_invitacion:
    print("Bienvenido al evento")
else:
    print("Acceso denegado")

print("")

# Ejemplo 3 (not, invierte el resultado, es decir no es False, es True. Es como decir NO está lloviendo)
esta_lloviendo = False

if not esta_lloviendo:
    print("Puedes salir sin paraguas")
else:
    print("Lleva el paraguas")

print("")
print("")

# Ejercicio práctica 6:
edad = int(input("¿Cuántos años tienes?"))
suscripcion = input("¿Tienes suscripción? si/no")

if edad >= 18 and suscripcion == "si":  # Tienes que poner las comillas del si, porque no es una variable sino un str.
    print("Acceso completo")
elif edad >= 18 and suscripcion == "no":
    print("Necesitas suscribirte")
else:
    print("Acceso denegado")

print("")
print("")

# Práctica 7 el bucle while:

# Teoría: El while repite un bloque de código mientras una condición sea verdadera. En cuanto la condición deja de cumplirse, el bucle para.

# Ejemplo 1 (Contador de vueltas):
contador = 1

while contador <= 5:
    print(f"Vuelta número {contador}")
    contador = contador + 1  # o contador += 1 es lo mismo, si falta esta parte del código el bucle se vuelve infinito. Si el programa se queda pillado pulsa Ctrl+C.

print("¡Carrera terminada!")  # Al llegar a 5 vueltas el bucle termina.
print("")

# Ejemplo 2 (Password):
password = input("Escribe la contraseña: ")

while password != "Beth1234":
    password = input("Incorrecta. Intenta otra vez: ")

print("")
print("")

# Ejercicio práctica 7 (Adivina el número):
numero_secreto = 0
intentos = 0

while numero_secreto != 17:
    numero_secreto = int(input("Escribe el número secreto: "))
    intentos += 1

    if numero_secreto > 17:
        print("Número demasiado alto")
    elif numero_secreto < 17:
        print("Número demasiado bajo")
    else:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos!")

    print()  # El print sin las dos "" sirve igual que sin ellas.

# Práctica número 8 el bucle for:

# Teoría: El for recorre una secuencia de elementos uno a uno y ejecuta el código para cada uno.
# A diferencia del while, no necesitas controlar un contador — el propio bucle sabe cuándo parar.

# Ejemplo 1, for con in range() sirve para repetir algo N veces:
for i in range(5):  # Después del for i del in range hay que poner :. Aquí le pedimos que la variable i llegue hasta 5.
    print(f"Vuelta {i}")

print("¡Terminado!")

# Ejemplo 2, for con una lista, es decir recorrer elementos.
print()

frutas = ["Manzana", "Pera", "Fresa", "Naranja", "Sandía"]

for fruta in frutas:
    print(f"Me gusta la {fruta}")

print()

# Ejemplo 3, for con texto, recorre letras:
nombre = "Beth"

for letra in nombre:
    print(letra)

# Ejercicio práctica 8, Tabla de multiplicar:
numero = int(input("Escribe el número que quieras multiplicar"))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
    print()

# Práctica 9, listas:

# Teoría: Una lista guarda varios valores en una sola variable, en orden.
# Se crea con corchetes [] y los elementos separados por comas.
# Puedes mezclar tipos: textos, números, booleans...

cantantes = ["Aitana", "Quevedo", "Bad Bunny", "Mora", "Lucía"]
numeros = ["17", "21", "14", "29", "10"]
mezcla = ["Beth", 16, True, 1.64]

# Ejemplo 1, acceder a elementos, índice.
cantantes = ["Aitana", "Quevedo", "Bad Bunny", "Mora", "Lucía"]  # El primero es el 0 y así puedes ir sumando o restando.

print(cantantes[0])
print(cantantes[1])
print(cantantes[2])
print(cantantes[3])
print(cantantes[4])

print()

# Ejemplo 2, operaciones básicas en listas.
print()

cantantes = ["Aitana", "Lucía", "Mora", "Quevedo", "Saiko"]

print(len(cantantes))  # El len indica cuántos elementos hay dentro de amigos, es decir te dirá 5.

cantantes.append("Omar")  # Añade a Omar al final
cantantes.remove("Mora")   # Elimina a Mora de la lista

print(cantantes)  # Imprimirá Aitana, Lucía, Quevedo, Saiko, Omar
print("Beth" in cantantes)  # False - comprobará si Beth está en cantantes, como no está pondrá False.

print()

# Ejemplo 3, recorrer una lista y dar información. (Notas de clase).
print()

notas = [5, 6, 1, 9, 4, 2, 7]

for nota in notas:
    if nota >= 5:
        print(f"{nota} Aprobado")
    else:
        print(f"{nota} Suspenso")

print()

# Práctica 9 (lista de la compra)
lista_compra = ["aguacate", "leche", "pan", "brócoli"]

print(lista_compra[0])
print(lista_compra[3])

lista_compra.append("yogur")
lista_compra.remove("pan")

for i, producto in enumerate(lista_compra, 1):
    print(f"{i}. {producto}")

print()

# Práctica 10, métodos.

# Teoría: Un método es una acción que puedes hacer sobre una lista.
# Se usa poniendo un punto después de la lista: lista.metodo().
# Ya conoces append() y remove() — ahora aprendes los más útiles.

print()

numeros = [1, 4, 7, 3, 9, 2]

# Los diferentes métodos:
numeros.append(3)      # El .append sirve para añadir algo al final de la lista.
numeros.insert(4, 5)   # El .insert sirve para insertar un número en una posición.
numeros.sort()         # El .sort sirve para ordenar de menor a mayor.
numeros.reverse()      # El .reverse invierte el orden de la lista.

ultimo = numeros.pop()  # Elimina el último número y lo guarda en la variable ultimo.

print(ultimo)   # Te imprimirá el número 2 que era el último de tu lista.
print(numeros)  # Imprime todos menos el último porque lo has cambiado de variable.

print()

# Ejemplo 2, count() y index().
# El count() te dice cuántas veces aparece algo y el index() en qué posición está.

notas = [7, 5, 9, 5, 3, 5, 8]

print(notas.count(5))   # Te dice cuántas veces aparece el número 5
print(notas.index(9))   # Te dice en qué posición está el 9
print(max(notas))       # Te dice la nota más alta
print(min(notas))       # Te dice la nota más baja
print(sum(notas))       # Suma todos los números.

print()

# Práctica 10, Gestor de notas.
notas = [3, 8, 4, 9, 2, 6]

notas.append(7)
notas.sort()

print(notas)  # Imprime las notas en orden
print(max(notas))
print(min(notas))
print(sum(notas) / len(notas))  # Imprime la media de las notas

for nota in notas:
    if nota >= 5:
        print("Aprobado")
    else:
        print("Suspenso")

# Prácticas de 1 a 10 terminadas.




