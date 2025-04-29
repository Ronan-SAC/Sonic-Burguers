import flet as ft
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.Cards import botao_bk_style

itens_lanche = [
    {
        "nome": "Whopper",
        "valor": 29.90,
        "ingredientes": [
            {"nome": "Pão com gergelim", "quantidade": 1},
            {"nome": "Hambúrguer grelhado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Tomate", "quantidade": 2},
            {"nome": "Maionese", "quantidade": 1},
            {"nome": "Ketchup", "quantidade": 1},
            {"nome": "Picles", "quantidade": 4},
            {"nome": "Cebola", "quantidade": 2}
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/_800x600_crop_center-center_none/whopper-thumb_2021-09-16-125319_mppe.png?mtime=20210916125320&focal=none&tmtime=20241024164409",
        "categoria": "carne"
    },
    {
        "nome": "Chicken",
        "valor": 24.90,
        "ingredientes": [
            {"nome": "Pão", "quantidade": 1},
            {"nome": "Frango empanado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Maionese", "quantidade": 1}
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/BK-Chicken-Crispy-thumb.png?mtime=20230125075509&focal=none",
        "categoria": "frango"
    },
    {
        "nome": "Fries",
        "valor": 12.90,
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSR98FtNSxebKF-I5dZEgSf9QbFCaGQ4XRVzA&s",
        "categoria": "acompanhamentos"
    },
    {
        "nome": "Nuggets",
        "valor": 19.90,
        "imagem": "https://wp-cdn.typhur.com/wp-content/uploads/2025/02/air-fryer-frozen-chicken-nuggets.jpg",
        "categoria": "frango"
    },
    {
        "nome": "Combo 1",
        "valor": 39.90,
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/1-C-Chicken-Crispy-app-thumb-cupom-m-d.png?mtime=20230703165033&focal=none",
        "categoria": "combos"
    },
    {
        "nome": "Combo 2",
        "valor": 44.90,
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQREHs1qMFNx8TTFiplwEzfbhwuT6vTfw6zrQ&s",
        "categoria": "combos"
    },
    {
        "nome": "Soda",
        "valor": 9.90,
        "imagem": "https://upload.wikimedia.org/wikipedia/commons/e/e8/15-09-26-RalfR-WLC-0098_-_Coca-Cola_glass_bottle_%28Germany%29.jpg",
        "categoria": "bebidas_sobremesas"
    },
    {
        "nome": "Shake",
        "valor": 14.90,
        "imagem": "https://static.itdg.com.br/images/1200-630/ee9c780da91c8377e7f6a10f30c6c1da/milk-shake-caseiro.jpg",
        "categoria": "bebidas_sobremesas"
    },
    {
        "nome": "Dessert",
        "valor": 7.90,
        "imagem": "https://images.rappi.com.br/restaurants_background/sobremesas_burger_king-1662576783697.jpg?e=webp&d=700x100&q=10",
        "categoria": "bebidas_sobremesas"
    },
]

def main(page: ft.Page):
    # Extrai a categoria da rota
    categoria = page.route.split("/")[-1] if page.route.startswith("/pedidos/") else "carne"

    # Filtra os itens pela categoria
    itens_filtrados = [item for item in itens_lanche if item.get("categoria") == categoria]

    # Lista para armazenar os itens do carrinho
    carrinho_itens = []

    # Função para voltar
    def voltar(e):
        page.go("/tipo_pedido")  # Volta para a página de seleção de categorias

    # Função para atualizar o carrinho na interface
    def atualizar_carrinho():
        carrinho_lista.controls.clear()
        total = 0
        for item in carrinho_itens:
            item_info = next((i for i in itens_lanche if i["nome"] == item), None)
            if item_info:
                total += item_info["valor"]
                ingredientes_texto = ", ".join([f"{ing['nome']} ({ing['quantidade']})" for ing in item_info.get("ingredientes", [])])
                carrinho_lista.controls.append(
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.FASTFOOD, color=ft.colors.ORANGE_700, size=24),
                                ft.Column(
                                    controls=[
                                        ft.Text(f"{item}", weight=ft.FontWeight.BOLD, size=16),
                                        ft.Text(f"R${item_info['valor']:.2f}", color=ft.colors.GREY_700, size=14),
                                        ft.Text(f"Ingredientes: {ingredientes_texto}", size=12, color=ft.colors.GREY_600, italic=True) if ingredientes_texto else ft.Text(""),
                                    ],
                                    spacing=5,
                                    expand=True
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE_OUTLINE,
                                    icon_color=ft.colors.RED_400,
                                    on_click=lambda e, item=item: remover_item(item)
                                ),
                                ft.IconButton(
                                    icon=ft.icons.EDIT_OUTLINED,
                                    icon_color=ft.colors.BLUE_400,
                                    on_click=lambda e, item=item: editar_lanche(item)
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        bgcolor=ft.colors.WHITE,
                        padding=10,
                        border_radius=10,
                        margin=ft.margin.only(bottom=8),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=5,
                            color=ft.colors.BLACK12,
                            offset=ft.Offset(0, 2)
                        )
                    )
                )
        carrinho_lista.controls.append(
            ft.Container(
                content=ft.Text(f"Total: R${total:.2f}", weight=ft.FontWeight.BOLD, size=18, color=ft.colors.BLACK87),
                padding=10,
                alignment=ft.alignment.center_right
            )
        )
        page.update()

    # Função para remover item do carrinho
    def remover_item(item):
        carrinho_itens.remove(item)
        atualizar_carrinho()

    # Função para editar lanche
    def editar_lanche(item):
        page.go(f"/Editar_Pedido/{item}")
        page.update()

    # Função de clique nos botões do menu
    def on_botao_click(e):
        item_nome = e.control.content.controls[1].content.value  # Pega o nome do item
        carrinho_itens.append(item_nome)  # Adiciona o item ao carrinho
        atualizar_carrinho()  # Atualiza a visualização do carrinho

    # Função para finalizar o pedido
    def finalizar_pedido(e):
        if carrinho_itens:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Pedido finalizado com sucesso!", color=ft.colors.WHITE),
                bgcolor=ft.colors.GREEN_600
            )
            page.snack_bar.open = True
            carrinho_itens.clear()  # Limpa o carrinho
            atualizar_carrinho()
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Carrinho vazio!", color=ft.colors.WHITE),
                bgcolor=ft.colors.RED_600
            )
            page.snack_bar.open = True
        page.update()

    # Botão de voltar
    botao_voltar = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        icon_color=ft.colors.WHITE,
        bgcolor=ft.colors.ORANGE_700,
        on_click=voltar,
        tooltip="Voltar",
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            padding=10,
        )
    )

    # Grid com os itens filtrados
    grid = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    botao_bk_style(item["nome"], item["imagem"], on_botao_click)
                    for item in itens_filtrados[i:i+3]
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER
            )
            for i in range(0, len(itens_filtrados), 3)
        ],
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Imagem do topo
    imagem_topo = ft.Image(
        src="./assets/Header/Header.png",
        fit=ft.ImageFit.COVER,
    )

    # Lista de itens do carrinho
    carrinho_lista = ft.Column(
        controls=[],
        scroll=ft.ScrollMode.AUTO,
        height=400,
        width=page.window.width - 40,
        spacing=0
    )
    carrinho_lista_container = ft.Container(
        content=carrinho_lista,
        bgcolor=ft.colors.GREY_100,
        padding=15,
        border_radius=15,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.colors.BLACK26,
            offset=ft.Offset(0, 4)
        )
    )

    # Carrinho na parte inferior
    carrinho = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.SHOPPING_CART, color=ft.colors.ORANGE_700, size=28),
                        ft.Text("Seu Carrinho", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK87),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10
                ),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                carrinho_lista_container,
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE, size=20),
                            ft.Text("Finalizar Pedido", size=16, weight=ft.FontWeight.BOLD),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=8
                    ),
                    on_click=finalizar_pedido,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.GREEN_600,
                        color=ft.colors.WHITE,
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=15,
                        elevation=5
                    ),
                    width=page.window.width - 40
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.only(left=20, right=20, top=20, bottom=20),
        width=page.window.width,
        border_radius=ft.border_radius.only(top_left=20, top_right=20),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.colors.BLACK26,
            offset=ft.Offset(0, -2)
        )
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
                content=grid,
                alignment=ft.alignment.center,
                padding=ft.padding.only(top=20)
            ),
            ft.Divider(height=20, color=ft.colors.TRANSPARENT),
            ft.Container(content= carrinho,  margin= ft.margin.only(top=560))
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    # Estrutura final da view
    return ft.View(
        route=f"/pedidos/{categoria}",
        controls=[conteudo],
        bgcolor=ft.colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.START,
        padding=0
    )