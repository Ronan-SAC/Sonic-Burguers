import flet as ft
import os
import sys
import uuid
import copy
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components.Cards import botao_bk_style
from Controllers.UsersControllers import Controller_user

def main(page: ft.Page):
    controller = Controller_user()
    # Função para navegar para a página de pedidos da categoria
    def navegar_categoria(e):
        categoria = e.control.data  # Acessa o data do Container
        page.go(f"/pedidos/{categoria}")

    # Função para voltar
    def voltar(e):
        page.go("/home")  # Redireciona para a página inicial

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
            "imagem": "https://images.rappi.com.br/restaurants_background/sobremesas_burger_king-1662576783697.jpg?e=webp&d=700x100&q=10",  # Substitua pelo caminho real da imagem
            "data": "bebidas_sobremesas"
        },
    ]

    carrinho_itens = page.session.get("carrinho_itens")
    if carrinho_itens is None:
        carrinho_itens = []
        page.session.set("carrinho_itens", carrinho_itens)

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
            carrinho_lista.controls.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.FASTFOOD, color=ft.Colors.ORANGE_700, size=24),
                            ft.Column(
                                controls=[
                                    ft.Text(f"{item['nome']}", weight=ft.FontWeight.BOLD, size=16),
                                    ft.Text(f"R${item['valor']:.2f}", color=ft.Colors.GREY_700, size=14),
                                    ft.Text(f"Ingredientes: {ingredientes_texto}", size=12, color=ft.Colors.GREY_600, italic=True) if ingredientes_texto else ft.Text(""),
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

    def finalizar_pedido(e):
        if carrinho_itens:
            user_name = page.session.get("user_name") if page.session.contains_key("user_name") else "Anônimo"
            user_id = page.session.get("user_id") if page.session.contains_key("user_id") else None
            total = 0
            nota_fiscal = {
                "id": str(uuid.uuid4())[:8],
                "items": []
            }
            print("=== Nota Fiscal ===")
            print(f"Cliente: {user_name}")
            print(f"Nota Fiscal: {nota_fiscal['id']}")
            print("-" * 30)
            for item in carrinho_itens:
                total += item["valor"]
                ingredientes_texto = ", ".join([f"{ing['nome']} ({ing['quantidade']})" for ing in item.get("ingredientes", [])]) if item.get("ingredientes") else "Sem ingredientes adicionais"
                combo_texto = ", ".join([f"{k}: {v}" for k, v in item.get("combo_selecoes", {}).items() if v and k != "brinquedo"]) + (f", Brinquedo: {item['combo_selecoes']['brinquedo']}" if item.get("combo_selecoes", {}).get("brinquedo") else "") if item.get("combo_selecoes") else ""
                tamanho_texto = f"Tamanho: {item.get('tamanho', '')}" if item.get("tamanho") else ""
                detalhes_texto = ", ".join(filter(None, [ingredientes_texto, combo_texto, tamanho_texto]))
                print(f"Item: {item['nome']}")
                print(f"Valor: R${item['valor']:.2f}")
                print(f"Detalhes: {detalhes_texto}")
                print("-" * 30)
                nota_fiscal["items"].append({
                    "nome": item["nome"],
                    "valor": item["valor"],
                    "detalhes": detalhes_texto
                })
            print(f"Total do Pedido: R${total:.2f}")
            print("==================")
            
            if user_id:
                try:
                    cursor = controller.DB.conexao.cursor()
                    cursor.execute(
                        "INSERT INTO historico (id_user, nota_fiscal, preco_total) VALUES (%s, %s, %s)",
                        (user_id, json.dumps(nota_fiscal), total)
                    )
                    controller.DB.conexao.commit()
                    cursor.close()
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

    # Botão de voltar
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

    # Grid de botões de categorias usando botao_bk_style
    grid_categorias = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    botao_bk_style(
                        texto=categoria["nome"],
                        imagem_path=categoria["imagem"],
                        on_click=navegar_categoria,
                        largura=(page.window.width / 2 - 30),
                        altura=350,
                        cor_texto="white",
                        cor_fundo_texto="orange",
                        data=categoria["data"],
                    )
                    for categoria in categorias[i:i+2]
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER
            )
            for i in range(0, len(categorias), 2)
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        height=750,
        width=page.window.width - 40,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Imagem do topo
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
                padding=ft.padding.only(top=20, left=20, right=20),
                margin=ft.margin.only(bottom=0)
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

    # Estrutura final da view
    return ft.View(
        route="/tipo_pedido",
        controls=[conteudo],
        bgcolor=ft.Colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.START,
        padding=0
    )

if __name__ == "__main__":
    ft.app(target=main)