import flet as ft
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Views.Home import main as Home

def interlude_page(page: ft.Page):
    page.window.maximizable = False
    page.window.maximized = True
    page.title = "SonicBurger - Interlude"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  
    page.window.width = 1080
    page.window.height = 1920
    page.window.resizable = False
    page.window.center()
    page.window.focused = True
    page.fullscreen = True 
    page.window.full_screen = True
    page.padding = 0

    def ir_home(e):
        page.clean()
        Home(page)
        page.update()

    bg = ft.Container(
        ft.Image(
            src="./assets/interlude/bg3.png",  
            fit=ft.ImageFit.COVER,
            width=1080,
            height=1920,    
        )
    )

    button_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10),
        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
    )

    botao_entrar = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Text("Correr"),
            margin=ft.margin.only(top=10)  # Ajustei a margem para ficar mais equilibrado
        ),
        on_click=ir_home,
        width=250,
        height=100,
        bgcolor=ft.Colors.RED_900,
        color=ft.Colors.WHITE,
        style=button_style
    )

    # Usando Column para centralizar o botão no final da tela
    safe = ft.Stack(
        controls=[
            bg,
            ft.Row([ft.Column(
                controls=[botao_entrar],
                alignment=ft.MainAxisAlignment.CENTER,  # Posiciona no final verticalmente
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente
                expand=True  # Faz a coluna ocupar todo o espaço disponível
            )],alignment=ft.MainAxisAlignment.CENTER,  # Posiciona no final verticalmente
                vertical_alignment=ft.CrossAxisAlignment.END, expand=True)
        ]
    )
    page.add(safe)

ft.app(target=interlude_page)