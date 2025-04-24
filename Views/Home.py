# views/home.py
import flet as ft
import os
import sys

# Configura o caminho para importar módulos de outras pastas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

def main(page: ft.Page):
    # Funções de navegação
    def entrar_convidado(e):
        """Navega para modo convidado"""
        page.go("/tipo_pedido")  # Sugestão: criar uma rota específica para guest
    
    def criar_conta(e):
        """Navega para página de cadastro"""
        page.go("/sign")
    
    def ir_para_login(e):
        """Navega para página de login"""
        page.go("/login")
    
    # Estilo dos botões
    button_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10),
        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
    )

    # Ícones interativos
    icon_tails = ft.GestureDetector(
        content=ft.Image(src="assets/Start_Page/icon_tails.png", width=300, height=300),
        on_tap=entrar_convidado 
    )

    icon_knuckles = ft.GestureDetector(
        content=ft.Image(src="assets/Start_Page/icon_knuckles.png", width=200, height=200),
        on_tap=ir_para_login
    )

    icon_knuckles_with_margin = ft.Container(
        content=icon_knuckles,
        margin=ft.margin.only(left=50, top=50)
    )

    icon_sonic = ft.GestureDetector(
        content=ft.Image(src="assets/Start_Page/icon_sonic.png", width=100, height=100),
        on_tap=criar_conta  
    )   
    
    # Botões
    botao_convidado = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Text("Login Convidado"),
            margin=ft.margin.only(top=100) 
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
            content=ft.Text("Criar Conta"),
            margin=ft.margin.only(left=70,)  
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
            margin=ft.margin.only(top=100), 
        ),
        on_click=ir_para_login,
        width=300,
        height=400,
        bgcolor=ft.Colors.RED_900,
        color=ft.Colors.WHITE,
        style=button_style
    )
    
    # Logo
    logo = ft.Image(src="assets/icons/MainLogo.png", height=750, width=750)
    
    # Layout principal
    main_column = ft.Column(
        [
            ft.Container(
                content=logo,  
                margin=ft.margin.only(top=-500, bottom=-250) 
            ),
            ft.Row(
                [
                    ft.Stack(controls=[botao_convidado, icon_tails]), 
                    ft.Stack(controls=[botao_login, icon_knuckles_with_margin])
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=100
            ),
            ft.Row(
                [ft.Stack(controls=[botao_criar_conta, icon_sonic])],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=50  
    )
    
    # Container principal
    container = ft.Container(
        content=main_column,
        alignment=ft.alignment.top_center,  
        padding=ft.padding.only(top=200), 
        width=1080,
        height=1920
    )
    
    # Retorna a view em vez de adicionar diretamente
    return ft.View(
        route="/",
        controls=[container],
        bgcolor=ft.Colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )

if __name__ == "__main__":
    ft.app(target=main)