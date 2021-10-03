#Crear un programa en el cual el usuario ingresa un string y dos índices numéricos. El programa debe crear una lista a partir de las letras del string, luego intercambiar dos letras de lugar a partir de los índices indicados por el usuario. Por último debe combinar las letras de la lista nuevamente en un string e imprimir el resultado. Si los índices son inválidos mostrar un mensaje de error.

palabra = str(input("Palabra? "))
lista = [x for x in palabra]
#print (lista)

i1 = int(input("Indice 1? "))
i2 = int(input("Indice 2? "))

if i1 < 0 or i2 < 0 or i1 > len(lista) or i2 > len(lista):
    print ("error")

else:
    lista[i1], lista[i2] = lista[i2], lista[i1]
    #print (lista)

    texto = "".join( lista )
    print (texto.capitalize())