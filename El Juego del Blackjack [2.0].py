__author__ = "Lautaro Toloza"

import random, time


def mostrar_menu_principal():
    print("\033[1;34m" + "---" * 30 + "\033[0;m")
    print("\033[1;34m" + "Bienvenidos al menú de opciones!!" + "\033[0;m")
    print("1. Apostar")
    print("2. Jugar una mano")
    print("3. Salir")
    print("\033[1;34m" + "---" * 30 + "\033[0;m")


def incrementar_pozo(pozo):
    flag = True
    incremento = int(input("Ingrese el incremento que desea a su pozo, tiene que ser mayor a 0 y múltiplo de 5: "))
    while flag:
        if incremento % 5 == 0 and incremento > 0:
            flag = False
        else:
            print("\033[1;31m" + "Error, el pozo tiene que ser mayor a 0 y múltiplo de 5!! " + "\033[0;m")
            incremento = int(input('Ingrese el incremento que desea a su pozo: '))

    pozo_actualizado = pozo + incremento

    return pozo_actualizado


def apuesta_valida(pozo):
    flag = True
    monto_apuesta = int(input("Ingrese el monto de la apuesta: "))
    while flag:
        if monto_apuesta % 5 == 0 and monto_apuesta <= pozo:
            flag = False
        else:
            print(
                "\033[1;31m" + "Error, el monto de la apuesta tiene que ser mayor a 0, tiene que ser múltiplo de 5 y tiene que ser menor o igual a su pozo!!" + "\033[0;m")
            monto_apuesta = int(input("Ingrese el monto de la apuesta: "))
    return monto_apuesta


def carta():
    numeros = (2, 3, 4, 5, 6, 7, 8, 9, 10, "AS", "J", "Q", "K")
    palos = ('Picas', 'Tréboles', 'Rombos', 'Corazones')
    carta_valor = random.choice(numeros)
    carta_palo = random.choice(palos)
    return carta_valor, carta_palo


def puntaje_carta(carta, puntaje, flag_as):
    if carta == "J" or carta == "Q" or carta == "K":
        puntaje += 10
    elif carta == "AS":
        if puntaje + 11 <= 21:
            mensaje = "\nLe tocó un AS.\nOpciones.. \nIngresando un '1' sumara 1 punto. \nIngresando un '2' sumara 11 puntos. \nIngrese su opción: "
            op = input(mensaje)
            while op != "1" and op != "2":
                print("Error, ingreso una opción incorrecta!!")
                op = input(mensaje)

            if op == "1":
                puntaje += 1
            else:
                puntaje += 11
                flag_as = True
        else:
            puntaje += 1

    else:
        puntaje += carta
    # Si se pasa del puntaje y tenia un as.
    if puntaje > 21 and flag_as:
        puntaje -= 10
        flag_as = False
    return puntaje, flag_as


def pedir_carta_jug(puntaje, flag_as):
    mensaje = "Ingrese una opción: '1' para pedir carta o '2' para frenarse: "
    numero_carta = (
        "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce"
        , "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiuno")
    cont = 0
    flag = True
    print("\033[1;34m" + "Continua jugando el jugador.." + "\033[0;m")
    while flag:
        if puntaje < 21:
            op = input(mensaje)
            if op == "1":
                carta_jug, palo_carta_jug = carta()
                print("Carta " + numero_carta[cont] + " jugador: ", carta_jug, palo_carta_jug)
                puntaje, flag_as = puntaje_carta(carta_jug, puntaje, flag_as)
                cont += 1
            elif op == "2":
                flag = False
            else:
                print("Error!! opción no válida, intente nuevamente!! ")
        else:
            flag = False
    return puntaje


def es_blackjack_natural(puntaje):
    flag = False
    if puntaje == 21:
        flag = True
    return flag


def pedir_carta_crup(puntaje, flag_as):
    numero_carta = (
        "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce"
        , "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiuno")
    cont = 0
    flag = True
    while flag:
        if puntaje < 17:
            carta_crup, palo_carta_crup = carta()
            print("Carta " + numero_carta[cont] + " crupier: ", carta_crup, palo_carta_crup)
            puntaje, flag_as = puntaje_carta(carta_crup, puntaje, flag_as)
            cont += 1
        else:
            flag = False
    return puntaje


def ganador(puntaje_jug, puntaje_crup, natural_jug, natural_crup, pozo, apuesta):
    ok_j = ok_c = ok_bj_n = False
    pozo_inicial = pozo
    if natural_jug == True and natural_crup:
        print("\n\033[1;33m" + "SE PRODUJO UN EMPATE, JUEGUEN NUEVAMENTE!! " + "\033[0;m")
        pozo = pozo
        ok_bj_n = True
    elif natural_jug == False and natural_crup:
        print("\n\033[1;33m" + "EL GANADOR DE LA MANO FUE EL CRUPIER!!" + "\033[0;m")
        pozo -= apuesta
        ok_c = True
        ok_bj_n = True
    elif natural_crup == False and natural_jug:
        print("\n\033[1;33m" + "EL GANADOR DE LA MANO FUE EL JUGADOR!!" + "\033[0;m")
        pozo += apuesta
        ok_j = True
        ok_bj_n = True
    elif puntaje_jug > puntaje_crup and puntaje_jug <= 21:
        print("\n\033[1;33m" + "EL GANADOR DE LA MANO FUE EL JUGADOR!!" + "\033[0;m")
        pozo += apuesta
        ok_j = True
    elif puntaje_crup > puntaje_jug and puntaje_crup <= 21:
        print("\n\033[1;33m" + "EL GANADOR DE LA MANO FUE EL CRUPIER!!" + "\033[0;m")
        pozo -= apuesta
        ok_c = True
    elif puntaje_crup > 21 and puntaje_jug <= 21:
        print("\n\033[1;33m" + "EL GANADOR DE LA MANO FUE EL JUGADOR!!" + "\033[0;m")
        pozo += apuesta
        ok_j = True
    elif puntaje_jug > 21 and puntaje_crup <= 21:
        print("\n\033[1;33m" + "EL GANADOR DE LA MANO FUE EL CRUPIER!!" + "\033[0;m")
        pozo -= apuesta
        ok_c = True
    elif puntaje_jug > 21 and puntaje_crup > 21:
        print("\n\033[1;33m" + "EL GANADOR DE LA MANO FUE EL CRUPIER!!" + "\033[0;m")
        pozo -= apuesta
        ok_c = True
    else:
        print("\n\033[1;33m" + "SE PRODUJO UN EMPATE, JUEGUEN NUEVAMENTE!! " + "\033[0;m")
        pozo = pozo

    if ok_c:
        perdida = pozo_inicial - pozo
    else:
        perdida = 0
    return pozo, ok_j, ok_c, ok_bj_n, perdida


def victorias(ok_j, vic_j, ok_c, vic_c, racha_c):
    if ok_j:
        vic_j += 1
        vic_c = 0
    elif ok_c:
        vic_c += 1
        if vic_c > racha_c:
            racha_c = vic_c
    else:
        vic_c = 0
    return vic_j, racha_c


def porcentaje_victorias_jugador(tot_manos, vic_j):
    porcentaje = vic_j * 100 / tot_manos
    return porcentaje


def promedio_monto(tot_monto, cont_manos):
    promedio = tot_monto / cont_manos
    return promedio


def test():
    print("\t\033[1;33m" + "Bienvenidos al juego del Blackjack [versión 2.0]!!" + "\033[0;m")
    print("\033[1;33m" + "**" * 30 + "\033[0;m")
    nombre_jug = input("Jugador, ingrese su nombre: ")
    con_mano = 1
    vic_jug = vic_crup = 0
    racha_crup = 0
    cont_bj_natural = 0
    perdida_may = None
    pozo = int(input('Ingresar el pozo para jugar hasta un máximo $100000: '))
    while pozo <= 0 or pozo > 100000:
        print("\033[1;31m" + "Error, el pozo tiene que ser mayor a 0!!" + "\033[0;m")
        pozo = int(input('Ingresar el pozo para jugar, el máximo es $100000: '))
    max_monto = tot_monto = pozo
    op = -1
    while op != 3:
        mostrar_menu_principal()
        op = int(input("Elija una opción: "))
        if op == 1:
            pozo = incrementar_pozo(pozo)
            print("El pozo actualizado es: ", pozo)
        elif op == 2:
            print("Monto del pozo: ", pozo)
            if pozo < 5:
                print("\033[1;31m" + "No tiene suficiente dinero para apostar, incremente su pozo!!" + "\033[0;m")
                pozo = incrementar_pozo(pozo)
                print("Monto actual del pozo: ", pozo)
            monto_apuesta = apuesta_valida(pozo)
            print("Monto apuesta: ", monto_apuesta)
            carta1_jug, palo_carta1_jug = carta()
            carta2_jug, palo_carta2_jug = carta()
            carta1_crup, palo_carta1_crup = carta()
            puntaje_jug = puntaje_crup = 0
            flag_as_jug = flag_as_crup = False

            # Carta 1 y 2 del jugador y carta 1 del crupier.
            print("Carta uno jugador: ", carta1_jug, palo_carta1_jug)
            print("Carta dos jugador: ", carta2_jug, palo_carta2_jug)
            print("Carta uno crupier: ", carta1_crup, palo_carta1_crup)
            puntaje_jug, flag_as_jug = puntaje_carta(carta1_jug, puntaje_jug, flag_as_jug)
            puntaje_jug, flag_as_jug = puntaje_carta(carta2_jug, puntaje_jug, flag_as_jug)

            # Hubo blackjack natural del jugador.
            flag_blackjack_natu_jug = es_blackjack_natural(puntaje_jug)
            puntaje_crup, flag_as_crup = puntaje_carta(carta1_crup, puntaje_crup, flag_as_crup)

            # Sigue jugando el jugador
            puntaje_jug = pedir_carta_jug(puntaje_jug, flag_as_jug)

            # Carta 2 del crupier y se analiza si hubo blackjack natural.
            carta2_crup, palo_carta2_crup = carta()
            print("\033[1;34m" + "Continua jugando el crupier.." + "\033[0;m")
            print("Carta dos crupier: ", carta2_crup, palo_carta2_crup)
            puntaje_crup, flag_as_crup = puntaje_carta(carta2_crup, puntaje_crup, flag_as_crup)
            flag_blackjack_natu_crup = es_blackjack_natural(puntaje_crup)
            puntaje_crup = pedir_carta_crup(puntaje_crup, flag_as_crup)

            # Ganador de partida
            time.sleep(1)
            print("\n\033[1;34m" + "Muestra del resultado final... " + "\033[0;m")
            print("\033[1;34m" + "---" * 30 + "\033[0;m")

            print("Puntaje final del jugador: ", puntaje_jug)
            print("Puntaje final del crupier: ", puntaje_crup)
            # Aca black jacj natural
            pozo, g_jug, g_crup, bj_natural, perdida = ganador(puntaje_jug, puntaje_crup, flag_blackjack_natu_jug,
                                                               flag_blackjack_natu_crup, pozo, monto_apuesta)
            print("Monto actualizado del pozo: ", pozo)
            print("\033[1;34m" + "---" * 30 + "\033[0;m")
            tot_monto += pozo
            if pozo > max_monto:
                max_monto = pozo
            # Datos para el punto 3
            vic_jug, racha_crup = victorias(g_jug, vic_jug, g_crup, vic_crup, racha_crup)
            if bj_natural:
                cont_bj_natural += 1

            if perdida_may is None or perdida > perdida_may:
                perdida_may = perdida

            con_mano += 1

        elif op == 3:
            if pozo > max_monto:
                max_monto = pozo
            if con_mano != 0:
                porc = porcentaje_victorias_jugador(con_mano, vic_jug)
                prom = promedio_monto(tot_monto, con_mano)
            else:
                porc = 0
                prom = 0
            print("\n\033[1;31m" + "**" * 30 + "\033[0;m")
            print("\t\t\t\033[1;31m" + "Muestra de los resultados!! " + "\033[0;m")
            print("\033[1;31m" + "**" * 30 + "\033[0;m")
            print("Monto actualizado del pozo: ", pozo)
            print("El porcentaje de victorias del jugador: ", round(porc, 2), " %")
            print("La racha más larga de victorias del croupier: ", racha_crup)
            # Donde hubo un bj
            print("La cantidad de manos donde hubo un blackjack natural: ", cont_bj_natural)
            print("El monto máximo que llegó a tener el jugador en el pozo: ", max_monto)
            print("El monto promedio del que dispuso el jugador para realizar apuestas: ", round(prom, 2))
            if perdida_may is None or perdida_may == 0:
                print("El jugador no tuvo ninguna perdida!! ")
            else:
                print("La pérdida más grande que sufrió el jugador: ", perdida_may)
            print("\033[1;31m" + "---" * 30 + "\033[0;m")
        else:
            print("Error, ingreso una opción incorrecta!! ")
    print("Finalizo el programa, gracias por jugar!!")
    print("Programa realizado por: (" + __author__ + ")")


# Script principal.
test()
