from DAO.Conexion import Conexion
from DTO.Pelicula import Pelicula

host = 'localhost'
user = 'root'
password = ''
db = 'bd_peliculas'

def agregar(p):
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO pelicula (titulo_pelicula, duracion, fecha_de_estreno, genero, idioma, director) VALUES ('{}', {}, '{}', {}, {}, '{}')".format(
            p.titulo, p.duracion, p.fecha, p.genero, p.idioma, p.director)
        con.ejecuta_query(sql)
        con.commit()
        con.desconectar()
        input("Película ingresada. Presione Enter.")
    except Exception as e:
        print("Error al agregar película:", e)

def eliminar(id_pelicula):
    try:
        con = Conexion(host, user, password, db)
        sql = "DELETE FROM pelicula WHERE id_pelicula={}".format(id_pelicula)
        con.ejecuta_query(sql)
        con.commit()
        con.desconectar()
        input("Película eliminada con exito. Presione Enter.")
    except Exception as e:
        print("Error al eliminar:", e)

def modificar(p, id_pelicula):
    try:
        con = Conexion(host, user, password, db)
        sql = "UPDATE pelicula SET titulo_pelicula='{}', duracion={}, fecha_de_estreno='{}', genero={}, idioma={}, director='{}' WHERE id_pelicula={}".format(
            p.titulo, p.duracion, p.fecha, p.genero, p.idioma, p.director, id_pelicula)
        con.ejecuta_query(sql)
        con.commit()
        con.desconectar()
        input("Película modificada. Presione Enter.")
    except Exception as e:
        print("Error al modificar:", e)

def mostrarTodos():
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM pelicula"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print("Error al mostrar todos:", e)

def mostrarUno(id_pelicula):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM pelicula WHERE id_pelicula={}".format(id_pelicula)
        cursor = con.ejecuta_query(sql)
        dato = cursor.fetchone()
        con.desconectar()
        return dato
    except Exception as e:
        print("Error al mostrar uno:", e)

def mostrarParcial(n):
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT * FROM pelicula"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(n)
        con.desconectar()
        return datos
    except Exception as e:
        print("Error al mostrar parcial:", e)
