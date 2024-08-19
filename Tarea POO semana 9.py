class Producto:
    # Constructor de la clase Producto
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Método para obtener el ID del producto
    def get_id(self):
        return self.id

    # Método para obtener el nombre del producto
    def get_nombre(self):
        return self.nombre

    # Método para obtener la cantidad del producto
    def get_cantidad(self):
        return self.cantidad

    # Método para obtener el precio del producto
    def get_precio(self):
        return self.precio

    # Método para establecer la cantidad del producto
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    # Método para establecer el precio del producto
    def set_precio(self, precio):
        self.precio = precio

    # Método para obtener una representación en cadena del producto
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

class Inventario:
    # Constructor de la clase Inventario
    def __init__(self):
        self.productos = []

    # Método para añadir un producto al inventario
    def añadir_producto(self, producto):
        # Verifica si el producto ya existe en el inventario
        for prod in self.productos:
            if prod.get_id() == producto.get_id():
                print("Error: El ID ya existe.")
                return
        # Añade el producto si no existe
        self.productos.append(producto)
        print("Producto añadido con éxito.")

    # Método para eliminar un producto del inventario
    def eliminar_producto(self, id):
        # Busca el producto por ID y lo elimina si se encuentra
        for prod in self.productos:
            if prod.get_id() == id:
                self.productos.remove(prod)
                print("Producto eliminado con éxito.")
                return
        print("Error: Producto no encontrado.")

    # Método para actualizar un producto en el inventario
    def actualizar_producto(self, id, cantidad=None, precio=None):
        # Busca el producto por ID y actualiza los campos especificados
        for prod in self.productos:
            if prod.get_id() == id:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                print("Producto actualizado con éxito.")
                return
        print("Error: Producto no encontrado.")

    # Método para buscar productos por nombre
    def buscar_producto(self, nombre):
        # Filtra productos cuyo nombre contenga el texto dado
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if resultados:
            for prod in resultados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    # Método para mostrar todos los productos del inventario
    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for prod in self.productos:
                print(prod)

def menu():
    inventario = Inventario()

    while True:
        # Muestra las opciones del menú
        print("\n1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Todos los Productos")
        print("6. Salir")

        # Lee la opción seleccionada por el usuario
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no se desea cambiar): ")
            precio = input("Nuevo precio (dejar vacío si no se desea cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

menu()
