import flet as ft

def main(page: ft.Page):

    page.title = "Inicio de Sesión"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    USUARIO_VALIDO = "Ale"
    CONTRASENA_VALIDA = "12345678"

    def mostrar_panel():

        contenido = ft.Column(
            [
                ft.Text("Bienvenido al sistema.", size=20),
                ft.Text("Has iniciado sesión correctamente.")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )

        page.clean()

        page.appbar = ft.AppBar(
            title=ft.Text("Panel principal"),
            bgcolor=ft.Colors.PINK_500
        )

        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.HOME,
                    label="Inicio"
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.INFO,
                    label="Información"
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.PERSON,
                    label="Inicio de sesión"
                ),
            ]
        )

        page.add(contenido)
        page.update()


    def login_click(e):
        usuario = txt_usuario.value
        contrasena = txt_contrasena.value

        if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
            mostrar_panel()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Usuario o contraseña incorrectos"))
            page.snack_bar.open = True
            page.update()

    def forgot_click(e):
        page.snack_bar = ft.SnackBar(
            ft.Text("Se han enviado instrucciones a tu correo electrónico")
        )
        page.snack_bar.open = True
        page.update()


    usuario = ft.TextField(
        label="Usuario",
        width=300,
        prefix_icon=ft.Icons.PERSON
    )

    contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        width=300,
        prefix_icon=ft.Icons.LOCK
    )

    login = ft.ElevatedButton(
        "Iniciar Sesión",
        on_click=login_click,
        width=200
    )

    forgot = ft.TextButton(
        "¿Olvidaste tu contraseña?",
        on_click=forgot_click
    )


    page.add(
        ft.Column(
            [
                ft.Icon(ft.Icons.PERSON, size=80),
                ft.Text("Iniciar Sesión", size=30, weight=ft.FontWeight.BOLD),
                usuario,
                contraseña,
                login,
                forgot,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            expand=True
        )
    )

ft.app(target=main)