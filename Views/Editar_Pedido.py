import flet as ft
from Views.PedidosCategoria import itens_lanche  # Importa a lista de itens

def main(page: ft.Page):
    page.title = "Modificar Lanche"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.bgcolor = ft.Colors.AMBER_100  

    # Extrai o nome do lanche da rota
    lanche_nome = page.route.split("/")[-1] if page.route.startswith("/Editar_Pedido/") else "Whopper"

    # Busca o item correspondente na lista de itens
    lanche_info = next((item for item in itens_lanche if item["nome"] == lanche_nome), None)
    if not lanche_info:
        return ft.View(
            route=page.route,
            controls=[
                ft.Text(f"Erro: Lanche {lanche_nome} não encontrado!", size=20, color=ft.Colors.RED)
            ],
            bgcolor=ft.Colors.AMBER_100,
            padding=20
        )

    # Título da página
    title = ft.Text(
        "Modifique Seu Lanche",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    )

    # Nome do lanche
    lanche_name = ft.Text(
        lanche_nome,
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.RED_800,
        text_align=ft.TextAlign.CENTER
    )

    # Texto para exibir o preço dinâmico
    preco_inicial = lanche_info["valor"]
    preco_texto = ft.Text(
        f"Preço: R${preco_inicial:.2f}",
        size=22,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.GREEN_700,
        text_align=ft.TextAlign.CENTER
    )

    # Ingredientes baseados no lanche selecionado, com preços
    ingredientes_base = [
        {**ing, "preco": preco} for ing, preco in [
            (ing, {
                "Pão com gergelim": 2.00, "Hambúrguer grelhado": 10.00, "Alface": 1.00, "Tomate": 1.50,
                "Maionese": 0.50, "Ketchup": 0.50, "Picles": 0.75, "Cebola": 0.80,
                "Pão": 1.50, "Frango empanado": 8.00
            }.get(ing["nome"], 1.00)) for ing in lanche_info.get("ingredientes", [])
        ]
    ]

    # Mapeamento de imagens para ingredientes
    imagens_ingredientes = {
        "Alface": "https://cdn.awsli.com.br/600x450/502/502061/produto/18350026/904bfc2e10.jpg",
        "Tomate": "https://static.vecteezy.com/system/resources/thumbnails/045/911/368/small/a-tomato-is-cut-in-half-and-has-a-small-drop-of-water-on-it-stock-png.png",
        "Cebola": "https://encrypted-tbn0.gstatic.com/images?q=GCSc3QvUQT1PdvLBo2QM5HzFOxoOk_0GNeqKuQ&s",
        "Picles": "https://static.vecteezy.com/system/resources/previews/045/905/548/non_2x/stack-of-sliced-pickles-cut-out-stock-png.png",
        "Hambúrguer grelhado": "https://example.com/hamburguer.png",
        "Pão": "https://example.com/pao.png",
        "Frango empanado": "https://example.com/frango_empanado.png",
    }

    # Combina ingredientes base com extras
    ingredientes = []
    for ing in ingredientes_base:
        ingredientes.append({
            "nome": ing["nome"],
            "quantidade": ing["quantidade"],
            "preco": ing["preco"],
            "imagem": imagens_ingredientes.get(ing["nome"], "https://example.com/placeholder.png")
        })

    # Função para calcular o preço total
    def calcular_preco_total():
        total = preco_inicial  # Começa com o preço inicial do lanche
        for ing in ingredientes:
            # Se o ingrediente for parte do lanche original, só adiciona o custo se a quantidade for maior que a original
            quantidade_original = next(
                (i["quantidade"] for i in ingredientes_base if i["nome"] == ing["nome"]), 0
            )
            quantidade_adicional = ing["quantidade"] - quantidade_original
            if quantidade_adicional > 0:
                total += quantidade_adicional * ing["preco"]
            elif quantidade_adicional < 0:
                # Subtrai o preço se remover ingredientes base (opcional, pode ser removido)
                total += quantidade_adicional * ing["preco"]
        return max(total, 0)  # Evita preços negativos

    # Função para atualizar a quantidade de ingredientes
    def atualizar_quantidade(ingrediente, incremento, texto_quantidade):
        nova_quantidade = ingrediente["quantidade"] + incremento
        if nova_quantidade >= 0:  # Evita quantidades negativas
            ingrediente["quantidade"] = nova_quantidade
            texto_quantidade.value = str(nova_quantidade)
            # Atualiza o preço total
            preco_texto.value = f"Preço: R${calcular_preco_total():.2f}"
        page.update()

    # Controles para os ingredientes
    ingredientes_controls = []
    for ingrediente in ingredientes:
        texto_quantidade = ft.Text(
            str(ingrediente["quantidade"]),
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLACK,
            text_align=ft.TextAlign.CENTER,
            width=50
        )

        quantidade_control = ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.REMOVE,
                    icon_color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.RED_700,
                    on_click=lambda e, ing=ingrediente, txt=texto_quantidade: atualizar_quantidade(ing, -1, txt),
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                ),
                texto_quantidade,
                ft.IconButton(
                    icon=ft.icons.ADD,
                    icon_color=ft.Colors.WHITE,
                    bgcolor=ft.Colors.GREEN_700,
                    on_click=lambda e, ing=ingrediente, txt=texto_quantidade: atualizar_quantidade(ing, 1, txt),
                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )

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
                    ft.Column(
                        [
                            ft.Text(ingrediente["nome"], size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                            ft.Text(f"R${ingrediente['preco']:.2f} por unidade", size=14, color=ft.Colors.GREY_700)
                        ],
                        spacing=5
                    ),
                    quantidade_control
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            margin=ft.margin.only(bottom=10),
            border=ft.border.all(1, ft.Colors.GREY_300)
        )
        ingredientes_controls.append(row)

    # Botões de ação
    def confirmar(e):
        # Atualiza os ingredientes e o preço do lanche na lista itens_lanche
        novos_ingredientes = [
            {"nome": ing["nome"], "quantidade": ing["quantidade"]}
            for ing in ingredientes if ing["quantidade"] > 0
        ]
        lanche_info["ingredientes"] = novos_ingredientes
        lanche_info["valor"] = calcular_preco_total()  # Atualiza o preço final
        # Exibe um resumo do pedido
        page.controls.clear()
        resumo = [ft.Text(f"{ing['nome']}: {ing['quantidade']}", size=18, color=ft.Colors.BLACK)
                  for ing in ingredientes if ing['quantidade'] > 0]
        page.add(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Lanche modificado com sucesso!", size=24, color=ft.Colors.GREEN_600, text_align=ft.TextAlign.CENTER),
                        ft.Text("Resumo do pedido:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                        ft.Column(resumo, alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                        ft.Text(f"Preço Final: R${lanche_info['valor']:.2f}", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700),
                        ft.ElevatedButton(
                            "Voltar ao pedido",
                            on_click=lambda e: page.go(f"/pedidos/{lanche_info['categoria']}"),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.RED_700,
                                color=ft.Colors.WHITE,
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
                bgcolor=ft.Colors.ORANGE_100,
                border_radius=15,
                border=ft.border.all(2, ft.Colors.RED_800),
            )
        )
        page.go(f"/pedidos/{lanche_info['categoria']}")
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
                    bgcolor=ft.Colors.RED_700,
                    color=ft.Colors.WHITE,
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
                    bgcolor=ft.Colors.GREY_700,
                    color=ft.Colors.WHITE,
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
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                lanche_name,
                preco_texto,
                ft.Text("Escolha os ingredientes:", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ft.Column(
                    ingredientes_controls,
                    spacing=0,
                    scroll=ft.ScrollMode.AUTO,
                    expand=True
                ),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                botoes
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=ft.Colors.AMBER_100,
        border_radius=15,
        border=ft.border.all(2, ft.Colors.RED_800),
    )

    return ft.View(
        route=f"/Editar_Pedido/{lanche_nome}",
        controls=[main_container],
        bgcolor=ft.Colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )