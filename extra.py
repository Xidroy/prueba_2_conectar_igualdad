# Palíndromo:
# Es una palabra, frase u oración que se lee igual de izquierda a derecha que de derecha a izquierda.
# Ejemplos:
# "Ana lava lana"
# "Dábale arroz a la zorra el abad"
# "A ti, no, bonita"
def Palindromo():
    pass

# Anagrama:
# Son palabras que se forman reordenando las letras de otra palabra.
# Ejemplos:
# De "roma" podemos formar: "mora"
# De "cinema" podemos formar: "micene"
def Anagrama():
    pass

# Isograma:
# Es una palabra en la que todas las letras son diferentes.
# Ejemplos:
# "trompeta"
# "abcdefg"
def Isograma():
    pass


def Menu():
    print('''Te voy  a pedir dos palabras o frases y vamos a determinar si son:
          Palindromos.
          Anagramas
          Isogramas''')
    pof1=str(input('Dame una palabra o frase'))
    pof2=str(input('Dame una palabra o frase'))
    pof1.lower()
    pof2.lower() # Ver el alcancce de las dos variables de cadena de caracteres y ver como eliminar los espacios en caso de ser un frase.