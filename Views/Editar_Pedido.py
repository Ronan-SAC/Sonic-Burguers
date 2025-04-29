import flet as ft
from Views.PedidosCategoria import itens_lanche  # Importa a lista de itens

def main(page: ft.Page):
    page.title = "Modificar Lanche"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.bgcolor = ft.colors.AMBER_100  

    # Extrai o nome do lanche da rota
    lanche_nome = page.route.split("/")[-1] if page.route.startswith("/Editar_Pedido/") else "Whopper"

    # Busca o item correspondente na lista de itens
    lanche_info = next((item for item in itens_lanche if item["nome"] == lanche_nome), None)
    if not lanche_info:
        return ft.View(
            route=page.route,
            controls=[
                ft.Text(f"Erro: Lanche {lanche_nome} não encontrado!", size=20, color=ft.colors.RED)
            ],
            bgcolor=ft.colors.AMBER_100,
            padding=20
        )

    # Título da página
    title = ft.Text(
        "Modifique Seu Lanche",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    )

    # Nome do lanche
    lanche_name = ft.Text(
        lanche_nome,
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.RED_800,
        text_align=ft.TextAlign.CENTER
    )

    # Ingredientes baseados no lanche selecionado, com opção de adicionar extras
    ingredientes_base = lanche_info.get("ingredientes", [])
    ingredientes_extras = [
        {"nome": "Queijo", "quantidade": 0, "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSc3QvUQT1PdvLBo2QM5HzFOxoOk_0GNeqKuQ&s"},
        {"nome": "Bacon", "quantidade": 0, "imagem": "https://static.vecteezy.com/system/resources/previews/025/222/207/non_2x/bacon-slices-isolated-on-transparent-background-png.png"},
    ]

    # Mapeamento de imagens para ingredientes
    imagens_ingredientes = {
        "Alface": "https://cdn.awsli.com.br/600x450/502/502061/produto/18350026/904bfc2e10.jpg",
        "Tomate": "https://static.vecteezy.com/system/resources/thumbnails/045/911/368/small/a-tomato-is-cut-in-half-and-has-a-small-drop-of-water-on-it-stock-png.png",
        "Cebola": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYifSkhYtJO-6xi4kPKvu7Ch-JiSxNt68grA&s",
        "Picles": "https://static.vecteezy.com/system/resources/previews/045/905/548/non_2x/stack-of-sliced-pickles-cut-out-stock-png.png",
        "Maionese": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0WLnjvJ6MIxWVaPUPVFG1RQwXTKDl-SZJWA&s",
        "Ketchup": "https://static.vecteezy.com/system/resources/thumbnails/054/649/666/small/ketchup-dollop-with-shiny-texture-and-vibrant-red-color-on-isolated-background-for-food-design-and-culinary-visuals-png.png",
        "Queijo": "https://encrypted-tbn0.gstatic.com/images?q=tbn=GCSc3QvUQT1PdvLBo2QM5HzFOxoOk_0GNeqKuQ&s",
        "Bacon": "https://static.vecteezy.com/system/resources/previews/025/222/207/non_2x/bacon-slices-isolated-on-transparent-background-png.png",
        "Pão com gergelim": "https://example.com/pao_gergelim.png",  # Substitua por uma URL válida
        "Hambúrguer grelhado": "https://example.com/hamburguer.png",  # Substitua por uma URL válida
        "Pão": "https://example.com/pao.png",  # Substitua por uma URL válida
        "Frango empanado": "https://example.com/frango_empanado.png",  # Substitua por uma URL válida
    }

    # Combina ingredientes base com extras, mantendo quantidades
    ingredientes = []
    for ing in ingredientes_base:
        ingredientes.append({
            "nome": ing["nome"],
            "quantidade": ing["quantidade"],
            "imagem": imagens_ingredientes.get(ing["nome"], "https://example.com/placeholder.png")
        })
    for ing in ingredientes_extras:
        ingredientes.append({
            "nome": ing["nome"],
            "quantidade": ing["quantidade"],
            "imagem": ing["imagem"]
        })

    def atualizar_quantidade(ingrediente, incremento, texto_quantidade):
        nova_quantidade = ingrediente["quantidade"] + incremento
        if nova_quantidade >= 0:  # Evita quantidades negativas
            ingrediente["quantidade"] = nova_quantidade
            texto_quantidade.value = str(nova_quantidade)  # Atualiza o texto na interface
        page.update()

    # Controles para os ingredientes
    ingredientes_controls = []
    for ingrediente in ingredientes:
        # Componente de texto para a quantidade
        texto_quantidade = ft.Text(
            str(ingrediente["quantidade"]),
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLACK,
            text_align=ft.TextAlign.CENTER,
            width=50
        )

        # Botões no estilo - Número +
        quantidade_control = ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.REMOVE,
                    icon_color=ft.colors.WHITE,
                    bgcolor=ft.colors.RED_700,
                    on_click=lambda e, ing=ingrediente, txt=texto_quantidade: atualizar_quantidade(ing, -1, txt),
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                ),
                texto_quantidade,
                ft.IconButton(
                    icon=ft.icons.ADD,
                    icon_color=ft.colors.WHITE,
                    bgcolor=ft.colors.GREEN_700,
                    on_click=lambda e, ing=ingrediente, txt=texto_quantidade: atualizar_quantidade(ing, 1, txt),
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )

        # Linha com imagem, nome e controle de quantidade
        row = ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                        src=ingrediente["imagem"],
                        width=60,
                        height=60,
                        fit=ft.ImageFit.CONTAIN,
                        error_content=ft.Text("Imagem não carregada")
                    ),
                    ft.Text(ingrediente["nome"], size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                    quantidade_control
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10,
            bgcolor=ft.colors.WHITE,
            border_radius=10,
            margin=ft.margin.only(bottom=10),
            border=ft.border.all(1, ft.colors.GREY_300)
        )
        ingredientes_controls.append(row)

    # Botões de ação
    def confirmar(e):
        # Atualiza os ingredientes do lanche na lista itens_lanche
        novos_ingredientes = [
            {"nome": ing["nome"], "quantidade": ing["quantidade"]}
            for ing in ingredientes if ing["quantidade"] > 0 and ing["nome"] not in ["Queijo", "Bacon"]
        ]
        lanche_info["ingredientes"] = novos_ingredientes
        # Exibe um resumo do pedido
        page.controls.clear()
        resumo = [ft.Text(f"{ing['nome']}: {ing['quantidade']}", size=18, color=ft.colors.BLACK)
                  for ing in ingredientes if ing['quantidade'] > 0]
        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Lanche modificado com sucesso!", size=24, color=ft.colors.GREEN_600, text_align=ft.TextAlign.CENTER),
                        ft.Text("Resumo do pedido:", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                        ft.Column(resumo, alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                        ft.ElevatedButton(
                            "Voltar ao pedido",
                            on_click=lambda e: page.go(f"/pedidos/{lanche_info['categoria']}"),
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.RED_700,
                                color=ft.colors.WHITE,
                                shape=ft.RoundedRectangleBorder(radius=10),
                                padding=15
                            ),
                            height=50,
                            width=150
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                ),
                padding=20,
                bgcolor=ft.colors.ORANGE_100,
                border_radius=15,
                border=ft.border.all(2, ft.colors.RED_800),
            )
        )
        page.update()

    def cancelar(e):
        # Volta à tela de pedidos sem salvar alterações
        page.go(f"/pedidos/{lanche_info['categoria']}")
        page.update()

    botoes = ft.Row(
        [
            ft.ElevatedButton(
                "Confirmar",
                on_click=confirmar,
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.RED_700,
                    color=ft.colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=10),
                    padding=15
                ),
                height=50,
                width=150
            ),
            ft.ElevatedButton(
                "Cancelar",
                on_click=cancelar,
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.GREY_700,
                    color=ft.colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=10),
                    padding=15
                ),
                height=50,
                width=150
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Layout principal
    main_container = ft.Container(
        content=ft.Column(
            [
                title,
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                lanche_name,
                ft.Text("Escolha os ingredientes:", size=22, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                ft.Column(
                    ingredientes_controls,
                    spacing=0,
                    scroll=ft.ScrollMode.AUTO,
                    expand=True
                ),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                botoes
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=ft.colors.AMBER_100, 
        border_radius=15,
        border=ft.border.all(2, ft.colors.RED_800),
    )

    return ft.View(
        route=f"/Editar_Pedido/{lanche_nome}",
        controls=[main_container],
        bgcolor=ft.colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )