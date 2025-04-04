import flet as ft
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.Cards import botao_bk_style


def Menu_page(page: ft.Page):

    #função de click 
    def on_botao_click(e):
        print(f"Botão clicado: {e.control.content.controls[1].content.value}")

    grid = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    botao_bk_style("Whopper", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/3b/9a/d2/burger-king.jpg?w=500&h=300&s=1", on_botao_click),
                    botao_bk_style("Chicken", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/3b/9a/d2/burger-king.jpg?w=500&h=300&s=1", on_botao_click),
                    botao_bk_style("Fries", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/3b/9a/d2/burger-king.jpg?w=500&h=300&s=1", on_botao_click),
                ],
                spacing=10
            ),
            ft.Row(
                controls=[
                    botao_bk_style("Nuggets", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/3b/9a/d2/burger-king.jpg?w=500&h=300&s=1", on_botao_click),
                    botao_bk_style("Combo 1", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/3b/9a/d2/burger-king.jpg?w=500&h=300&s=1", on_botao_click),
                    botao_bk_style("Combo 2", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/3b/9a/d2/burger-king.jpg?w=500&h=300&s=1", on_botao_click),
                ],
                spacing=10
            ),
            ft.Row(
                controls=[
                    botao_bk_style("Soda", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/3b/9a/d2/burger-king.jpg?w=500&h=300&s=1", on_botao_click),
                    botao_bk_style("Shake", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/3b/9a/d2/burger-king.jpg?w=500&h=300&s=1", on_botao_click),
                    botao_bk_style("Dessert", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/3b/9a/d2/burger-king.jpg?w=500&h=300&s=1", on_botao_click),
                ],
                spacing=10
            ),
        ],
        spacing=10
    )


    imagem_topo = ft.Image(
        src="./assets/Header/Header.png", 
        height=300,
        fit=ft.ImageFit.COVER, 
    )

    conteudo = ft.Column(
        controls=[
            imagem_topo,
            grid
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(conteudo)

if __name__ == "__main__":
    ft.app(target=Menu_page)
