# views/home.py
import flet as ft
import os

# Adiciona o diretório raiz do projeto ao sys.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Importa a função main da tela de login
from Views.LoginPage import main as login_main

def main(page: ft.Page):
    page.title = "Sonic Burgers Kiosk"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.AMBER_100
    page.window.width = 1080
    page.window.height = 1920
    page.window.resizable = False
    page.window.center()
    page.window.maximizable = False
    
    def entrar_convidado(e):
        page.clean()
        page.add(ft.Text("Entering as guest..."))
        page.update()
    
    def criar_conta(e):
        page.clean()
        page.add(ft.Text("Redirecting to account creation..."))
        page.update()
    
    def ir_para_login(e):
        page.clean()
        login_main(page)
        page.update()
    
    button_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10),
        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
    )

    icon_tails = ft.GestureDetector(
        content=ft.Image(src="../assets/Start_Page/icon_tails.png", width=300, height=300),
        on_tap=entrar_convidado 
    )

    icon_knuckles = ft.GestureDetector(
        content=ft.Image(src="../assets/Start_Page/icon_knuckles.png", width=200, height=200),
        on_tap=ir_para_login
    )


    icon_knuckles_with_margin = ft.Container(
        content=icon_knuckles,
        margin=ft.margin.only(left=50, top=50)
    )

    icon_sonic = ft.GestureDetector(
        content=ft.Image(src="../assets/Start_Page/icon_sonic.png", width=100, height=100),
        on_tap=criar_conta  
    )   
    

    botao_convidado = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Text("Guest Login"),
            margin=ft.margin.only(top=100)  # Margin aplicada no Container
        ),
        on_click=entrar_convidado,
        width=300,
        height=400,
        bgcolor=ft.Colors.AMBER_500,
        color=ft.Colors.WHITE,
        style=button_style
    )
    botao_criar_conta = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Text("Create Account"),
            margin=ft.margin.only(left=70)  # Margin aplicada no Container
        ),
        on_click=criar_conta,
        width=250,
        height=100,
        bgcolor=ft.Colors.BLUE_900,
        color=ft.Colors.WHITE,
        style=button_style
    )
    
    botao_login = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Text("Login"),
            margin=ft.margin.only(top=100),  # Margin aplicada no Container
        ),
        on_click=ir_para_login,
        width=300,
        height=400,
        bgcolor=ft.Colors.RED_900,
        color=ft.Colors.WHITE,
        style=button_style
    )
    
    logo = ft.Image(src="../assets/icons/MainLogo.png", height=650, width=650)
    
    # Main column containing all elements
    main_column = ft.Column(
        [
            ft.Container(
                content=logo,  # Logo dentro do Container
                margin=ft.margin.only(top=-300,bottom=-170) # Adiciona margem negativa para mover a logo para cima
            ),
            ft.Row(
                [ft.Stack(controls=[botao_convidado,icon_tails]), ft.Stack(controls=[botao_login,icon_knuckles_with_margin])],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=100
            ),
            ft.Row(
                [ft.Stack(controls=[botao_criar_conta,icon_sonic])],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.START,  # Mantém alinhamento no topo (START)
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=50  # Mantém o espaçamento entre os elementos
    )



    
    # Container to hold everything
    container = ft.Container(
        content=main_column,
        alignment=ft.alignment.top_center,  # Changed to top_center
        padding=ft.padding.only(top=200),  # Adds 200px padding from the top
        width=1080,
        height=1920
    )
    
    page.add(container)
    page.update()

