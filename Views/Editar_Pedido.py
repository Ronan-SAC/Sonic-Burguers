import flet as ft
from Views.PedidosCategoria import itens_lanche
import copy
import uuid

def main(page: ft.Page):
    page.title = "Modificar Item"
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
        "Modifique Seu Item",
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

    # Verificar tipo de item
    item_original = next((i for i in itens_lanche if i["nome"] == lanche_info["nome"]), None)
    is_hamburger = "ingredientes" in item_original
    is_combo = "combo_componentes" in item_original
    is_tamanho = not is_hamburger and not is_combo and "tamanhos" in item_original

    ingredientes = []
    tamanhos = []
    combo_componentes = {}
    tamanho_selecionado = ft.Ref[ft.Dropdown]()
    hamburguer_selecionado = ft.Ref[ft.Dropdown]()
    bebida_selecionada = ft.Ref[ft.Dropdown]()
    acompanhamento_selecionado = ft.Ref[ft.Dropdown]()
    brinquedo_selecionado = ft.Ref[ft.Dropdown]()

    if is_hamburger:
        # Configuração para hambúrgueres
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
    elif is_tamanho:
        # Configuração para itens com tamanhos
        tamanhos = item_original.get("tamanhos", [])
        lanche_info["tamanho"] = lanche_info.get("tamanho", tamanhos[1]["nome"] if tamanhos else "Médio")
    elif is_combo:
        # Configuração para combos
        combo_componentes = item_original.get("combo_componentes", {})
        lanche_info["combo_selecoes"] = lanche_info.get("combo_selecoes", {
            "hamburguer": combo_componentes["hamburguer"][0]["nome"],
            "bebida": combo_componentes["bebida"][0]["nome"],
            "acompanhamento": combo_componentes["acompanhamento"][0]["nome"],
            "brinquedo": combo_componentes.get("brinquedo", [None])[0]["nome"] if "brinquedo" in combo_componentes else None
        })

    def calcular_preco_total():
        if is_hamburger:
            total = item_original["valor"]
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
        elif is_tamanho:
            selected_tamanho = tamanho_selecionado.current.value if tamanho_selecionado.current else tamanhos[1]["nome"]
            tamanho_info = next((t for t in tamanhos if t["nome"] == selected_tamanho), None)
            return tamanho_info["preco"] if tamanho_info else item_original["valor"]
        elif is_combo:
            total = 0  # Start from 0 to sum the selected components
            selecoes = lanche_info["combo_selecoes"]
            # Preço do hambúrguer
            hamburguer_item = next((h for h in combo_componentes["hamburguer"] if h["nome"] == selecoes["hamburguer"]), None)
            total += hamburguer_item["valor"] if hamburguer_item else combo_componentes["hamburguer"][0]["valor"]
            # Preço da bebida
            bebida_item = next((b for b in combo_componentes["bebida"] if b["nome"] == selecoes["bebida"]), None)
            total += bebida_item["valor"] if bebida_item else combo_componentes["bebida"][0]["valor"]
            # Preço do acompanhamento
            acompanhamento_item = next((a for a in combo_componentes["acompanhamento"] if a["nome"] == selecoes["acompanhamento"]), None)
            total += acompanhamento_item["valor"] if acompanhamento_item else combo_componentes["acompanhamento"][0]["valor"]
            # Preço do brinquedo (apenas Combo 2)
            if selecoes.get("brinquedo") and selecoes["brinquedo"] != "Nenhum":
                brinquedo_item = next((b for b in combo_componentes.get("brinquedo", []) if b["nome"] == selecoes["brinquedo"]), None)
                total += brinquedo_item["valor"] if brinquedo_item else 0
            # Apply a discount to make combo pricing attractive (optional)
            total = total * 0.9  # 10% discount for combo
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
                        disabled=ingrediente["quantidade"] >= 5,
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

    def on_componente_change(e):
        if is_combo:
            lanche_info["combo_selecoes"] = {
                "hamburguer": hamburguer_selecionado.current.value,
                "bebida": bebida_selecionada.current.value,
                "acompanhamento": acompanhamento_selecionado.current.value,
                "brinquedo": brinquedo_selecionado.current.value if brinquedo_selecionado.current and brinquedo_selecionado.current.value != "Nenhum" else None
            }
        preco_texto.value = f"Preço: R${calcular_preco_total():.2f}"
        page.update()

    # Controles para combos
    combo_controls = []
    if is_combo:
        combo_controls.append(
            ft.Container(
                content=ft.Dropdown(
                    ref=hamburguer_selecionado,
                    label="Hambúrguer",
                    value=lanche_info["combo_selecoes"]["hamburguer"],
                    options=[ft.dropdown.Option(h["nome"]) for h in combo_componentes["hamburguer"]],
                    on_change=on_componente_change,
                    width=200,
                    bgcolor=ft.Colors.WHITE,
                    border_color=ft.Colors.GREY_300,
                    text_size=16
                ),
                padding=10,
                bgcolor=ft.Colors.WHITE,
                border_radius=10,
                margin=ft.margin.only(bottom=10),
                border=ft.border.all(1, ft.Colors.GREY_300)
            )
        )
        combo_controls.append(
            ft.Container(
                content=ft.Dropdown(
                    ref=bebida_selecionada,
                    label="Bebida",
                    value=lanche_info["combo_selecoes"]["bebida"],
                    options=[ft.dropdown.Option(b["nome"]) for b in combo_componentes["bebida"]],
                    on_change=on_componente_change,
                    width=200,
                    bgcolor=ft.Colors.WHITE,
                    border_color=ft.Colors.GREY_300,
                    text_size=16
                ),
                padding=10,
                bgcolor=ft.Colors.WHITE,
                border_radius=10,
                margin=ft.margin.only(bottom=10),
                border=ft.border.all(1, ft.Colors.GREY_300)
            )
        )
        combo_controls.append(
            ft.Container(
                content=ft.Dropdown(
                    ref=acompanhamento_selecionado,
                    label="Acompanhamento",
                    value=lanche_info["combo_selecoes"]["acompanhamento"],
                    options=[ft.dropdown.Option(a["nome"]) for a in combo_componentes["acompanhamento"]],
                    on_change=on_componente_change,
                    width=200,
                    bgcolor=ft.Colors.WHITE,
                    border_color=ft.Colors.GREY_300,
                    text_size=16
                ),
                padding=10,
                bgcolor=ft.Colors.WHITE,
                border_radius=10,
                margin=ft.margin.only(bottom=10),
                border=ft.border.all(1, ft.Colors.GREY_300)
            )
        )
        if "brinquedo" in combo_componentes:
            combo_controls.append(
                ft.Container(
                    content=ft.Dropdown(
                        ref=brinquedo_selecionado,
                        label="Brinquedo",
                        value=lanche_info["combo_selecoes"]["brinquedo"] or "Nenhum",
                        options=[ft.dropdown.Option("Nenhum")] + [ft.dropdown.Option(b["nome"]) for b in combo_componentes["brinquedo"]],
                        on_change=on_componente_change,
                        width=200,
                        bgcolor=ft.Colors.WHITE,
                        border_color=ft.Colors.GREY_300,
                        text_size=16
                    ),
                    padding=10,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=10,
                    margin=ft.margin.only(bottom=10),
                    border=ft.border.all(1, ft.Colors.GREY_300)
                )
            )

    tamanho_dropdown = ft.Dropdown(
        ref=tamanho_selecionado,
        label="Tamanho",
        value=lanche_info.get("tamanho", tamanhos[1]["nome"] if tamanhos else "Médio"),
        options=[ft.dropdown.Option(t["nome"]) for t in tamanhos],
        on_change=on_componente_change,
        width=200,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.GREY_300,
        text_size=16
    ) if is_tamanho else None

    main_container = ft.Container(
        content=ft.Column(
            [
                title,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                lanche_name,
                preco_texto,
                ft.Column(
                    combo_controls if is_combo else (ingredientes_controls if is_hamburger else [tamanho_dropdown] if tamanho_dropdown else []),
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
        if is_hamburger:
            novos_ingredientes = [
                {"nome": ing["nome"], "quantidade": ing["quantidade"]}
                for ing in ingredientes if ing["quantidade"] > 0
            ]
            lanche_info["ingredientes"] = novos_ingredientes
        elif is_tamanho:
            lanche_info["tamanho"] = tamanho_selecionado.current.value if tamanho_selecionado.current else tamanhos[1]["nome"]
        elif is_combo:
            lanche_info["combo_selecoes"] = {
                "hamburguer": hamburguer_selecionado.current.value,
                "bebida": bebida_selecionada.current.value,
                "acompanhamento": acompanhamento_selecionado.current.value,
                "brinquedo": brinquedo_selecionado.current.value if brinquedo_selecionado.current and brinquedo_selecionado.current.value != "Nenhum" else None
            }
        lanche_info["valor"] = calcular_preco_total()
        page.session.set("carrinho_itens", carrinho_itens)
        page.go(f"/pedidos/{lanche_info['categoria']}")
        page.update()

    def cancelar():
        page.go(f"/pedidos/{lanche_info['categoria']}")
        page.update()

    if is_hamburger:
        atualizar_ingredientes_controls()
    else:
        preco_texto.value = f"Preço: R${calcular_preco_total():.2f}"

    return ft.View(
        route=f"/Editar_Pedido/{item_id}",
        controls=[main_container],
        bgcolor=ft.Colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )

if __name__ == "__main__":
    ft.app(target=main)