# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowel_count = 0  # Variable de contador para las vocales
    
    # Lista de vocales
    vocales = ["a", "e", "i", "o", "u"]
    
    for letter in sentence:
        if letter in vocales and letter != 'y':
            vowel_count += 1  # Incrementa el contador cuando se encuentra una vocal (que no sea 'y')
    
    return vowel_count  # Devuelve el recuento de vocales (sin contar 'y')

# Ejemplo de uso:
resultado = get_count("paralelepipedo")
print(resultado)  # Debería imprimir el número de vocales (sin contar 'y'), en este caso, 6

