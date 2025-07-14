from src.verificador import son_anagramas
# Test Para Anagramas
def test_anagramas_basico():
    assert son_anagramas("roma", "amor") is True

def test_anagramas_falso():
    assert son_anagramas("python", "java") is False

def test_anagramas_con_espacios():
    assert son_anagramas("listen", "silent") is True
    assert son_anagramas("funeral", "real fun") is True

def test_anagramas_unicode():
    assert son_anagramas("café", "féca") is True 

