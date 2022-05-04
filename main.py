# Librerias.
from pymongo import MongoClient

# Datos conexion.
MONGO_URI = 'mongodb://localhost'
cliente = MongoClient(MONGO_URI)

# Creación base datos.
bd = cliente['BDPrueba']

# Creación colección.
coleccion = bd['ColeccionPrueba']

# Insertar un dato.
coleccion.insert_one({"Atributo": "Valor", "Atributo2": "Valor"})

# Insertar más de un dato.
# Crear objetos.
objeto1 = {"Atributo": "Valor", "Atributo2": "Valor"}
objeto2 = {"Atributo": "Valor", "Atributo2": "Valor"}

# Insertar objetos.
coleccion.insert_many([objeto1, objeto2])

# Buscar objeto.
consulta = coleccion.find()
for x in consulta:
    print(x)