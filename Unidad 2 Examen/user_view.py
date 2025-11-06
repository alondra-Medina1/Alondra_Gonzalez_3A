import tkinter as tk
from tkinter import messagebox, ttk
from user_controlller import ver_usuarios, agregar_usuarios, actualizar_usuarios, eliminar_usuarios


class UserApp(tk.Frame):
    # Añadimos el parámetro is_initial_view
    def __init__(self, parent, username, on_logout=None, is_initial_view=False, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.username = username
        self.on_logout = on_logout
        self.is_initial_view = is_initial_view # Guardamos el estado

        self.crear_elementos()
        self.load_usuarios()

    def crear_elementos(self):
        tk.Label(self, text=f"Hola, {self.username}",  font=("Arial", 22, "bold")).pack(pady=10)
        
        # LÓGICA DEL BOTÓN: Muestra "Iniciar sesión" si es la vista inicial
        if self.is_initial_view:
            tk.Button(self, text="Iniciar sesión", width=15, command=self.cerrar_sesion).pack(pady=20, padx=10)
        else:
            tk.Button(self, text="Cerrar sesión", width=15, command=self.cerrar_sesion).pack(pady=20, padx=10)


        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar usuarios", width=20, command=self.agregar_usuarios).pack(pady=6)
        tk.Button(frame_botones, text="Actualizar usuarios", width=20, command=self.actualizar_usuarios).pack(pady=6)
        tk.Button(frame_botones, text="Eliminar usuarios", width=20, command=self.eliminar_usuarios).pack(pady=6)

        tk.Label(self, text=f"Lista de usuarios",  font=("Arial", 26, "bold")).pack(pady=10)

        #CREAR TABLA CON TREEVIEW
        self.tree = ttk.Treeview(self, columns=("ID", "Usuario"), show="headings", height=10)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

    def load_usuarios(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        usuarios = ver_usuarios()
        for u in usuarios:
            self.tree.insert("", tk.END, values=u)

    def agregar_usuarios(self):
        ventana = tk.Toplevel(self)
        ventana.title("Agregar Usuario")
        ventana.geometry("300x200")
        tk.Label(ventana, text="Usuario").pack(pady=5)
        entry_user = tk.Entry(ventana)
        entry_user.pack(pady=5)
        tk.Label(ventana, text="Contraseña").pack(pady=5)
        entry_pass = tk.Entry(ventana, show="*")
        entry_pass.pack(pady=5)

        def guardar():
            u = entry_user.get().strip()
            p = entry_pass.get().strip()
            if not u or not p:
                messagebox.showwarning("Campos vacíos", "Ingrese usuario y contraseña.")
                return
            if agregar_usuarios(u, p):
                messagebox.showinfo("Éxito", f"Usuario {u} creado correctamente.")
                self.load_usuarios()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo crear el usuario.")

        tk.Button(ventana, text="crear usuario", command=guardar).pack(pady=10)

    def actualizar_usuarios(self):
        ventana = tk.Toplevel(self)
        ventana.title("Actualizar Usuario")
        ventana.geometry("320x240")
        tk.Label(ventana, text="ID del Usuario a actualizar").pack(pady=5)
        entry_id = tk.Entry(ventana)
        entry_id.pack(pady=5)
        tk.Label(ventana, text="Nuevo Usuario").pack(pady=5)
        entry_user = tk.Entry(ventana)
        entry_user.pack(pady=5)
        tk.Label(ventana, text="Nueva Contraseña").pack(pady=5)
        entry_pass = tk.Entry(ventana, show="*")
        entry_pass.pack(pady=5)

        def actualizar():
            id_u = entry_id.get().strip()
            new_u = entry_user.get().strip()
            new_p = entry_pass.get().strip()
            if not id_u or not new_u or not new_p:
                messagebox.showwarning("Campos vacíos", "Ingrese ID, nuevo usuario y nueva contraseña.")
                return
            
            try:
                id_v = int(id_u)
            except ValueError:
                messagebox.showwarning("Tipo incorrecto", "ID debe ser un número entero.")
                return

            if actualizar_usuarios(id_v, new_u, new_p):
                messagebox.showinfo("Éxito", f"Usuario ID {id_u} actualizado correctamente.")
                self.load_usuarios()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el usuario.")

        tk.Button(ventana, text="Actualizar usuario", command=actualizar).pack(pady=10)

    def eliminar_usuarios(self):
        ventana = tk.Toplevel(self)
        ventana.title("Eliminar Usuario")
        ventana.geometry("300x150")
        tk.Label(ventana, text="ID del Usuario a eliminar").pack(pady=5)
        entry_id = tk.Entry(ventana)
        entry_id.pack(pady=5)

        def eliminar():
            id_u = entry_id.get().strip()
            if not id_u:
                messagebox.showwarning("Campo vacío", "Ingrese ID del usuario a eliminar.")
                return
            
            try:
                id_v = int(id_u)
            except ValueError:
                messagebox.showwarning("Tipo incorrecto", "ID debe ser un número entero.")
                return

            if eliminar_usuarios(id_v):
                messagebox.showinfo("Éxito", f"Usuario ID {id_u} eliminado correctamente.")
                self.load_usuarios()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario.")

        tk.Button(ventana, text="Eliminar usuario", command=eliminar).pack(pady=10)

    def cerrar_sesion(self):
        if callable(self.on_logout):
            # Llama a la acción de logout del AppController, que nos lleva a show_login()
            self.on_logout() 
        else:
            try:
                self.master.destroy()
            except Exception:
                pass