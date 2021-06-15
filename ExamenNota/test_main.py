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
    tabla1 = [{'hoyo': 1, 'par': 0, 'golpes': 0}]
    par1 = 2
    hoyo1 = 1
    modifica_par(tabla1,hoyo1,par1)
    for element in tabla1:
        if element['hoyo'] == 1:
            assert element['par'] == 2



def test_modifica_golpes():
    tabla1 = [{'hoyo': 1, 'par': 1, 'golpes': 3}]
    par1 = 2
    hoyo1 = 1
    golpes1 = 5
    modifica_golpes(tabla1,hoyo1,golpes1)
    for element in tabla1:
        if element['hoyo'] == 1:
            assert element['golpes'] == 5

def test_resultado():
    tabla1 = [{'hoyo': 16, 'par': 4, 'golpes': 6},
              {'hoyo': 10, 'par': 4, 'golpes': 10},
              {'hoyo': 14, 'par': 4, 'golpes': 5},
              {'hoyo': 17, 'par': 3, 'golpes': 3},
              {'hoyo': 18, 'par': 4, 'golpes': 3},
              {'hoyo': 15, 'par': 5, 'golpes': 3},
              ]

    assert resultado(tabla1,10) == -6
    assert resultado(tabla1,14) == 'BOGEY'
    assert resultado(tabla1,17) == 'PAR'
    assert resultado(tabla1,18) == 'BIRDIE'
    assert resultado(tabla1,15) == 'EAGLE'
    assert resultado(tabla1,16) == 'DOBLE BOGEY'



def test_resultadotabla():
    assert resultadotabla(tabla) == 0