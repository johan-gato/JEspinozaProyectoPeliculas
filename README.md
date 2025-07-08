# 🎬 Regripeli - CRUD de Películas con Python y MySQL

## 📌 Descripción
**Regripeli** es una aplicación de consola desarrollada en Python que permite 
registrar, buscar, modificar y eliminar películas desde una base de datos MySQL (phpMyAdmin). 
Cuenta con validaciones completas y un menú simple y claro. 
Se conecta a la base de datos `bd_peliculas` y opera mediante una interfaz por consola intuitiva.

## 🧠 Funcionalidades
- ✅ Agregar nuevas películas.
- ✅ Mostrar todas, una o algunas películas.
- ✅ Buscar por ID.
- ✅ Modificar registros existentes.
- ✅ Eliminar películas por ID.
- ✅ Validaciones y mensajes de error claros.
- ✅ Menús estructurados.
- ✅ Conexión a MySQL totalmente funcional.

## 🗂 Estructura del Proyecto
```
ProyectoPeliculas/
│
├── dao/
│   ├── Conexion.py         # Conexión a MySQL (puerto 3308)
│   └── CRUDPelicula.py     # Funciones CRUD conectadas a la BD
│
├── dto/
│   └── Pelicula.py         # Clase Pelicula (DTO)
│
├── pelicula.py             # (Archivo no utilizado directamente)
└── main.py                 # Lógica del menú e interacción con el usuario
```

## 🛠 Requisitos
- Python 3.x
- MySQL (phpMyAdmin o WampServer)
- Librería `pymysql`  
  Instalar con:
  ```
  pip install pymysql
  ```

## 🧩 Base de Datos
**Nombre de la base de datos:** `bd_peliculas`  
**Tabla:** `pelicula`

| Campo             | Tipo        | Extra                                |
|------------------|-------------|--------------------------------------|
| id_pelicula      | INT         | PRIMARY KEY, AUTO_INCREMENT          |
| titulo_pelicula  | VARCHAR(45) |                                      |
| duracion         | INT         |                                      |
| fecha_de_estreno | DATE        |                                      |
| genero           | INT         | 1 = Terror, 2 = Ciencia Ficción, 3 = Drama |
| idioma           | INT         | 1 = Español, 2 = Inglés, 3 = Portugués |
| director         | VARCHAR(45) |                                      |

> ⚠️ **Puerto MySQL utilizado:** `3308` (modificable en `Conexion.py` si usas otro).

## 🚀 Cómo Ejecutar el Proyecto

1. Clona este repositorio o descarga los archivos.
2. Crea la base de datos `bd_peliculas` en phpMyAdmin y crea la tabla `pelicula` con los campos indicados.
3. Verifica la configuración de `Conexion.py` para que coincida con tu entorno local.
4. Abre una terminal en Visual Studio Code o consola.
5. Ejecuta el archivo principal:
   ```
   python main.py
   ```
6. Navega por el menú de opciones y utiliza el sistema.

## 📚 Menú Principal
```
1. Ingresar Película
2. Mostrar Películas
3. Modificar Película
4. Eliminar Película
5. Salir
```

## 📊 Submenú Mostrar
```
1. Mostrar Todos
2. Mostrar Uno
3. Mostrar Parcial
4. Volver
```

## ✅ Estado del Proyecto

| Funcionalidad           | Estado           |
|------------------------|------------------|
| Conexión a MySQL       | ✅ 100% Operativa |
| Insertar Películas     | ✅ Funcional      |
| Mostrar Películas      | ✅ Con formato en tabla |
| Modificar Registros    | ✅ Validado       |
| Eliminar Películas     | ✅ Validado       |
| Buscar por ID          | ✅ Con manejo de errores |
| Validaciones           | ✅ Aplicadas      |
| Manejo de errores      | ✅ Bien implementado |

## 💡 Mejoras Extra Incluidas
- Traducción de códigos (género e idioma) a texto legible.
- Fechas con formato legible: `"11 de noviembre de 2015"` en lugar de `2015-11-11`.
- Diseño tipo tabla al mostrar los datos en consola.
- Mensajes de advertencia amigables para el usuario.

## 👨‍💻 Autor
**Johan Espinoza**  
Estudiante de Ingeniería en Telecomunicaciones - INACAP  
Proyecto desarrollado para la Evaluación EVA4

---

## 📝 Licencia
Este proyecto es de uso académico. Puedes estudiarlo, modificarlo y adaptarlo libremente para fines educativos.
