#Escribir una función que, dada una cantidad de fichas, calcule cuál es el n(valor máximo) de las fichas. Si el número de fichas no corresponde a la cantidad de fichas de ningún juego de dominó completo retornar "Inválido" y en caso contrario que indique "Válido" y el valor máximo de las fichas de ese juego de dominó.

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
        print("Valor máximo de ficha:" + str(vmax[-1]))

n = int(input("Cantidad de fichas?"))
if n <= 0:
    print ("Inválido")
else:
    valMaxFichas(n)


