#Escriba un programa que imprima los números del 1 al 100, pero que para cada número que sea múltiplo de 3 imprima N3, para los múltiplos de 5 imprima N5, y para los múltiplos de los dos, N3N5.

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "N3N5")
    
    if i % 3 == 0 and not (i % 5 == 0):
        print(i, "N3")
            
    if i % 5 == 0 and not (i % 3 == 0):
        print(i, "N5")

    if not (i % 5 == 0) and not (i % 3 == 0):
        print(i)   
