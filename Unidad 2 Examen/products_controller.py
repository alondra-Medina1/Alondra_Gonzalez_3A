from database import crear_conexion

def ver_productos():
    conexion = crear_conexion()
    if not conexion:
        return []

    cursor = conexion.cursor()
    # CORRECCIÓN: Usar id_producto
    cursor.execute("SELECT id_producto, nombre_producto, precio, stock FROM productos")
    resultado = cursor.fetchall()
    conexion.close()
    return resultado


def agregar_productos(nombre_producto, descripcion, stock, precio, status, marca, proveedor):
    conexion = crear_conexion()
    if not conexion:
        return False, "No se pudo conectar a la base de datos."
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre_producto, descripcion, stock, precio, status, marca, proveedor) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (nombre_producto, descripcion, stock, precio, status, marca, proveedor),
        )
        conexion.commit()
        conexion.close()
        return True, None
    except Exception as e:
        # Devolver el error para que la vista pueda mostrar información más útil
        err = str(e)
        print(f"Error al crear un producto. Tipo de error: {err}")
        return False, err

def actualizar_productos(id_producto, nombre_producto, descripcion, stock, precio, status, marca, proveedor):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        # CORRECCIÓN: Usar id_producto en el WHERE
        cursor.execute(
            "UPDATE productos SET nombre_producto=%s, descripcion=%s, stock=%s, precio=%s, status=%s, marca=%s, proveedor=%s WHERE id_producto=%s",
            (nombre_producto, descripcion, stock, precio, status, marca, proveedor, id_producto),
        )
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al actualizar producto. Tipo de error: {e}")
        return False


def eliminar_productos(id_producto):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        # CORRECCIÓN: Usar id_producto
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al eliminar producto. Tipo de error: {e}")
        return False