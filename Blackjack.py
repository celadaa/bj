import random

CORAZON   = chr(9829) # Character 9829 is '♥'.
DIAMANTE = chr(9830) # Character 9830 is '♦'.
PICA   = chr(9824) # Character 9824 is '♠'.
TREBOL    = chr(9827) # Character 9827 is '♣'.

NUM_BARAJAS = 6
PALOS = [CORAZON,DIAMANTE,PICA,TREBOL] * NUM_BARAJAS
VALORES = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] * NUM_BARAJAS

def crear_baraja() -> list:
    baraja = []
    for palo in PALOS:
        for valor in VALORES:
            baraja.append((valor,palo))
    random.shuffle(baraja)
    return baraja

def crupier_logica(cartas):
    if obtener_valor_cartas(cartas) < 17:
        cartas_dealer.append(baraja.pop())

def mostrar_cartas(cartas, dealer = False) -> None:
    for fila in range(4):
        ace = 0
        for columna, carta in enumerate(cartas):
            valor, palo = carta
            if valor == 'a': ace += 1
            if dealer and columna == 1: valor, palo = '*', '?'
            if fila == 0:
                print(' ___ ', end=' ')
            elif fila == 1:
                print(f'|{valor}  |', end=' ')
            elif fila == 2:
                print(f'| {palo} |', end=' ')
            elif fila == 3:
                print(f'|__{valor}|', end=' ')
        print()
        if fila == 3 and not dealer:
            print(f"{obtener_valor_cartas(cartas)}".rjust(len(cartas) * 5 + (len(cartas) - 1),'-'))

def obtener_valor_cartas(cartas) -> int:
    valor = 0
    for carta in cartas:
        if carta[0] in ['J','Q','K']:
            valor += 10
        elif carta[0] == 'A':
            if valor + 11 == 21 or valor < 11 :
                valor += 11
            elif valor + 11 > 21:
                valor += 1
        else:
            valor += carta[0]
    return valor

def pedir() -> bool:
    decision = ''
    while decision not in ['H','S']:
        decision = input("H | S\n").upper()
    return True if decision == 'H' else False


baraja = crear_baraja()
cartas_dealer = [baraja.pop(),baraja.pop()]
cartas_jugador = [baraja.pop(),baraja.pop()]
print('Dealer')
mostrar_cartas(cartas_dealer, True)
print('Jugador')
mostrar_cartas(cartas_jugador)

if pedir():
    cartas_jugador.append(baraja.pop())

mostrar_cartas(cartas_jugador)
mostrar_cartas(cartas_dealer)
crupier_logica(cartas_dealer)
mostrar_cartas(cartas_dealer)


