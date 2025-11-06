import tkinter as tk
from login_view import LoginApp
from products_view import ProductsApp
from user_view import UserApp


class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Aplicación')
        self.root.geometry('900x600')

        # container frame where views will be swapped
        self.container = tk.Frame(self.root)
        self.container.pack(fill='both', expand=True)

        # Inicia con la vista de usuarios (UserApp) y le indica que es la vista inicial
        self.show_users(username='admin', is_initial_view=True) 

    def clear_container(self):
        for child in self.container.winfo_children():
            child.destroy()

    def show_login(self, username_after_logout=None):
        self.clear_container()
        self.login_view = LoginApp(self.container, on_login=self.on_login)
        self.login_view.pack(fill='both', expand=True)

    def on_login(self, username):
        # después de login, muestra la vista de productos
        self.clear_container()
        # Cuando viene de login, is_initial_view no se pasa, o se asume False
        self.products_view = ProductsApp(self.container, username, on_logout=self.on_logout, on_show_users=self.show_users)
        self.products_view.pack(fill='both', expand=True)

    # Añadimos el parámetro is_initial_view con valor por defecto False
    def show_users(self, username=None, is_initial_view=False): 
        # muestra la vista de gestión de usuarios
        self.clear_container()
        
        logout_action = self.on_logout

        # MODIFICACIÓN: Pasamos el parámetro is_initial_view a UserApp
        self.user_view = UserApp(self.container, 
                                 username or 'admin', 
                                 on_logout=logout_action,
                                 is_initial_view=is_initial_view) 
        self.user_view.pack(fill='both', expand=True)

    def on_logout(self):
        # Función de logout universal: regresa a login
        self.show_login()


def main():
    app = AppController()
    app.root.mainloop()


if __name__ == '__main__':
    main()