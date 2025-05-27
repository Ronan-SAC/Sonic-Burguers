import flet as ft
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.Cards import botao_bk_style

def main(page: ft.Page):
    # Função para navegar para a página de pedidos da categoria
    def navegar_categoria(e):
        categoria = e.control.data  # Acessa o data do Container
        page.go(f"/pedidos/{categoria}")

    # Função para voltar
    def voltar(e):
        page.session.remove("user_id") if page.session.contains_key("user_id") else None
        page.session.remove("user_name") if page.session.contains_key("user_name") else None
        page.session.set("carrinho_itens", [])
        page.go("/home")
        page.update()  # Redireciona para a página inicial

    # Lista de categorias com seus textos, imagens e dados
    categorias = [
        {
            "nome": "Carne",
            "imagem": "https://gkpb.com.br/wp-content/uploads/2020/09/mega-stacker-mucarela-empanda-scaled.jpg",  # Substitua pelo caminho real da imagem
            "data": "carne"
        },
        {
            "nome": "Frango",
            "imagem": "https://gkpb.com.br/wp-content/uploads/2022/12/gkpb-burger-king-sanduiches-frango-1.jpg",  # Substitua pelo caminho real da imagem
            "data": "frango"
        },
        {
            "nome": "Combos",
            "imagem": "https://gkpb.com.br/wp-content/uploads/2019/12/supercombo-burger-king-R-1990-geek-publicitario.png",  # Substitua pelo caminho real da imagem
            "data": "combos"
        },
        {
            "nome": "Acompanhamentos",
            "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/acompanhamentos-banner-cardapio-d.jpg?mtime=20210226103906&focal=none",  # Substitua pelo caminho real da imagem
            "data": "acompanhamentos"
        },
        {
            "nome": "Bebidas/Sobremesas",
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-ACoECbim_JOPKfX3yi0OpBucEUA5Ir7VuQ&s",  # Substitua pelo caminho real da imagem
            "data": "bebidas_sobremesas"
        },
    ]

    # Botão de voltar
    botao_voltar = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        icon_color=ft.Colors.WHITE,  # Atualizado para ft.Colors
        bgcolor=ft.Colors.ORANGE_700,  # Atualizado para ft.Colors
        on_click=voltar,
        tooltip="Voltar",
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            padding=10,
        )
    )

    # Grid de botões de categorias usando botao_bk_style
    grid_categorias = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    botao_bk_style(
                        texto=categoria["nome"],
                        imagem_path=categoria["imagem"],
                        on_click=navegar_categoria,
                        largura=(page.window.width / 2 - 30),  # Ajusta para 2 cards por linha
                        altura=350,  # Altura reduzida para melhor visualização
                        cor_texto="white",
                        cor_fundo_texto="orange",
                        data=categoria["data"],  # Passa o data para o componente
                    )
                    for categoria in categorias[i:i+2]
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER
            )
            for i in range(0, len(categorias), 2)
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO
    )

    # Imagem do topo
    imagem_topo = ft.Image(
        src="./assets/Header/Header.png",
        fit=ft.ImageFit.COVER,
    )

    # Conteúdo principal
    conteudo = ft.Column(
        controls=[
            imagem_topo,
            ft.Container(
                content=ft.Row(
                    controls=[botao_voltar],
                    alignment=ft.MainAxisAlignment.START
                ),
                padding=ft.padding.only(left=20, top=20)
            ),
            ft.Container(
                content=grid_categorias,
                alignment=ft.alignment.center,
                padding=ft.padding.only(top=20, left=20, right=20)
            )
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    # Estrutura final da view
    return ft.View(
        route="/tipo_pedido",
        controls=[conteudo],
        bgcolor=ft.Colors.AMBER_100,  # Atualizado para ft.Colors
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.START,
        padding=0
    )

if __name__ == "__main__":
    ft.app(target=main)