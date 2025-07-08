import os
from DTO.Pelicula import Pelicula
import DAO.CRUDPelicula as crud

def menuPrincipal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== PRINCIPAL ===")
    print("1. Ingresar Película")
    print("2. Mostrar Películas")
    print("3. Modificar Película")
    print("4. Eliminar Película")
    print("5. Salir")

def menuMostrar():
    print("=== MENÚ :)===")
    print("1. Mostrar Todos")
    print("2. Mostrar Uno")
    print("3. Mostrar Parcial")
    print("4. Volver")

def ingresar():
    print("=== Ingresar Película ===")
    titulo = input("Título de pelicula: ")
    duracion = int(input("Duración (en minutos): "))
    fecha = input("Fecha de estreno (año-mes-dia): ")
    genero = int(input("Género (1=Terror, 2=Ciencia Ficción, 3=Drama): "))
    idioma = int(input("Idioma (1=Español, 2=Inglés, 3=Portugués): "))
    director = input("Director: ")
    p = Pelicula(titulo, duracion, fecha, genero, idioma, director)
    crud.agregar(p)

def mostrar():
    while True:
        menuMostrar()
        op = input("Opciónes: ")
        if op == '1':
            datos = crud.mostrarTodos()
            for d in datos:
                print(d)
        elif op == '2':
            idp = int(input("ID de película: "))
            d = crud.mostrarUno(idp)
            print(d)
        elif op == '3':
            n = int(input("¿Cuántas películas quieres mostrar?: "))
            datos = crud.mostrarParcial(n)
            for d in datos:
                print(d)
        elif op == '4':
            break
        else:
            print("Opción inválida.")

def modificar():
    print("=== Listado de Película ===")
    datos=crud.mostrarTodos()
    for d in datos:
        print(d)
    print("------------------------------------------------------------------------")
    idp = int(input("ID de película a modificar: "))
    titulo = input("Nuevo título: ")
    duracion = int(input("Nueva duración: "))
    fecha = input("Nueva fecha (año-mes-dia): ")
    genero = int(input("Nuevo género (1=Terror, 2=C.Ficción, 3=Drama): "))
    idioma = int(input("Nuevo idioma (1=Español, 2=Inglés, 3=Portugués): "))
    director = input("Nuevo director: ")
    p = Pelicula(titulo, duracion, fecha, genero, idioma, director)
    crud.modificar(p, idp)

def eliminar():
    idp = int(input("ID de película a eliminar: "))
    crud.eliminar(idp)


while True:
    menuPrincipal()
    op = input("Opción: ")
    if op == '1':
        ingresar()
    elif op == '2':
        mostrar()
    elif op == '3':
        modificar()
    elif op == '4':
        eliminar()
    elif op == '5':
        print("adios👋")
        break
    else:
        print("Opción inválida.")