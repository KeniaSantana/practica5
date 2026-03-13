import flet as ft

def main(page: ft.Page):
    
    page.title = "Inicio de Sesión"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    
    USUARIO_VALIDO = "admin"
    CONTRASENA_VALIDA = "123456"

    
    def login_click(e):
        usuario = txt_usuario.value
        contrasena = txt_contrasena.value

        if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
            page.show_dialog(
                ft.SnackBar(ft.Text("¡Inicio de sesión exitoso!"))
            )
        else:
            page.show_dialog(
                ft.SnackBar(ft.Text("Usuario o contraseña incorrectos."))
            )

    
    def forgot_click(e):
        page.show_dialog(
            ft.SnackBar(ft.Text("Se han enviado instrucciones a tu correo electrónico"))
        )

    
    txt_usuario = ft.TextField(
        label="Usuario",
        width=300,
        prefix_icon=ft.Icons.PERSON
    )

    txt_contrasena = ft.TextField(
        label="Contraseña",
        password=True,
        width=300,
        prefix_icon=ft.Icons.LOCK
    )

    
    btn_login = ft.ElevatedButton(
        "Iniciar Sesión",
        on_click=login_click,
        width=200
    )

    
    link_forgot = ft.TextButton(
        "¿Olvidaste tu contraseña?",
        on_click=forgot_click
    )

    
    page.add(
        ft.Column(
            [
                ft.Icon(ft.Icons.PERSON, size=80),
                ft.Text("Iniciar Sesión", size=30, weight=ft.FontWeight.BOLD),
                txt_usuario,
                txt_contrasena,
                btn_login,
                link_forgot,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


ft.app(target=main)