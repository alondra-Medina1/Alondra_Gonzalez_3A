import tkinter as tk
from tkinter import messagebox, ttk
from products_controller import (ver_productos, agregar_productos, actualizar_productos, eliminar_productos)


class ProductsApp(tk.Frame):
    def __init__(self, parent, username, on_logout=None, on_show_users=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.username = username
        self.on_logout = on_logout
        self.on_show_users = on_show_users

        self.crear_elementos()
        self.ver_productos()

    def crear_elementos(self):
        tk.Label(self, text=f"Hola, {self.username}", font=("Arial", 22, "bold")).pack(pady=10)
        tk.Button(self, text="Cerrar sesión", width=0, command=self.cerrar_sesion).pack(pady=10, padx=10)

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar producto", width=20, command=self.agregar_producto).pack(pady=8, padx=5)
        tk.Button(frame_botones, text="Actualizar producto", width=20, command=self.actualizar_producto).pack(pady=8, padx=5)
        tk.Button(frame_botones, text="Eliminar producto", width=20, command=self.eliminar_producto).pack(pady=8, padx=5)
        tk.Button(frame_botones, text="Ver usuarios", width=20, command=self.show_users).pack(pady=8, padx=5)

        tk.Label(self, text="Lista de productos", font=("Arial", 26, "bold")).pack(pady=10)

        # CREAR TABLA CON TREEVIEW: ID, Nombre, Precio, Stock
        self.tree = ttk.Treeview(self, columns=("ID", "Nombre", "Precio", "Stock"), show="headings", height=12)
        self.tree.heading("ID", text="ID Producto")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Stock", text="Stock")
        self.tree.column("Nombre", width=350)
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

    def ver_productos(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # MANEJO DE ERRORES: Añadido para capturar fallos de conexión/consulta
        try:
            productos = ver_productos()
            for p in productos:
                # p debe ser (id_producto, nombre_producto, precio, stock)
                self.tree.insert("", tk.END, values=p)
        except Exception as e:
            messagebox.showerror("Error al cargar productos", 
                                 f"Ocurrió un error al intentar cargar los datos. Verifique la base de datos. Detalle: {e}")

    def agregar_producto(self):
        ventana = tk.Toplevel(self)
        ventana.title("Agregar Producto")
        ventana.geometry("400x420")

        tk.Label(ventana, text="Nombre").pack(pady=3)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Descripción").pack(pady=3)
        entry_descripcion = tk.Entry(ventana)
        entry_descripcion.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Stock").pack(pady=3)
        entry_stock = tk.Entry(ventana)
        entry_stock.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Precio").pack(pady=3)
        entry_precio = tk.Entry(ventana)
        entry_precio.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Status").pack(pady=3)
        entry_status = tk.Entry(ventana)
        entry_status.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Marca").pack(pady=3)
        entry_marca = tk.Entry(ventana)
        entry_marca.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Proveedor").pack(pady=3)
        entry_proveedor = tk.Entry(ventana)
        entry_proveedor.pack(pady=3, fill="x", padx=10)

        def guardar():
            nombre = entry_nombre.get().strip()
            descripcion = entry_descripcion.get().strip()
            stock = entry_stock.get().strip()
            precio = entry_precio.get().strip()
            status = entry_status.get().strip()
            marca = entry_marca.get().strip()
            proveedor = entry_proveedor.get().strip()

            if not nombre or not precio or not stock:
                messagebox.showwarning("Campos vacíos", "Ingrese nombre, precio y stock del producto.")
                return

            try:
                stock_v = int(stock)
                precio_v = float(precio)
            except ValueError:
                messagebox.showwarning("Tipo incorrecto", "Stock debe ser entero y precio numérico.")
                return

            result = agregar_productos(nombre, descripcion, stock_v, precio_v, status, marca, proveedor)

            if isinstance(result, tuple):
                success, err = result
            else:
                success = bool(result)
                err = None

            if success:
                messagebox.showinfo("Éxito", f"Producto {nombre} creado correctamente.")
                self.ver_productos()
                ventana.destroy()
            else:
                msg = "No se pudo crear el producto."
                if err:
                    msg += f"\nDetalle: {err}"
                messagebox.showerror("Error", msg)

        tk.Button(ventana, text="Crear producto", command=guardar).pack(pady=12)

    def actualizar_producto(self):
        ventana = tk.Toplevel(self)
        ventana.title("Actualizar Producto")
        ventana.geometry("420x460")

        tk.Label(ventana, text="ID del Producto a actualizar").pack(pady=3)
        entry_id = tk.Entry(ventana)
        entry_id.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Nombre").pack(pady=3)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Descripción").pack(pady=3)
        entry_descripcion = tk.Entry(ventana)
        entry_descripcion.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Stock").pack(pady=3)
        entry_stock = tk.Entry(ventana)
        entry_stock.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Precio").pack(pady=3)
        entry_precio = tk.Entry(ventana)
        entry_precio.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Status").pack(pady=3)
        entry_status = tk.Entry(ventana)
        entry_status.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Marca").pack(pady=3)
        entry_marca = tk.Entry(ventana)
        entry_marca.pack(pady=3, fill="x", padx=10)

        tk.Label(ventana, text="Proveedor").pack(pady=3)
        entry_proveedor = tk.Entry(ventana)
        entry_proveedor.pack(pady=3, fill="x", padx=10)

        def actualizar():
            id_p = entry_id.get().strip()
            nombre = entry_nombre.get().strip()
            descripcion = entry_descripcion.get().strip()
            stock = entry_stock.get().strip()
            precio = entry_precio.get().strip()
            status = entry_status.get().strip()
            marca = entry_marca.get().strip()
            proveedor = entry_proveedor.get().strip()

            if not id_p or not nombre or not precio or not stock:
                messagebox.showwarning("Campos vacíos", "Ingrese ID, nombre, precio y stock.")
                return

            try:
                id_v = int(id_p)
                stock_v = int(stock)
                precio_v = float(precio)
            except ValueError:
                messagebox.showwarning("Tipo incorrecto", "ID y stock deben ser enteros; precio numérico.")
                return

            if actualizar_productos(id_v, nombre, descripcion, stock_v, precio_v, status, marca, proveedor):
                messagebox.showinfo("Éxito", f"Producto ID {id_v} actualizado correctamente.")
                self.ver_productos()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el producto.")

        tk.Button(ventana, text="Actualizar producto", command=actualizar).pack(pady=12)

    def eliminar_producto(self):
        ventana = tk.Toplevel(self)
        ventana.title("Eliminar Producto")
        ventana.geometry("320x160")
        tk.Label(ventana, text="ID del Producto a eliminar").pack(pady=8)
        entry_id = tk.Entry(ventana)
        entry_id.pack(pady=5)

        def eliminar():
            id_p = entry_id.get().strip()
            if not id_p:
                messagebox.showwarning("Campo vacío", "Ingrese ID del producto a eliminar.")
                return
            try:
                id_v = int(id_p)
            except ValueError:
                messagebox.showwarning("Tipo incorrecto", "ID debe ser un número entero.")
                return

            if eliminar_productos(id_v):
                messagebox.showinfo("Éxito", f"Producto ID {id_v} eliminado correctamente.")
                self.ver_productos()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto.")

        tk.Button(ventana, text="Eliminar producto", command=eliminar).pack(pady=10)

    def cerrar_sesion(self):
        if callable(self.on_logout):
            self.on_logout()
        else:
            try:
                self.master.destroy()
            except Exception:
                pass

    def show_users(self):
        if callable(self.on_show_users):
            self.on_show_users(self.username)