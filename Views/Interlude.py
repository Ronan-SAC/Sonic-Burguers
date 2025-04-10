import flet as ft

def main(page: ft.Page):

    def ir_home(e):
        page.clean()
        page.go("/home")
        page.update()

    bg = ft.Container(
        ft.Image(
            src="./assets/interlude/bg3.png",  
            fit=ft.ImageFit.COVER,
            width=1080,
            height=1920,    
        ),
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

    container = ft.Stack(
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

    return ft.View(
        route="/interlude",
        controls=[container],
        bgcolor=ft.Colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )

if __name__ == "__main__":
    ft.app(target=main)