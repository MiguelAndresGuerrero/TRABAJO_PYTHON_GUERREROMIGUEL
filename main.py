#importaciones del json y de la fecha y hora actual
import json
from datetime import datetime

#Conexion del Json general
def abrirArchivo():
    with open("info.json", "r") as openfile:
        return json.load(openfile)

def guardarArchivo(data):
    with open("info.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

#Json que se genera despues de ralizar una compra
def guardarCompras(compras):
    with open("compras.json", "w") as outfile:
        json.dump(compras, outfile, indent=4)

def cargarCompras():
    try:
        with open("compras.json", "r") as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        return []

compras = cargarCompras()

#Bienvenida al usuario
Name = input("Bienvenido usuario, ¿Como te llamas? ")
print("Bienvenido Usuario", Name)

#Login de 3 tipos de Usuarios
print("¿Cómo quieres ingresar?")
print("""
        1. Cliente
        2. Moderador
        3. Propietario
    """)
Rango = int(input("¿Cuál es tu forma de acceso? "))

#Guardamos la fecha y hora cuando se haga la compra
def registrar_compra(producto, precio):
    fecha_compra = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    compra = {
        "producto": producto,
        "precio": precio,
        "fecha": fecha_compra
    }
    compras.append(compra)
    guardarCompras(compras)
    print(f"Has comprado {producto} por {precio}")
    print(f"Fecha de compra: {fecha_compra}")

#menu de los productos
def productos(grupo):
    print("Tienda:", grupo["Tienda"])
    for producto in grupo["Productos"]:
        print("/////////////////////////////////////")
        print("ID del producto:", producto["id"])
        print("Nombre:", producto["producto"])
        print("Precio:", producto["precio"])
        print("/////////////////////////////////////")

#menu de modificacion del producto
def modificar_producto(grupo):
    productos_id = int(input("Ingrese el ID del producto que desea modificar: "))
    for producto in grupo["Productos"]:
        if producto["id"] == productos_id:
            opcion = int(input("""
                ¿Qué desea modificar del producto?
                1. Nombre del producto
                2. Precio del producto
                """))
            if opcion == 1:
                producto["producto"] = input("Nuevo nombre del producto: ")
            elif opcion == 2:
                producto["precio"] = input("Nuevo precio del producto: ")
            elif opcion == 0:
                print("Opción inválida.")
                return
            guardarArchivo(data)
            print("Cambio realizado.")
            return
    print("No se encontró ningún producto con ese ID")


def comprar_producto(data):
    print("Lista de tiendas:")
    for i, grupo in enumerate(data):
        print(f"{i+1}. {grupo['Tienda']}")
    tienda_id = int(input("Seleccione el ID de la tienda donde desea comprar: ")) - 1
    if 0 <= tienda_id < len(data):
        tienda = data[tienda_id]
        productos(tienda)
        producto_id = int(input("Ingrese el ID del producto que desea comprar: "))
        for producto in tienda["Productos"]:
            if producto["id"] == producto_id:
                registrar_compra(producto["producto"], producto["precio"])
                return
        print("No se encontró ningún producto con ese ID.")
    else:
        print("ID de tienda inválido.")

#menu de interaccion con el cliente
def menu_cliente(data):
    while True:
        print("****************************")
        print("      MENU DEL CLIENTE      ")
        print("****************************")
        print("1. Revisar productos")
        print("2. Comprar producto")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            for grupo in data:
                productos(grupo)
                
        elif opcion == "2":
            comprar_producto(data)
                
        elif opcion == "3":
            print("Gracias por usar el programa")
            break
        
        else:
            print("Opción inválida.")

#menu del moderador
def menu_moderador(data):
    while True:
        print("............................")
        print("      MENU DEL MODERADOR     ")
        print("............................")
        print("1. Revisar productos")
        print("2. Modificar productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            for grupo in data:
                productos(grupo)
                
        elif opcion == "2":
            for grupo in data:
                print(f"Tienda: {grupo['Tienda']}")
                modificar_producto(grupo)
                
        elif opcion == "3":
            print("Gracias por usar el programa")
            break
        
        else:
            print("Opción inválida.")

#Informe de ventas
def generar_informe():
    total_ingresos = 0
    print("============================")
    print("     INFORME DE VENTAS      ")
    print("============================")
    for compra in compras:
        print(f"Producto: {compra['producto']}, Precio: {compra['precio']}, Fecha: {compra['fecha']}")
        # Extraer solo el número del precio y convertirlo a entero
        precio_numerico = int(compra['precio'].split()[0])
        total_ingresos += precio_numerico
    print("============================")
    print(f"Total de ingresos: {total_ingresos} COP")
    print("============================")

#menu del proprietario
def menu_propietario(data):
    while True:
        print("-----------------------------")
        print("      MENU DE PROPIETARIO    ")
        print("-----------------------------")
        print("1. Revisar productos")
        print("2. Modificar productos")
        print("3. Ver registro de compras")
        print("4. Generar informe de ventas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            for grupo in data:
                productos(grupo)
                
        elif opcion == "2":
            for grupo in data:
                print(f"Tienda: {grupo['Tienda']}")
                modificar_producto(grupo)
                
        elif opcion == "3":
            print("Registro de compras:")
            for compra in compras:
                print(f"Producto: {compra['producto']}, Precio: {compra['precio']}, Fecha: {compra['fecha']}")
                
        elif opcion == "4":
            generar_informe()
                
        elif opcion == "5":
            print("Gracias por usar el programa")
            break
        
        else:
            print("Opción inválida.")

data = abrirArchivo()

if Rango == 1:
    menu_cliente(data)
elif Rango == 2:
    menu_moderador(data)
elif Rango == 3:
    menu_propietario(data)
else:
    print("Opción de acceso inválida")

#Creado por Miguel Guerrero C.C 1090381839