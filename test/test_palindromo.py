from src.verificador import es_palindromo
# Test Para Palindromos
def test_palindromo_simple():
    assert es_palindromo("reconocer") is True 

def test_no_es_palindromo():
    assert es_palindromo("python") is False

def test_palindromo_con_espacios():
    assert es_palindromo("anita lava la tina") is True

def test_palindromo_con_mayusculas():
    assert es_palindromo("Ana") is True

def test_palindromo_vacio():
    assert es_palindromo("") is True  # Caso borde

def test_palindromo_con_numeros():
    assert es_palindromo("12321") is True