# FUNCIONES ANAGRAMA
# def son_anagramas(palabra1: str, palabra2: str) -> bool:
#     return True

# def son_anagramas(palabra1: str, palabra2: str) -> bool:
#     return sorted(palabra1.lower()) == sorted(palabra2.lower())

def son_anagramas(palabra1: str, palabra2: str) -> bool:
    # Elimina espacios y normaliza a minúsculas
    palabra1_limpia = palabra1.lower().replace(" ", "")
    palabra2_limpia = palabra2.lower().replace(" ", "")
    return sorted(palabra1_limpia) == sorted(palabra2_limpia)

# FUNCIONES PALINDROMOS

# def es_palindromo(palabra: str) -> bool:
#     return True

# def es_palindromo(palabra: str) -> bool:
#     return palabra == palabra[::-1] 

# def es_palindromo(palabra: str) -> bool:
#     return palabra == palabra[::-1] 

def es_palindromo(palabra: str) -> bool:
    caracteres_limpios = []
    for i in palabra:
        if i.isalnum():
            caracteres_limpios.append(i.lower())  
    palabra_limpia = ''.join(caracteres_limpios)  
    return palabra_limpia == palabra_limpia[::-1]