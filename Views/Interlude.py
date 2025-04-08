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

    texto=ft.Text("Correr", size=58)

    running_icon = ft.Icon(name=ft.Icons.DIRECTIONS_RUN, color=ft.Colors.WHITE, size=58)
    running_icon.margin =  ft.margin.only(top=40)
    
    botao_entrar = ft.ElevatedButton(
        content=ft.Container(
            content=texto,
            margin=ft.margin.only(top=0)  
        ),
        on_click=ir_home,
        width=450,
        height=100,
        bgcolor=ft.Colors.RED_900,
        color=ft.Colors.WHITE,
        style=button_style
        
    )

    safe = ft.Stack(
        controls=[
            bg,
            ft.Column(
                controls=[
                    ft.Container(ft.Container(margin= ft.margin.only(top=660), expand=True)),  # Espaço vazio para empurrar o botão para baixo
                    ft.Row(
                        controls=[ft.Stack([ft.Container(botao_entrar),ft.Container(content= running_icon, margin=ft.margin.only(top=20,left=40))])],
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza horizontalmente
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,  # Alinha o conteúdo no final da coluna
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Garante que a coluna esteja centralizada
            )
        ],
        width=1080,
        height=1920        
    )

    page.add(safe)

ft.app(target=interlude_page)