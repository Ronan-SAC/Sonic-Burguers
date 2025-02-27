import flet as ft

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
        page.add(ft.Text("Redirecting to login page..."))
        page.update()
    
    button_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10),
        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
    )
    
    botao_convidado = ft.ElevatedButton(
        text="Guest Login",
        on_click=entrar_convidado,
        width=300,
        height=400,
        bgcolor=ft.Colors.ORANGE_700,
        color=ft.Colors.WHITE,
        style=button_style
    )
    
    botao_criar_conta = ft.ElevatedButton(
        text="Create Account",
        on_click=criar_conta,
        width=250,
        height=100,
        bgcolor=ft.Colors.ORANGE_700,
        color=ft.Colors.WHITE,
        style=button_style
    )
    
    botao_login = ft.ElevatedButton(
        text="Login",
        on_click=ir_para_login,
        width=300,
        height=400,
        bgcolor=ft.Colors.ORANGE_700,
        color=ft.Colors.WHITE,
        style=button_style
    )
    
    t1 = ft.Text(
        "Sonic Burgers Kiosk",
        size=40,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    # Main column containing all elements
    main_column = ft.Column(
        [
            t1,
            ft.Row(
                [botao_convidado, botao_login],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=100
            ),
            ft.Row(
                [botao_criar_conta],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.START,  # Changed from CENTER to START
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=100
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

ft.app(target=main)