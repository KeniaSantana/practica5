
import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de secion"
    page.padding = 20

    titulo = ft.Text(
        "Inicia Sesion",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
        
    )
    nombre=ft.TextField(
    label="Nombre",
    hint_text="Ingresa tu nombre",
)
    correo=ft.TextField(
    label="Correo",
    hint_text="Ingresa tu correo",
)

    password=ft.TextField(
    label="Contraseña",
    hint_text="Ingresa tu contraseña",
    password=True,
    can_reveal_password=True,

)
    boton=ft.ElevatedButton(
    text="Guardar",
    icon=ft.Icons.SAVE,
    color=ft.Colors.WHITE,
)


ft.app(main)