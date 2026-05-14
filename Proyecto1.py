
aciertos = 0
fallos = 0
lista_fallos = []

print("Bienvenida")

nombre = input("¿Cómo te llamas? ")
print()

print(f"Hola, {nombre}, vamos a jugar al juego de las 5 preguntas")

print()
print("Empecemos, pero antes responde dos preguntas de prueba")
print()

edad = input("¿Cuántos años tienes? ")

print()
print("Ahora sí, empecemos con las preguntas, y recuerda: al responder escribe en minúsculas")
print()

lados = int(input("¿Cuántos lados tiene un cuadrado? "))

if lados == 4:
    print("Correcto")
    aciertos += 1
else:
    print("Incorrecto, tiene 4 lados")
    fallos += 1
    lista_fallos.append("¿Cuántos lados tiene un cuadrado?")

print()

tema = input("La próxima pregunta puedes elegir el tema. Elige música o fútbol: ")

if tema == "musica":
    musica = input("Buena elección. ¿Cómo se llama el álbum que sacó Aitana en 2025? ").lower()  # .lower sirve por si escriben mayúsculas.
    
    if musica == "cuarto azul":
        print("Correcto, pasemos a la siguiente pregunta")
        aciertos += 1
    else:
        print("Incorrecto, el álbum se llama Cuarto Azul")
        fallos += 1
        lista_fallos.append("¿Cómo se llama el álbum que sacó Aitana en 2025?")

elif tema == "futbol":
    futbol = input("Buena elección. ¿Cuántas Champions tiene el FC Barcelona? ").lower()

    if futbol == "5" or futbol == "cinco":
        print("Correcto, vamos a la siguiente pregunta")
        aciertos += 1
    else:
        print("Incorrecto, el FC Barcelona tiene 5 Champions")
        fallos += 1
        lista_fallos.append("¿Cuántas Champions tiene el FC Barcelona?")

print()

barcelona = input("¿En qué ciudad está la Sagrada Família? ").lower()

if barcelona == "barcelona":
    print("Correcto, pasemos a la siguiente pregunta")
    aciertos += 1
else:
    print("Casi, se encuentra en Barcelona")
    fallos += 1
    lista_fallos.append("¿En qué ciudad está la Sagrada Família?")

print()

america = int(input("¿En qué año llegó Colón a América? "))

if america == 1492:
    print("Correcto, vamos a por la última pregunta")
    aciertos += 1
else:
    print("Llegó en 1492, bueno no pasa nada, vamos a por la penúltima pregunta")
    fallos += 1
    lista_fallos.append("¿En qué año llegó Colón a América?")

covid = input("¿En qué año comenzó el confinamiento por Covid? ¿Cuántos días duró el confinamiento? ").lower()

if covid == "comenzo en 2020" or covid == "2020":
    print("Muy bien, esta era difícil")
    aciertos += 1
else:
    print("Comenzó en 2020 y duró 99 días, esta era difícil")
    fallos += 1
    lista_fallos.append("¿En qué año comenzó el confinamiento por Covid? ¿Cuántos días duró el confinamiento?")

celulas = int(input("¿Cuántos tipos de células hay? "))

if celulas == 2:
    print("Esta era fácil, es correcta")
    aciertos += 1
else:
    print("Casi, la respuesta era 2")
    fallos += 1
    lista_fallos.append("¿Cuántos tipos de células hay?")

puntuacion = aciertos * 2

if puntuacion >= 9:
    print("Sobresaliente")
elif puntuacion >= 7:
    print("Notable")
elif puntuacion >= 5:
    print("Suficiente")
else:
    print("Suspenso")

print(f"{nombre}, has acertado {aciertos} y fallado {fallos}. Puntuación: {puntuacion}/10")

if lista_fallos:
    print("Preguntas falladas:")

    for pregunta in lista_fallos:
        print(f"  - {pregunta}")



    
     

    


    