
def modifica_par(tabla,hoyo,par):
    for elemento in tabla:
        if elemento['hoyo'] == hoyo:
            elemento['par']= par

def modifica_golpes(tabla,hoyo,golpes):
    for elemento in tabla:
        if elemento['hoyo'] == hoyo:
            elemento['golpes'] = golpes

def listado(tabla):
    for element in tabla:
        print( 'HOYO:',element['hoyo'] ,'PAR:',element['par'],'GOLPES:', element['golpes'])


def resultado(tabla,hoyo):
    for element in tabla:
        if element['hoyo'] == hoyo:
            resultado = element['par'] - element ['golpes']
            return termino_golf(resultado)

def resultadotabla(tabla):
    resultado = 0
    for element in tabla:
        resultado += element['par'] - element['golpes']
    return resultado

def termino_golf(resultado):
    if resultado == 0:
        return 'PAR'
    if resultado == 1:
        return 'BIRDIE'
    if resultado == -1:
        return 'BOGEY'
    if resultado == 2:
        return 'EAGLE'
    if resultado == -2:
        return 'DOBLE BOGEY'

    else:
        return resultado

if __name__ == '__main__':


    tabla = [
        {'hoyo': 1, 'par':0, 'golpes':0},
        {'hoyo': 2, 'par': 0, 'golpes': 0},
        {'hoyo': 3, 'par': 0, 'golpes': 0},
        {'hoyo': 4, 'par': 0, 'golpes': 0},
        {'hoyo': 5, 'par': 0, 'golpes': 0},
        {'hoyo': 6, 'par': 0, 'golpes': 0},
        {'hoyo': 7, 'par': 0, 'golpes': 0},
        {'hoyo': 8, 'par': 0, 'golpes': 0},
        {'hoyo': 9, 'par': 0, 'golpes': 0},
        {'hoyo': 10, 'par': 0, 'golpes': 0},
        {'hoyo': 11, 'par': 0, 'golpes': 0},
        {'hoyo': 12, 'par': 0, 'golpes': 0},
        {'hoyo': 13, 'par': 0, 'golpes': 0},
        {'hoyo': 14, 'par': 0, 'golpes': 0},
        {'hoyo': 15, 'par': 0, 'golpes': 0},
        {'hoyo': 16, 'par': 0, 'golpes': 0},
        {'hoyo': 17, 'par': 0, 'golpes': 0},
        {'hoyo': 18, 'par': 0, 'golpes': 0},
    ]
    print(tabla)
    print('Bienvenido a tu gestor de golf...')
    print('Para modificar los valores de la tabla ejecute: ')
    print('-Cambiar par = par HOYO GOLPE \n-Cambiar golpe = HOYO GOLPE')
    print('Ejecute uno de los siguientes comandos para otras opciones:')
    print('-listado \n -resultado \n score \n -exit')

    game = True
    while game:
        try:
            command = input('Introduce el comando que quieras realizar: ')
            comando = command.split(' ')
            if command == 'exit':
                game = 'False'

            if len(comando)== 3 and comando[0] == 'par':
                hoyo = int(comando[1])
                if hoyo > 18 or hoyo < 1:
                    print('El rango de HOYO es 1-18, intentalo de nuevo.')
                    continue
                par = int(comando[2])

                modifica_par(tabla, hoyo, par)


            if len(comando)==2:
                hoyo = int(comando[0])
                if hoyo > 18 or hoyo < 1:
                    print('El rango de HOYO es 1-18, intentalo de nuevo.')
                    continue
                golpes = int(comando[1])
                if golpes < 0:
                    print('El número de golpes debe ser entero positivo')
                    continue
                for element in tabla:
                    if element['hoyo'] == hoyo:
                        if element['par'] == 0:
                            print('No se ha introducido el par correspondiente al hoyo.')
                            par = int(input('Introduce el par que tendra el hoyo seleccionado: '))
                            modifica_par(tabla, hoyo, par)

                        if element['golpes'] != 0:
                            respuesta = input('El resultado ya ha sido cargado. ¿Desea modificarlo? \n y o n: ')
                            if respuesta == 'y':
                                modifica_golpes(tabla, hoyo, golpes)
                                break
                            if respuesta == 'n':
                                print('El resultado no se modificara')
                                break
                            else:
                                print('Has introducido una respuesta incorrecta. Introduce Y o N: ')
                                continue
                        modifica_golpes(tabla, hoyo, golpes)

            if command =='listado':
                listado(tabla)

            if command == 'resultado':
                hoyo = int(input('Introduce el hoyo del que quieras ver el resultado: '))
                if hoyo > 18 or hoyo < 1:
                    print('El rango de HOYO es 1-18, intentalo de nuevo.')
                    continue
                print(resultado(tabla, hoyo))

            if command == 'score':
                print(resultadotabla(tabla))

            '''
            PRIMERA VERSION:
            if command == 'exit':
                game = 'False'
            if command == 'par':
                hoyo = int(input('Introduce el número del hoyo a modificar: '))
                if hoyo > 18 or hoyo<1:
                    print('El rango de HOYO es 1-18, intentalo de nuevo.')
                    continue
                par = int(input('introduce el número de golpes que tendra el par: '))
                modifica_par(tabla,hoyo,par)

            if command == 'golpes':
                hoyo = int(input('Introduce el número del hoyo a modificar: '))
                if hoyo > 18 or hoyo < 1:
                    print('El rango de HOYO es 1-18, intentalo de nuevo.')
                    continue
                golpes = int(input('introduce el resultado: '))
                if golpes < 0:
                    print('El número de golpes debe ser entero positivo')
                    continue
                for element in tabla:
                    if element['hoyo'] == hoyo:
                        if element['par'] == 0:
                            print('No se ha introducido el par correspondiente al hoyo.')
                            par = int(input('Introduce el par que tendra el hoyo seleccionado: '))
                            modifica_par(tabla,hoyo,par)

                        if element['golpes'] != 0:
                            respuesta = input('El resultado ya ha sido cargado. ¿Desea modificarlo? \n y o n: ')
                            if respuesta == 'y':
                                modifica_golpes(tabla, hoyo, golpes)
                                break
                            if respuesta == 'n':
                                print('El resultado no se modificara')
                                break
                            else:
                                print('Has introducido una respuesta incorrecta. Introduce Y o N: ')
                                continue
                        modifica_golpes(tabla, hoyo, golpes)

            if command == 'listado':
                listado(tabla)

            if command == 'resultado':
                hoyo = int(input('Introduce el hoyo del que quieras ver el resultado: '))
                if hoyo > 18 or hoyo < 1:
                    print('El rango de HOYO es 1-18, intentalo de nuevo.')
                    continue
                print(resultado(tabla,hoyo))'''


        except ValueError:
            print('Error: Debes introducir números cuando se requiera')






