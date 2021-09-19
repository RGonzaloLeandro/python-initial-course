#La leyenda de Filius Bonacci
#Imprima  n  números de la sucesión de Fibonacci..


cant = int(input(" Cantidad de numeros a imprimir:"))

a = 0
b = 1

print (a)
print (b)

for x in range (cant-2):
    c = a + b
    print (c)
    a = b
    b = c
    
