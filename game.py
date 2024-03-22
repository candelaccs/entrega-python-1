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
    for vocal in secret_word: # recorre la palabra a descifrar
        if vocal in vocals:
            guessed_letters.append(vocal)
        else:
            guessed_letters.append ("_")   
elif dif == "Media":
    guessed_letters.append(secret_word[0])
    guessed_letters.append(secret_word[-1])
    
else:
     None 
      #  word_displayed = "_" * len(secret_word) # se le asigna el tamaño de la palabra a adivinar / -------- 

word_displayed = ""     
if dif == "Facil" :
    for l in secret_word:
        if l in guessed_letters:
            word_displayed += l
        else:
            word_displayed += "_" 
elif dif == "Media":
     for l in secret_word:
        if l in guessed_letters:
            word_displayed += l
        else:
            word_displayed += "_" 
else:
    word_displayed = "_" * len(secret_word)

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
        if letter in guessed_letters :
            letters.append(letter) # si la letra esta en la lista de letras adivinadas, la agrega al final de la nueva lista letters
        else:
            letters.append("_") # sino hace un -

    word_displayed = "".join(letters) # concatena las letras todas juntas sin separar

    print(f"Palabra: {word_displayed}")


# Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break 

else: 
    print(f"¡Oh no! Has agotado los {max_fails} fallos.")
    print(f"La palabra secreta era: {secret_word}")


