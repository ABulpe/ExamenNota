from main import player
from main import apply

players = [
    {'name': 'Alberto', 'PV': 100},
    {'name': 'Beatriz', 'PV': 100},
    {'name': 'Abraham', 'PV': 100},
]

jugador = player(players,'Alberto')
actions = [
        {'type': 'attack', 'name': 'Alberto', 'PV': 10, 'goal': 'Abraham', 'accurage': 100},
        {'type': 'attack', 'name': 'Abraham', 'PV': 20, 'goal': 'Alberto', 'accurage': 80},
        {'type': 'cure', 'name': 'Alberto', 'PV': 20},
    ]

def test_player():
    assert player(players,'Beatriz') == {'name': 'Beatriz', 'PV': '100'}
    assert player(players,'Alberto') == {'name': 'Alberto', 'PV': '100'}

def test_apply():
    apply(jugador,actions[1])
    assert jugador['PV'] == 80
    apply(jugador,actions[2])
    assert jugador['PV'] == 100

