import os

biblioteca = []

def registrar():
    try:
        nombre = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        publicacion = input("Ingrese el año de publicacion del libro: ")
        sku = input("ingrese el codigo del libro")
            
           
        
        libro = {
            "Nombre": nombre,
            "Autor": autor,
            "Publicacion": publicacion,
            "SKU": sku,
        }

        biblioteca.append(libro)
        print("Registro de libro con exito")

    except ValueError as e:
        print(e)

def prestar():
    try:
        usuario = input("Ingresa tu nombre de usuario: ")
        sku = input("Ingrese el codigo del libro: ")

        if usuario < sku:
            raise ValueError("El libro no exite o Esta prestado")
        
        prestamo = {
            "Usuario": usuario,
            "SKU": sku,
        }

        biblioteca.append(prestar)
        print("Prestamo con exito")

    except ValueError as e:
        print(e)

def listar():
    if not biblioteca:
        print("No hay libro resgistrado.")
        return
    for libro in biblioteca:
        print(f"Nombre: {libro['nombre']}\tAutor: {libro['autor']}\tPublicacion: {libro['publicacion']}\tsku: {libro['sku']}")
    
def imprimir():
    op = int(input("desea imprimir planilla"))
    filename = "prestamo.txt"





def menu():
    while True:
        try:
            print("\n*** MENU ***\n")
            print("1. Registrar libro\n2. Prestar libro\n3. Lista de libro\n4. Imprimir planilla de libro en prestamo\n5. Salir del programa")
            op = int(input("Ingrese una opcion: "))

            if op == 1:
                registrar()
            elif op == 2:
                prestar()
            elif op == 3:
                listar()
            elif op == 4:
                imprimir()
            elif op == 4:
                print("Programa finalizando... Desarrollado por Fabian Oyarce Run: 21.703.383-7")
                break
            else:
                print("Opcion fuera de rango. Intelato nuevamente")
        except ValueError:
            print("Error en el tipo de dato ingresado. Intente nuevamente")
                      


