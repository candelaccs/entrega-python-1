import random


# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]


# Elegir una palabra al azar
secret_word = random.choice(words)
 

# Número máximo de intentos permitidos
max_fails = 10
fails =0
# Lista para almacenar las letras adivinadas
guessed_letters = []


print("¡Bienvenido al juego de adivinanzas!")
print (" ------------------------------------------------------------------------------------------------- ")
print ("Seleccione el nivel de dificultad: ")
print (  )
print ("1. Facil  2. Media  3. Dificil ")
print ( )
dif = input ()
print ()
print (f"Usted selecciono dificultad:  {dif} ")
print ()
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")


if dif == "Facil":
    vocals = ["a", "e", "i", "o", "u"]
    show_vocals = []
    for vocal in secret_word: # recorre la palabra a descifrar
        if vocal in vocals:
            show_vocals.append(vocal)
        else:
            show_vocals.append ("_")
            word_displayed = "".join(show_vocals)
elif dif == "Media":
    first = secret_word[0] # 1er letra
    n = len(secret_word)
    last = secret_word[n-1] #ult letra
    sp = n-2
    word_displayed = first + ("_"*sp) + last    
    #print(word_displayed)
else:
       word_displayed = "_" * len(secret_word) # se le asigna el tamaño de la palabra a adivinar / -------- 
     

# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")


while fails < max_fails:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()


    if letter == "":
        print (" Error, eso es un espacio vacio, ingresa una letra! ")
        letter = input("Ingresa una letra: ").lower()


    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter) # agrega la letra al final


    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
         print("Lo siento, la letra no está en la palabra.")
         fails += 1


    # Mostrar la palabra parcialmente adivinada
    letters = [] 
    for letter in secret_word: # recorre la palabra a adivinar
        if letter in guessed_letters:
            letters.append(letter) # si la letra esta en la lista de letras adivinadas, la agrega al final de la nueva lista letters
        else:
            letters.append("_") # sino hace un -

    word_displayed = "".join(letters) # concatena las letras todas juntas sin separar

    print(f"Palabra: {word_displayed}")


# Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break 

else: # si llegó aca es porque ya agoto sus intentos/fallos
    print(f"¡Oh no! Has agotado los {max_fails} fallos.")
    print(f"La palabra secreta era: {secret_word}")


