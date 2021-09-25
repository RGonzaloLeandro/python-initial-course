#Escribir una función que, dada una cantidad de fichas, calcule cuál es el  n  (valor máximo) de las fichas. Si el número de fichas no corresponde a la cantidad de fichas de ningún juego de dominó completo retornar -1.

def valMaxFichas(maxValue):
    vmax = []
    i = 1
    while sum(vmax) < maxValue:
        vmax.append (i)
        i += 1

    if  not (sum(vmax) == maxValue):
        print ("Inválido")
    else:
        print ("Válido")
        print("Valor máximo de ficha:" + str(vmax[-2]))

n = int(input("Cantidad de fichas?"))
valMaxFichas(n)


