import flet as ft
import os
import sys
import uuid
import copy
import json

from Controllers.UsersControllers import Controller_user

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.Cards import botao_bk_style

itens_lanche = [
    {
        "nome": "Whopper",
        "valor": 29.90,
        "ingredientes": [
            {"nome": "Hambúrguer grelhado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Tomate", "quantidade": 2},
            {"nome": "Picles", "quantidade": 4},
            {"nome": "Cebola", "quantidade": 2}
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/_800x600_crop_center-center_none/whopper-thumb_2021-09-16-125319_mppe.png?mtime=20210916125320&focal=none&tmtime=20241024164409",
        "categoria": "carne"
    },
    {
        "nome": "Whopper",
        "valor": 29.90,
        "ingredientes": [
            {"nome": "Hambúrguer grelhado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Tomate", "quantidade": 2},
            {"nome": "Picles", "quantidade": 4},
            {"nome": "Cebola", "quantidade": 2}
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/_800x600_crop_center-center_none/whopper-thumb_2021-09-16-125319_mppe.png?mtime=20210916125320&focal=none&tmtime=20241024164409",
        "categoria": "carne"
    },
    {
        "nome": "Whopper",
        "valor": 29.90,
        "ingredientes": [
            {"nome": "Hambúrguer grelhado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Tomate", "quantidade": 2},
            {"nome": "Picles", "quantidade": 4},
            {"nome": "Cebola", "quantidade": 2}
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/_800x600_crop_center-center_none/whopper-thumb_2021-09-16-125319_mppe.png?mtime=20210916125320&focal=none&tmtime=20241024164409",
        "categoria": "carne"
    },
    {
        "nome": "Whopper",
        "valor": 29.90,
        "ingredientes": [
            {"nome": "Hambúrguer grelhado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Tomate", "quantidade": 2},
            {"nome": "Picles", "quantidade": 4},
            {"nome": "Cebola", "quantidade": 2}
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/_800x600_crop_center-center_none/whopper-thumb_2021-09-16-125319_mppe.png?mtime=20210916125320&focal=none&tmtime=20241024164409",
        "categoria": "carne"
    },
    {
        "nome": "Whopper",
        "valor": 29.90,
        "ingredientes": [
            {"nome": "Hambúrguer grelhado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Tomate", "quantidade": 2},
            {"nome": "Picles", "quantidade": 4},
            {"nome": "Cebola", "quantidade": 2}
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/_800x600_crop_center-center_none/whopper-thumb_2021-09-16-125319_mppe.png?mtime=20210916125320&focal=none&tmtime=20241024164409",
        "categoria": "carne"
    },
    {
        "nome": "Whopper",
        "valor": 29.90,
        "ingredientes": [
            {"nome": "Hambúrguer grelhado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Tomate", "quantidade": 2},
            {"nome": "Picles", "quantidade": 4},
            {"nome": "Cebola", "quantidade": 2}
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/_800x600_crop_center-center_none/whopper-thumb_2021-09-16-125319_mppe.png?mtime=20210916125320&focal=none&tmtime=20241024164409",
        "categoria": "carne"
    },
    {
        "nome": "Whopper",
        "valor": 29.90,
        "ingredientes": [
            {"nome": "Hambúrguer grelhado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Tomate", "quantidade": 2},
            {"nome": "Picles", "quantidade": 4},
            {"nome": "Cebola", "quantidade": 2}
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/_800x600_crop_center-center_none/whopper-thumb_2021-09-16-125319_mppe.png?mtime=20210916125320&focal=none&tmtime=20241024164409",
        "categoria": "carne"
    },
    {
        "nome": "Whopper",
        "valor": 29.90,
        "ingredientes": [
            {"nome": "Hambúrguer grelhado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Tomate", "quantidade": 2},
            {"nome": "Picles", "quantidade": 4},
            {"nome": "Cebola", "quantidade": 2}
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/_800x600_crop_center-center_none/whopper-thumb_2021-09-16-125319_mppe.png?mtime=20210916125320&focal=none&tmtime=20241024164409",
        "categoria": "carne"
    },
    {
        "nome": "Whopper",
        "valor": 29.90,
        "ingredientes": [
            {"nome": "Hambúrguer grelhado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Tomate", "quantidade": 2},
            {"nome": "Picles", "quantidade": 4},
            {"nome": "Cebola", "quantidade": 2}
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/_800x600_crop_center-center_none/whopper-thumb_2021-09-16-125319_mppe.png?mtime=20210916125320&focal=none&tmtime=20241024164409",
        "categoria": "carne"
    },
    {
        "nome": "Whopper",
        "valor": 29.90,
        "ingredientes": [
            {"nome": "Hambúrguer grelhado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
            {"nome": "Tomate", "quantidade": 2},
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
            {"nome": "Frango empanado", "quantidade": 1},
            {"nome": "Alface", "quantidade": 2},
        ],
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/BK-Chicken-Crispy-thumb.png?mtime=20230125075509&focal=none",
        "categoria": "frango"
    },
    {
        "nome": "Fries",
        "valor": 12.90,
        "tamanhos": [
            {"nome": "Pequeno", "preco": 8.90},
            {"nome": "Médio", "preco": 12.90},
            {"nome": "Grande", "preco": 15.90}
        ],
        "imagem": "https://compote.slate.com/images/c72f30b4-4e25-46dc-b1f4-b6a7063b3d56.jpeg?width=780&height=520&rect=1558x1039&offset=2x0",
        "categoria": "acompanhamentos"
    },
    {
        "nome": "Nuggets",
        "valor": 19.90,
        "tamanhos": [
            {"nome": "4 Peças", "preco": 12.90},
            {"nome": "6 Peças", "preco": 19.90},
            {"nome": "10 Peças", "preco": 25.90}
        ],
        "imagem": "https://wp-cdn.typhur.com/wp-content/uploads/2025/02/air-fryer-frozen-chicken-nuggets.jpg",
        "categoria": "frango"
    },
    {
        "nome": "Combo 1",
        "valor": 39.90,
        "combo_componentes": {
            "hamburguer": [
                {"nome": "Whopper", "valor": 29.90},
                {"nome": "Chicken", "valor": 24.90}
            ],
            "bebida": [
                {"nome": "Soda", "valor": 9.90},
                {"nome": "Shake", "valor": 14.90}
            ],
            "acompanhamento": [
                {"nome": "Fries", "valor": 12.90},
                {"nome": "Nuggets", "valor": 19.90}
            ]
        },
        "imagem": "https://d3sn2rlrwxy0ce.cloudfront.net/1-C-Chicken-Crispy-app-thumb-cupom-m-d.png?mtime=20230703165033&focal=none",
        "categoria": "combos"
    },
    {
        "nome": "Combo 2",
        "valor": 44.90,
        "combo_componentes": {
            "hamburguer": [
                {"nome": "Whopper", "valor": 29.90},
                {"nome": "Chicken", "valor": 24.90}
            ],
            "bebida": [
                {"nome": "Soda", "valor": 9.90},
                {"nome": "Shake", "valor": 14.90}
            ],
            "acompanhamento": [
                {"nome": "Fries", "valor": 12.90},
                {"nome": "Nuggets", "valor": 19.90}
            ],
            "brinquedo": [
                {"nome": "Sonic", "valor": 5.00},
                {"nome": "Tails", "valor": 5.00},
                {"nome": "Knuckles", "valor": 5.00}
            ]
        },
        "imagem": "https://instagram.fcgr3-1.fna.fbcdn.net/v/t51.29350-15/449314986_934419321772947_3975521562287087351_n.jpg?stp=dst-jpg_e35_p750x750_sh0.08_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fcgr3-1.fna.fbcdn.net&_nc_cat=103&_nc_oc=Q6cZ2QHrzhr51NOy97gX3Z4krJuocKx9SQnkfgkCDwsAUTmfDHPTMxtrweP7o5Jj8Omnutg&_nc_ohc=6EgoMPH5Y6kQ7kNvwHaaJEe&_nc_gid=4baxSiTj_DTF2vm3b827Jg&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfKadY0oXtHi-c2RsF7LDQUT56W9gGawaAHtUPPOA6KVXQ&oe=683E8DA7&_nc_sid=d885a2",
        "categoria": "combos"
    },
    {
        "nome": "Soda",
        "valor": 9.90,
        "tamanhos": [
            {"nome": "Pequeno", "preco": 7.90},
            {"nome": "Médio", "preco": 9.90},
            {"nome": "Grande", "preco": 11.90}
        ],
        "imagem": "https://upload.wikimedia.org/wikipedia/commons/e/e8/15-09-26-RalfR-WLC-0098_-_Coca-Cola_glass_bottle_%28Germany%29.jpg",
        "categoria": "bebidas_sobremesas"
    },
    {
        "nome": "Shake",
        "valor": 14.90,
        "tamanhos": [
            {"nome": "Pequeno", "preco": 10.90},
            {"nome": "Médio", "preco": 14.90},
            {"nome": "Grande", "preco": 17.90}
        ],
        "imagem": "https://static.itdg.com.br/images/1200-630/ee9c780da91c8377e7f6a10f30c6c1da/milk-shake-caseiro.jpg",
        "categoria": "bebidas_sobremesas"
    },
    {
        "nome": "Dessert",
        "valor": 7.90,
        "tamanhos": [
            {"nome": "Pequeno", "preco": 5.90},
            {"nome": "Médio", "preco": 7.90},
            {"nome": "Grande", "preco": 9.90}
        ],
        "imagem": "https://images.rappi.com.br/restaurants_background/sobremesas_burger_king-1662576783697.jpg?e=webp&d=700x100&q=10",
        "categoria": "bebidas_sobremesas"
    },
]

def main(page: ft.Page):
    controller = Controller_user()
    categoria = page.route.split("/")[-1] if page.route.startswith("/pedidos/") else "carne"
    itens_filtrados = [item for item in itens_lanche if item.get("categoria") == categoria]

    carrinho_itens = page.session.get("carrinho_itens")
    if carrinho_itens is None:
        carrinho_itens = []
        page.session.set("carrinho_itens", carrinho_itens)

    def voltar(e):
        page.go("/tipo_pedido")

    def logout():
        page.session.remove("user_id") if page.session.contains_key("user_id") else None
        page.session.remove("user_name") if page.session.contains_key("user_name") else None
        page.session.set("carrinho_itens", [])
        page.go("/")
        page.update()

    def atualizar_carrinho():
        carrinho_lista.controls.clear()
        total = 0
        for item in carrinho_itens:
            total += item["valor"]
            ingredientes_texto = ", ".join([f"{ing['nome']} ({ing['quantidade']})" for ing in item.get("ingredientes", [])])
            combo_texto = ", ".join([f"{k}: {v}" for k, v in item.get("combo_selecoes", {}).items() if v and k != "brinquedo"]) + (f", Brinquedo: {item['combo_selecoes']['brinquedo']}" if item.get("combo_selecoes", {}).get("brinquedo") else "") if item.get("combo_selecoes") else ""
            tamanho_texto = f"Tamanho: {item.get('tamanho', '')}" if item.get("tamanho") else ""
            detalhes_texto = ", ".join(filter(None, [ingredientes_texto, combo_texto, tamanho_texto]))
            carrinho_lista.controls.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.FASTFOOD, color=ft.Colors.ORANGE_700, size=24),
                            ft.Column(
                                controls=[
                                    ft.Text(f"{item['nome']}", weight=ft.FontWeight.BOLD, size=16),
                                    ft.Text(f"R${item['valor']:.2f}", color=ft.Colors.GREY_700, size=14),
                                    ft.Text(f"Detalhes: {detalhes_texto}", size=12, color=ft.Colors.GREY_600, italic=True) if detalhes_texto else ft.Text(""),
                                ],
                                spacing=5,
                                expand=True
                            ),
                            ft.IconButton(
                                icon=ft.icons.DELETE_OUTLINE,
                                icon_color=ft.Colors.RED_400,
                                on_click=lambda e, item_id=item["id"]: remover_item(item_id)
                            ),
                            ft.IconButton(
                                icon=ft.icons.EDIT_OUTLINED,
                                icon_color=ft.Colors.BLUE_400,
                                on_click=lambda e, item_id=item["id"]: editar_lanche(item_id)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    bgcolor=ft.Colors.WHITE,
                    padding=10,
                    border_radius=10,
                    margin=ft.margin.only(bottom=8),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=5,
                        color=ft.Colors.BLACK12,
                        offset=ft.Offset(0, 2)
                    )
                )
            )
        carrinho_lista.controls.append(
            ft.Container(
                content=ft.Text(f"Total: R${total:.2f}", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.BLACK),
                padding=10,
                alignment=ft.alignment.center_right
            )
        )
        page.session.set("carrinho_itens", carrinho_itens)
        page.update()

    def remover_item(item_id):
        carrinho_itens[:] = [item for item in carrinho_itens if item["id"] != item_id]
        atualizar_carrinho()

    def editar_lanche(item_id):
        page.go(f"/Editar_Pedido/{item_id}")
        page.update()

    def on_botao_click(e):
        item_nome = e.control.content.controls[1].content.value
        item_original = next((i for i in itens_lanche if i["nome"] == item_nome), None)
        if item_original:
            item_carrinho = copy.deepcopy(item_original)
            item_carrinho["id"] = str(uuid.uuid4())
            carrinho_itens.append(item_carrinho)
            atualizar_carrinho()

    def finalizar_pedido(e):
        if carrinho_itens:
            user_name = page.session.get("user_name") if page.session.contains_key("user_name") else "Anônimo"
            user_id = page.session.get("user_id") if page.session.contains_key("user_id") else None
            total = 0
            nota_fiscal_id = str(uuid.uuid4())[:8]
            nota_fiscal_str = f"NotaFiscalID: {nota_fiscal_id}\nCliente: {user_name}\nItens:\n"

            print("=== Nota Fiscal ===")
            print(f"Cliente: {user_name}")
            print(f"Nota Fiscal: {nota_fiscal_id}")
            print("-" * 30)
        
            itens_str = []
            for item in carrinho_itens:
                total += item["valor"]
                ingredientes_texto = ", ".join([f"{ing['nome']} ({ing['quantidade']})" for ing in item.get("ingredientes", [])]) if item.get("ingredientes") else "Sem ingredientes adicionais"
                combo_texto = ", ".join([f"{k}: {v}" for k, v in item.get("combo_selecoes", {}).items() if v and k != "brinquedo"]) + (f", Brinquedo: {item['combo_selecoes']['brinquedo']}" if item.get("combo_selecoes", {}).get("brinquedo") else "") if item.get("combo_selecoes") else ""
                tamanho_texto = f"Tamanho: {item.get('tamanho', '')}" if item.get("tamanho") else ""
                detalhes_texto = ", ".join(filter(None, [ingredientes_texto, combo_texto, tamanho_texto]))
            
                # Adicionar item à string com separador interno (por exemplo, ;)
                item_str = f"{item['nome']};R${item['valor']:.2f};{detalhes_texto}"
                itens_str.append(item_str)
            
                print(f"Item: {item['nome']}")
                print(f"Valor: R${item['valor']:.2f}")
                print(f"Detalhes: {detalhes_texto}")
                print("-" * 30)
        
            # Concatenar itens com quebras de linha
            nota_fiscal_str += "\n".join(itens_str) + f"\nTotal: R${total:.2f}"
        
            print(f"Total do Pedido: R${total:.2f}")
            print("====================================================================================")
        
            if user_id:
                try:
                    controller.DB.adicionar_historico(user_id, nota_fiscal_str)
                except Exception as e:
                    print(f"Erro ao salvar no histórico: {str(e)}")
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text(f"Erro ao salvar histórico: {str(e)}", color=ft.Colors.WHITE),
                        bgcolor=ft.Colors.RED_600
                    )
                    page.snack_bar.open = True

            page.snack_bar = ft.SnackBar(
                content=ft.Text("Pedido finalizado com sucesso!", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.GREEN_600
            )
            page.snack_bar.open = True
            carrinho_itens.clear()
            atualizar_carrinho()
            logout()
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Carrinho vazio!", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.RED_600
            )
            page.snack_bar.open = True
            page.update()

    botao_voltar = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        icon_color=ft.Colors.WHITE,
        bgcolor=ft.Colors.ORANGE_700,
        on_click=voltar,
        tooltip="Voltar",
        style=ft.ButtonStyle(
            shape=ft.CircleBorder(),
            padding=10,
        )
    )

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
        height=750,
        width=page.window.width - 40,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    imagem_topo = ft.Image(
        src="./assets/Header/Header.png",
        fit=ft.ImageFit.COVER,
    )

    carrinho_lista = ft.Column(
        controls=[],
        scroll=ft.ScrollMode.AUTO,
        height=400,
        width=page.window.width - 40,
        spacing=0
    )
    carrinho_lista_container = ft.Container(
        content=carrinho_lista,
        bgcolor=ft.Colors.GREY_100,
        padding=15,
        border_radius=15,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.Colors.BLACK,
            offset=ft.Offset(0, 4)
        )
    )

    carrinho = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.SHOPPING_CART, color=ft.Colors.ORANGE_700, size=28),
                        ft.Text("Seu Carrinho", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10
                ),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
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
                        bgcolor=ft.Colors.GREEN_600,
                        color=ft.Colors.WHITE,
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
        bgcolor=ft.Colors.WHITE,
        padding=ft.padding.only(left=20, right=20, top=20, bottom=20),
        width=page.window.width,
        border_radius=ft.border_radius.only(top_left=20, top_right=20),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.Colors.BLACK,
            offset=ft.Offset(0, -2)
        )
    )

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
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            ft.Container(content=carrinho, margin=ft.margin.only(top=160))
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    atualizar_carrinho()

    return ft.View(
        route=f"/pedidos/{categoria}",
        controls=[conteudo],
        bgcolor=ft.Colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.START,
        padding=0
    )

if __name__ == "__main__":
    ft.app(target=main)