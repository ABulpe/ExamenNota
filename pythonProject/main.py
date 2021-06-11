import random


def player(list,name):
    for player in list:
        if player['name'] == name:
            return player
    return False


def apply(player,action):
    if action['type'] == 'cure':
        player['PV'] += action['PV']
    if action['type'] == 'attack':
        acierto = random.randint(0,100)
        if action['accurage'] >= acierto:
            player['PV'] -= action['PV']
    else:
        return False





if __name__ == '__main__':

    players =[
        {'name': 'Alberto', 'PV': 100},
        {'name': 'Beatriz', 'PV': 100},
        {'name': 'Abraham', 'PV': 100},
    ]

    actions = [
        {'type': 'attack', 'name': 'Alberto', 'PV': 10, 'goal': 'Abraham', 'accurage': 100},
        {'type': 'attack', 'name': 'Abraham', 'PV': 20, 'goal': 'Alberto', 'accurage': 80},
        {'type': 'cure', 'name': 'Alberto', 'PV': 20},
    ]

    print("Bienvenido al juego mas facil del mundo.")
    print("Estos son los comandos que puede ejecutar:")
    print("- crear \n -atacar \n -curar \n -listado \n -fin")
    game = True
    while game:
        try:
            command = input("Introduce un comando: ")
            if command == 'fin':
                game = False
            if command == 'listado':
                print(players)

            if command == 'crear':
                name = input('Introduce nombre de tu jugador: ')
                pv = input('Introduce pv de tu jugador: ')
                players.append({'name': name , 'PV': pv})

            if command == 'curar':
                name = input('Introduce nombre del jugador: ')
                flag = False
                pv = int(input('Introduce cantidad a curar: '))
                action = {'type': 'cure', 'name': name, 'PV': pv}
                jugador = player(players,name)
                if not jugador:
                    print('Tu jugador no existe. Intenta crearlo')
                    break

                apply(jugador, action)

            if command == 'atacar':
                name = input('Introduce nombre del jugador que atacara: ')
                goal = input('Introduce nombre del jugador objetivo: ')
                accurage = int(input('Introduce la probabilidad de acierto: '))
                pv = int(input('Introduce cantidad a restar: '))
                action = {'type': 'attack', 'name': name, 'PV': pv , 'goal': goal, 'accurage': accurage}
                jugador = player(players, goal)
                apply(jugador, action)
        except ValueError:
            print('Error: Debes introducir números donde corresponde')