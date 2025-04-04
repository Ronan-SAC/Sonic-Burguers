import flet as ft


#Criar parametros do Componente
def botao_bk_style(
    texto: str,
    imagem_path: str,
    on_click=None,
    largura: int = 350,
    altura: int = 350,
    cor_texto: str = "white",
    cor_fundo_texto: str = "orange",
):



    #parametros do botão 
    botao = ft.Container(
        width=largura,
        height=altura,
        content=ft.Stack(
            controls=[
                ft.Image(
                    src=imagem_path,
                    fit=ft.ImageFit.COVER,
                    width=largura,
                    height=altura,
                ),
                ft.Container(
                    content=ft.Text(
                        texto,
                        color=cor_texto,
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    bgcolor=cor_fundo_texto,
                    width=largura,
                    height=120,
                    alignment=ft.alignment.center,
                    padding=5,
                    margin=ft.margin.only(top=altura - 80),
                ),
            ]
        ),
        border_radius=8,
        ink=True,
        on_click=on_click,
    )
    return botao
