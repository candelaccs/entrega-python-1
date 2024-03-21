import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_attempts = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

word_displayed = "_" * len(secret_word) # se le asigna el tamaño de la palabra a adivinar / --------

# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

for i in range(max_attempts):
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()

     if letter == "":
         print (" Error, eso es un espacio vacio, ingresa una letra! ")
         letter = input("Ingresa una letra: ").lower() 

     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         continue # hacia donde seguiria? se salta el guessed_letters?
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter) # agrega la letra al final // no debria ir mas adentro identado?

     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
          print("Lo siento, la letra no está en la palabra.")

     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter) # si la letra esta en la lista de letras adivinadas, la agrega al final de la nueva lista letters
         else:
             letters.append("_") # sino hace un - // cmo las pone ordenadas?

     word_displayed = "".join(letters) # concatena las letras todas juntas sin separar
     print(f"Palabra: {word_displayed}")



# Verificar si se ha adivinado la palabra completa
if word_displayed == secret_word:
     print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
else:
     print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
     print(f"La palabra secreta era: {secret_word}")