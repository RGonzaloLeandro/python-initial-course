#Adivina adivinador
#Ahora les proponemos a ustedes realizar el programa que adivine un número que ustedes elijan, indicándole si los números que este propone son mayores o menores al elegido.

#Ustedes pensarán en un número secreto (para este ejercicio consideremos que el número es menor a 10.000), luego el programa intenta adivinarlo. El usuario debe responder con el símbolo > , < ó = . En el caso de ser igual, el programa termina e imprime la cantidad de intentos que tardó, caso contrario, debe volver a intentar adivinar el número y se repite el procedimiento.

#Desafío: Encontrar la estrategia que puede ejecutar la máquina para adivinar el número en la menor cantidad de intentos posible.

print ("pensa un numero del 1 al 10.000")

rango_dwn = 0
rango_up = 10000
numero = 0
c = 0
while numero == 0:

    rango = int((rango_up + rango_dwn)/2)
    respuesta = input ("El numero es mayor o menor que " + str(rango) + "?")
    
    if respuesta == ">":
        rango_dwn = rango

    if respuesta == "<":
        rango_up = rango

    c += 1

    if respuesta == "=":
        print("Acerté en", c, " intentos!")
        numero = rango
