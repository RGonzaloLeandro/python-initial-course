#Escribir una función que, dada una cantidad de fichas, calcule cuál es el  n  (valor máximo) de las fichas. Si el número de fichas no corresponde a la cantidad de fichas de ningún juego de dominó completo retornar -1.

def valMax(x):
    c = 1
    va = 0
    vm = 0


    while va <= x:
        
        for a in range(c):
            va += c
            
        c += 1
    
    print(va)
    
    
n = int(input("Cantidad de fichas?"))
valMax(n)


