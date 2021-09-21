#1. A pesar de que el domino tradicional se juega con fichas hasta el número 6, vamos a considerar un juego de fichas de valor máximo  n .Escribir una función que calcule la cantidad de fichas para un juego de dominó completo con fichas que contienen hasta el número  n . Nota: ¡No hay fichas repetidas! 2-4 es la misma ficha que 4-2. ¡Observar que en el dominó hay fichas con valor 0!

#2. Escribir una función que muestre todas las fichas para un juego de dominó como el anterior, en cualquier orden.

#COMENTARIO MIO:este codigo resuelve las dos consignas antriores

def cantidadFichas(x):
    c1 = 0
    c2 = x + 1
    c3 = 0
    cant = 0
    
    for a in range(c2):
        c1 = c3
        for b in range(c2):        
            print (c3, "-", c1)
            c1 += 1
            cant += 1
            
        c1 = c2 - 1
        c2 -= 1
        c3 += 1
        

    print ("Cantidad de fichas:", cant)    
    return (cant)


n = int(input("Valor máximo en ficha?"))
cantidadFichas(n)
