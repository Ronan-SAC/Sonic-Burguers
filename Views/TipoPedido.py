import flet as ft

def main(page: ft.Page):
    # Função para navegar para a página de pedidos da categoria
    def navegar_categoria(e):
        categoria = e.control.data
        page.go(f"/pedidos/{categoria}")

    # Função para voltar
    def voltar(e):
        page.go("/home")  # Redireciona para a página inicial (ajuste conforme necessário)

    # Lista de categorias com seus ícones e textos
    categorias = [
        {"nome": "Lanches de Carne", "icone": ft.icons.FASTFOOD, "data": "carne"},
        {"nome": "Frango", "icone": ft.icons.FASTFOOD, "data": "frango"},
        {"nome": "Combos", "icone": ft.icons.MENU_BOOK, "data": "combos"},
        {"nome": "Acompanhamentos", "icone": ft.icons.RESTAURANT, "data": "acompanhamentos"},
        {"nome": "Bebidas/Sobremesas", "icone": ft.icons.LOCAL_DRINK, "data": "bebidas_sobremesas"},
    ]

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

    # Grid de botões de categorias
    grid_categorias = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(categoria["icone"], color=ft.colors.WHITE, size=24),
                                ft.Text(categoria["nome"], size=18, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10
                        ),
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.ORANGE_700,
                            color=ft.colors.WHITE,
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=20,
                            elevation=5
                        ),
                        on_click=navegar_categoria,
                        data=categoria["data"],
                        width=page.window.width / 2 - 30  # Divide a largura para 2 botões por linha
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
        bgcolor=ft.colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.START,
        padding=0
    )

if __name__ == "__main__":
    ft.app(target=main)