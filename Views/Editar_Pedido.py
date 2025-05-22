import flet as ft
from Views.PedidosCategoria import itens_lanche
import copy

def main(page: ft.Page):
    page.title = "Modificar Lanche"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.bgcolor = ft.Colors.AMBER_100

    item_id = page.route.split("/")[-1] if page.route.startswith("/Editar_Pedido/") else None
    carrinho_itens = page.session.get("carrinho_itens")
    if carrinho_itens is None:
        carrinho_itens = []
        page.session.set("carrinho_itens", carrinho_itens)
    
    lanche_info = next((item for item in carrinho_itens if item["id"] == item_id), None)
    if not lanche_info:
        return ft.View(
            route=page.route,
            controls=[
                ft.Text(f"Erro: Item não encontrado!", size=20, color=ft.Colors.RED)
            ],
            bgcolor=ft.Colors.AMBER_100,
            padding=20
        )

    title = ft.Text(
        "Modifique Seu Lanche",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    )

    lanche_name = ft.Text(
        lanche_info["nome"],
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.RED_800,
        text_align=ft.TextAlign.CENTER
    )

    preco_texto = ft.Text(
        f"Preço: R${lanche_info['valor']:.2f}",
        size=22,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.GREEN_700,
        text_align=ft.TextAlign.CENTER
    )

    ingredientes_base = [
        {**ing, "preco": preco} for ing, preco in [
            (ing, {
                "Pão com gergelim": 2.00, "Hambúrguer grelhado": 10.00, "Alface": 1.00, "Tomate": 1.50,
                "Maionese": 0.50, "Ketchup": 0.50, "Picles": 0.75, "Cebola": 0.80,
                "Pão": 1.50, "Frango empanado": 8.00
            }.get(ing["nome"], 1.00)) for ing in lanche_info.get("ingredientes", [])
        ]
    ]

    imagens_ingredientes = {
        "Alface": "https://cdn.awsli.com.br/600x450/502/502061/produto/18350026/904bfc2e10.jpg",
        "Tomate": "https://static.vecteezy.com/system/resources/thumbnails/045/911/368/small/a-tomato-is-cut-in-half-and-has-a-small-drop-of-water-on-it-stock-png.png",
        "Cebola": "https://encrypted-tbn0.gstatic.com/images?q=GCSc3QvUQT1PdvLBo2QM5HzFOxoOk_0GNeqKuQ&s",
        "Picles": "https://static.vecteezy.com/system/resources/previews/045/905/548/non_2x/stack-of-sliced-pickles-cut-out-stock-png.png",
        "Hambúrguer grelhado": "https://example.com/hamburguer.png",
        "Pão": "https://example.com/pao.png",
        "Frango empanado": "https://example.com/frango_empanado.png",
    }

    ingredientes = [
        {
            "nome": ing["nome"],
            "quantidade": ing["quantidade"],
            "preco": ing["preco"],
            "imagem": imagens_ingredientes.get(ing["nome"], "https://example.com/placeholder.png")
        } for ing in ingredientes_base
    ]

    def calcular_preco_total():
        total = lanche_info["valor"]
        for ing in ingredientes:
            quantidade_original = next(
                (i["quantidade"] for i in ingredientes_base if i["nome"] == ing["nome"]), 0
            )
            quantidade_adicional = ing["quantidade"] - quantidade_original
            if quantidade_adicional > 0:
                total += quantidade_adicional * ing["preco"]
            elif quantidade_adicional < 0:
                total += quantidade_adicional * ing["preco"]
        return max(total, 0)

    ingredientes_controls = []

    def atualizar_ingredientes_controls():
        ingredientes_controls.clear()
        for ingrediente in ingredientes:
            texto_quantidade = ft.Text(
                str(ingrediente["quantidade"]),
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK,
                text_align=ft.TextAlign.CENTER,
                width=50
            )

            quantidade_original = next(
                (i["quantidade"] for i in ingredientes_base if i["nome"] == ingrediente["nome"]), 0
            )

            quantidade_control = ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.REMOVE,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.RED_700,
                        disabled=ingrediente["quantidade"] <= quantidade_original,
                        on_click=lambda e, ing=ingrediente, txt=texto_quantidade: atualizar_quantidade(ing, -1, txt),
                        style=ft.ButtonStyle(shape=ft.CircleBorder()),
                    ),
                    texto_quantidade,
                    ft.IconButton(
                        icon=ft.icons.ADD,
                        icon_color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.GREEN_700,
                        disabled=ingrediente["quantidade"] >= 5,  # Disable when quantity reaches 5
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
        main_container.content.controls[4] = ft.Column(
            ingredientes_controls,
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )

    def atualizar_quantidade(ingrediente, incremento, texto_quantidade):
        quantidade_original = next(
            (i["quantidade"] for i in ingredientes_base if i["nome"] == ingrediente["nome"]), 0
        )
        nova_quantidade = ingrediente["quantidade"] + incremento
        if incremento < 0 and nova_quantidade < quantidade_original:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Não é possível remover mais {ingrediente['nome']}. Quantidade mínima é {quantidade_original}."),
                bgcolor=ft.Colors.RED_700,
                duration=3000
            )
            page.snack_bar.open = True
            page.update()
        elif incremento > 0 and nova_quantidade > 5:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Não é possível adicionar mais {ingrediente['nome']}. Quantidade máxima é 5."),
                bgcolor=ft.Colors.RED_700,
                duration=3000
            )
            page.snack_bar.open = True
            page.update()
        elif nova_quantidade >= 0:
            ingrediente["quantidade"] = nova_quantidade
            texto_quantidade.value = str(nova_quantidade)
            preco_texto.value = f"Preço: R${calcular_preco_total():.2f}"
            atualizar_ingredientes_controls()
            page.update()

    main_container = ft.Container(
        content=ft.Column(
            [
                title,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                lanche_name,
                preco_texto,
                ft.Column(
                    [],  # Will be populated by atualizar_ingredientes_controls
                    spacing=0,
                    scroll=ft.ScrollMode.AUTO,
                    expand=True
                ),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Confirmar",
                            on_click=lambda e: confirmar(),
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
                            on_click=lambda e: cancelar(),
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
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=ft.Colors.AMBER_100,
        border_radius=15,
        border=ft.border.all(2, ft.Colors.RED_800),
    )

    def confirmar():
        novos_ingredientes = [
            {"nome": ing["nome"], "quantidade": ing["quantidade"]}
            for ing in ingredientes if ing["quantidade"] > 0
        ]
        lanche_info["ingredientes"] = novos_ingredientes
        lanche_info["valor"] = calcular_preco_total()
        page.session.set("carrinho_itens", carrinho_itens)
        page.go(f"/pedidos/{lanche_info['categoria']}")
        page.update()

    def cancelar():
        page.go(f"/pedidos/{lanche_info['categoria']}")
        page.update()

    atualizar_ingredientes_controls()  # Populate initial controls

    return ft.View(
        route=f"/Editar_Pedido/{item_id}",
        controls=[main_container],
        bgcolor=ft.Colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )

if __name__ == "__main__":
    ft.app(target=main)