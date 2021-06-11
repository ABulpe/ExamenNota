from main import modifica_par, modifica_golpes, resultado, termino_golf, resultadotabla

tabla = [
    {'hoyo': 1, 'par': 0, 'golpes': 0},
    {'hoyo': 2, 'par': 0, 'golpes': 0},
    {'hoyo': 3, 'par': 0, 'golpes': 0},
    {'hoyo': 4, 'par': 0, 'golpes': 0},
    {'hoyo': 5, 'par': 0, 'golpes': 0},
    {'hoyo': 6, 'par': 0, 'golpes': 0},
    {'hoyo': 7, 'par': 3, 'golpes': 1},
    {'hoyo': 8, 'par': 0, 'golpes': 0},
    {'hoyo': 9, 'par': 0, 'golpes': 0},
    {'hoyo': 10, 'par': 4, 'golpes': 4},
    {'hoyo': 11, 'par': 0, 'golpes': 0},
    {'hoyo': 12, 'par': 0, 'golpes': 0},
    {'hoyo': 13, 'par': 0, 'golpes': 0},
    {'hoyo': 14, 'par': 4, 'golpes': 5},
    {'hoyo': 15, 'par': 5, 'golpes': 6},
    {'hoyo': 16, 'par': 4, 'golpes': 4},
    {'hoyo': 17, 'par': 3, 'golpes': 3},
    {'hoyo': 18, 'par': 4, 'golpes': 4},
]
hoyo = 1
par = 3
golpes = 7
def test_modifica_par():
    modifica_par(tabla,hoyo,par)
    for element in tabla:
        if element['hoyo'] == 1:
            assert element['par'] == 0



def test_modifica_golpes():
    modifica_golpes(tabla,hoyo,golpes)
    for element in tabla:
        if element['hoyo'] == 1:
            assert element['golpes'] == 7

def test_resultado():
    assert resultado(tabla,10) == -6
    assert resultado(tabla,14) == 'PAR'
    assert resultado(tabla,17) == 'EAGLE'
    assert resultado(tabla,18) == 'BIRDIE'
    assert resultado(tabla,15) == 'DOBLE BOGEY'
    assert resultado(tabla,16) == 'BOGEY'



def test_resultadotabla():
    assert resultadotabla(tabla) == 0