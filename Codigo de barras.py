#Realizar un programa para controlar el sistema de impresión de etiquetas con códigos de barras en un supermercado. Primero se debe ingresar la cantidad de productos diferentes que necesitan etiquetas. Luego, para cada producto, se ingresa el código a imprimir y la cantidad de veces que hay que imprimirlo. Posteriormente el programa imprimirá dicho código.

cant_productos = int(input("Ingrese cantidad de productos:"))

for a in range(cant_productos):
  codigo = int(input("Ingrese codigo de producto:"))
  cant_imprimir= int(input("Ingrese cantidad a imprimir:"))

  for x in range(cant_imprimir):
    print(codigo)