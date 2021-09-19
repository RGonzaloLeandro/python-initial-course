def suma(a, b):
    s = a + b
    return s #para que sirve linea en este caso del ejemplo?... el resultado de la funcion se almacena en la variable s?... no se usa nunca esa variable

z = suma(3, 4)
print("3 + 4 =", z)

x = int(input("Ingrese el primer sumando: "))
y = int(input("Ingrese el segundo sumando: "))
z = suma(x, y)
print("x + y =", z)