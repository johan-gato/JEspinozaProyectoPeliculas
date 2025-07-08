import os
import DAO.CRUDPelicula
from DTO.Pelicula import Pelicula
from datetime import datetime

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def formatear_fecha(fecha):
    if isinstance(fecha, str):
        try:
            fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
        except:
            return fecha
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    return f"{fecha.day} de {meses[fecha.month - 1]} de {fecha.year}"

def traducir_genero(g):
    return {1: "Terror", 2: "Ciencia Ficción", 3: "Drama"}.get(g, "Desconocido")

def traducir_idioma(i):
    return {1: "Español", 2: "Inglés", 3: "Portugués"}.get(i, "Desconocido")

def menuPrincipal():
    limpiar_pantalla()
    print("================================")
    print("        MENÚ PRINCIPAL")
    print("================================")
    print("1.- Ingresar Película")
    print("2.- Mostrar Películas")
    print("3.- Modificar Película")
    print("4.- Eliminar Película")
    print("5.- Salir")
    print("================================")

def menuMostrar():
    limpiar_pantalla()
    print("================================")
    print("       MENÚ MOSTRAR")
    print("================================")
    print("1.- Mostrar Todas")
    print("2.- Mostrar Una")
    print("3.- Mostrar Parcial")
    print("4.- Volver")
    print("================================")

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except:
        return False

def ingresarDatos():
    limpiar_pantalla()
    print("=======================================")
    print("         INGRESAR PELÍCULA")
    print("=======================================")
    titulo = input("Título: ").strip()

    while True:
        duracion_str = input("Duración (minutos): ").strip()
        if duracion_str.isdigit() and int(duracion_str) > 0:
            duracion = int(duracion_str)
            break
        else:
            print("⚠️ Duración inválida.")

    while True:
        fecha = input("Fecha de estreno (AAAA-MM-DD): ").strip()
        if validar_fecha(fecha):
            break
        else:
            print("⚠️ Fecha inválida.")

    print("1 = Terror\n2 = Ciencia Ficción\n3 = Drama")
    while True:
        genero_str = input("Género: ").strip()
        if genero_str in ['1', '2', '3']:
            genero = int(genero_str)
            break
        else:
            print("⚠️ Género inválido.")

    print("1 = Español\n2 = Inglés\n3 = Portugués")
    while True:
        idioma_str = input("Idioma: ").strip()
        if idioma_str in ['1', '2', '3']:
            idioma = int(idioma_str)
            break
        else:
            print("⚠️ Idioma inválido.")

    director = input("Director: ").strip()

    p = Pelicula(titulo, duracion, fecha, genero, idioma, director)
    DAO.CRUDPelicula.agregar(p)
    print("Película ingresada. Presione Enter.")
    input()

def imprimir_tabla(peliculas):
    print("ID   Título                 Duración   Fecha                     Género           Idioma         Director")
    print("-------------------------------------------------------------------------------------------------------------")
    for d in peliculas:
        print(f"{str(d[0]).ljust(5)}{d[1].ljust(22)}{str(d[2]).ljust(10)}{formatear_fecha(d[3]).ljust(25)}"
              f"{traducir_genero(d[4]).ljust(17)}{traducir_idioma(d[5]).ljust(15)}{d[6]}")

def imprimir_lista_simple(peliculas):
    print("ID   Título")
    print("--------------------")
    for d in peliculas:
        print(f"{str(d[0]).ljust(5)}{d[1]}")

def mostrar():
    while True:
        menuMostrar()
        op = input("Ingrese una opción: ").strip()
        if op == '1':
            mostrarTodos()
        elif op == '2':
            mostrarUno()
        elif op == '3':
            mostrarParcial()
        elif op == '4':
            break
        else:
            print("⚠️ Opción inválida.")
            input("Presione Enter para continuar...")

def mostrarTodos():
    limpiar_pantalla()
    print("=======================================")
    print("         TODAS LAS PELÍCULAS")
    print("=======================================")
    datos = DAO.CRUDPelicula.mostrarTodos()
    if datos:
        imprimir_tabla(datos)
    else:
        print("📭 No hay películas registradas.")
    input("Presione Enter para continuar...")

def mostrarUno():
    limpiar_pantalla()
    print("=======================================")
    print("         BUSCAR PELÍCULA POR ID")
    print("=======================================")
    datos = DAO.CRUDPelicula.mostrarTodos()
    if not datos:
        print("📭 No hay películas registradas.")
        input("Presione Enter para continuar...")
        return

    # Mostrar lista simple para que usuario vea qué ID usar
    imprimir_lista_simple(datos)

    while True:
        id_str = input("Ingrese el ID de la película: ").strip()
        if id_str.isdigit():
            idp = int(id_str)
            dato = DAO.CRUDPelicula.mostrarUno(idp)
            if dato:
                limpiar_pantalla()
                print("=======================================")
                print("       INFORMACIÓN DE LA PELÍCULA")
                print("=======================================")
                imprimir_tabla([dato])
                break
            else:
                print("⚠️ Película no encontrada. Intente otro ID.")
        else:
            print("⚠️ Ingrese un número válido.")
    input("Presione Enter para continuar...")

def mostrarParcial():
    limpiar_pantalla()
    print("=======================================")
    print("       MOSTRAR ALGUNAS PELÍCULAS")
    print("=======================================")
    datos = DAO.CRUDPelicula.mostrarTodos()
    if not datos:
        print("📭 No hay películas registradas.")
        input("Presione Enter para continuar...")
        return
    max_cantidad = len(datos)
    while True:
        cant_str = input(f"¿Cuántas películas mostrar? (1 - {max_cantidad}): ").strip()
        if cant_str.isdigit():
            cantidad = int(cant_str)
            if 1 <= cantidad <= max_cantidad:
                datos_parcial = DAO.CRUDPelicula.mostrarParcial(cantidad)
                imprimir_tabla(datos_parcial)
                break
            else:
                print("⚠️ Número fuera de rango.")
        else:
            print("⚠️ Ingrese un número válido.")
    input("Presione Enter para continuar...")

def modificar():
    limpiar_pantalla()
    print("=======================================")
    print("        MODIFICAR UNA PELÍCULA")
    print("=======================================")
    datos = DAO.CRUDPelicula.mostrarTodos()
    if not datos:
        print("📭 No hay películas para modificar.")
        input("Presione Enter para continuar...")
        return
    imprimir_tabla(datos)
    while True:
        id_str = input("Ingrese el ID de la película a modificar: ").strip()
        if id_str.isdigit():
            idp = int(id_str)
            pelicula = DAO.CRUDPelicula.mostrarUno(idp)
            if pelicula:
                break
            else:
                print("⚠️ Película no encontrada. Intente otro ID.")
        else:
            print("⚠️ Ingrese un número válido.")

    titulo = input(f"Título actual ({pelicula[1]}): ").strip() or pelicula[1]

    while True:
        duracion_str = input(f"Duración actual ({pelicula[2]}): ").strip()
        if duracion_str == "":
            duracion = pelicula[2]
            break
        elif duracion_str.isdigit() and int(duracion_str) > 0:
            duracion = int(duracion_str)
            break
        else:
            print("⚠️ Duración inválida.")

    while True:
        fecha = input(f"Fecha actual ({pelicula[3]}): ").strip()
        if fecha == "":
            fecha = pelicula[3]
            break
        elif validar_fecha(fecha):
            break
        else:
            print("⚠️ Fecha inválida.")

    print("1 = Terror\n2 = Ciencia Ficción\n3 = Drama")
    while True:
        genero_str = input(f"Género actual ({pelicula[4]}): ").strip()
        if genero_str == "":
            genero = pelicula[4]
            break
        elif genero_str in ['1', '2', '3']:
            genero = int(genero_str)
            break
        else:
            print("⚠️ Género inválido.")

    print("1 = Español\n2 = Inglés\n3 = Portugués")
    while True:
        idioma_str = input(f"Idioma actual ({pelicula[5]}): ").strip()
        if idioma_str == "":
            idioma = pelicula[5]
            break
        elif idioma_str in ['1', '2', '3']:
            idioma = int(idioma_str)
            break
        else:
            print("⚠️ Idioma inválido.")

    director = input(f"Director actual ({pelicula[6]}): ").strip() or pelicula[6]

    p = Pelicula(titulo, duracion, fecha, genero, idioma, director)
    DAO.CRUDPelicula.modificar(p, idp)
    print("Película modificada. Presione Enter.")
    input()

def eliminarDatos():
    limpiar_pantalla()
    print("=======================================")
    print("         ELIMINAR UNA PELÍCULA")
    print("=======================================")
    datos = DAO.CRUDPelicula.mostrarTodos()
    if not datos:
        print("📭 No hay películas para eliminar.")
        input("Presione Enter para continuar...")
        return
    imprimir_tabla(datos)
    while True:
        id_str = input("Ingrese el ID de la película a eliminar: ").strip()
        if id_str.isdigit():
            idp = int(id_str)
            pelicula = DAO.CRUDPelicula.mostrarUno(idp)
            if pelicula:
                DAO.CRUDPelicula.eliminar(idp)
                print("Película eliminada correctamente.")
                break
            else:
                print("⚠️ Película no encontrada. Intente otro ID.")
        else:
            print("⚠️ Ingrese un número válido.")
    input("Presione Enter para continuar...")

while True:
    menuPrincipal()
    op = input("Ingrese una opción: ").strip()
    if op == '1':
        ingresarDatos()
    elif op == '2':
        mostrar()
    elif op == '3':
        modificar()
    elif op == '4':
        eliminarDatos()
    elif op == '5':
        salir = input("¿Desea salir? S/Sí o N/No: ").upper()
        if salir == "S":
            print("Hasta luego 👋")
            break
    else:
        print("⚠️ Opción inválida.")
        input("Presione Enter para continuar...")
