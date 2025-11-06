import tkinter as tk
from tkinter import messagebox
from auth_controller import validar_credenciales


class LoginApp(tk.Frame):
    def __init__(self, parent, on_login, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.on_login = on_login

        #Encabezado
        tk.Label(self, text="Bienvenido al sistema", font=("Arial", 16, "bold")).pack(pady=16)

        # Campos de texto
        tk.Label(self, text="Ingresa tu nombre de usuario:").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Ingresa tu contraseña:").pack()
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Iniciar sesión", command=self.login).pack(pady=20)

    def login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showinfo("Faltan datos", "Favor de ingresar usuario y contraseña")
            return

        if validar_credenciales(usuario, password):
            messagebox.showinfo("Acceso permitido", f"Bienvenido {usuario}")
            # notify controller
            if callable(self.on_login):
                self.on_login(usuario)
        else:
            messagebox.showerror("Acceso denegado", "Tus datos son incorrectos, no se pudo ingresar.")