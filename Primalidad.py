#PrimalidadEscribir una función que recibe un número y devuelve True si el número es primo y False en caso contrario.

#Mediante un for verificar la primalidad de los numeros del  1  al  20 , es decir, decidir si cada número es primo o no.

def primo(x):
    #if x%2 != 0 and x%(x**(0.5)) != 0:
    #    print (x, " es primo")
    #else:
    #    print (x, " no es primo")
    for r in range (2,int(x**(0.5))):
        if x%r == 0:
            print (x, " no es primo")
            return
            
    print(x, " es primo")


a = 0
while a == 0:

    numero = int(input())
    if numero == -1:
        a = 1

    primo(numero)
