import flet as ft
from Views.Home import main as home_main
from Views.LoginPage import main as login_main
from Views.SignUp import main as sign_main
from Views.Interlude import main as interlude_main
from Views.TipoPedido import main as tipo_pedido_main
from Views.PedidosCategoria import main as pedidos_categoria_main
from Views.Editar_Pedido import main as editar_pedido_main

def main(page: ft.Page):
    page.title = "Toten Sonic Burguers"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.AMBER_100
    page.window.width = 1080
    page.window.height = 1920
    page.window.resizable = False
    page.window.center()
    page.window.maximizable = False
    page.window.full_screen = True
    page.padding = 0
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            track_visibility=False,
            thumb_visibility=False,
            track_border_color=ft.Colors.BLUE,
            thumb_color={
                ft.ControlState.HOVERED: ft.Colors.AMBER_500,
                ft.ControlState.DEFAULT: ft.Colors.BLUE_700,
            },
            thickness=5,
            radius=10,
        )
    )
    def route_change(route):
        page.views.clear()
        
        route_handlers = {
            "/": interlude_main,
            "/home": home_main,
            "/login": login_main,
            "/sign": sign_main,
            "/tipo_pedido": tipo_pedido_main,
            "/pedidos/carne": pedidos_categoria_main,
            "/pedidos/frango": pedidos_categoria_main,
            "/pedidos/combos": pedidos_categoria_main,
            "/pedidos/acompanhamentos": pedidos_categoria_main,
            "/pedidos/bebidas_sobremesas": pedidos_categoria_main,
        }
        
        if page.route.startswith("/Editar_Pedido/"):
            view_handler = editar_pedido_main
        else:
            view_handler = route_handlers.get(page.route, home_main)
        
        new_view = view_handler(page)
        
        if new_view is None:
            print(f"Erro: view_handler retornou None para a rota {page.route}")
            new_view = ft.View(
                route=page.route,
                controls=[
                    ft.Text(f"Erro: View não encontrada para {page.route}", size=20, color=ft.Colors.RED)
                ],
                bgcolor=ft.Colors.AMBER_100,
                padding=20
            )
        
        new_view.padding = 0
        new_view.bgcolor = page.bgcolor
        page.views.append(new_view)
        page.update()

    def view_pop(view):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    page.go(page.route if page.route else "/tipo_pedido")

if __name__ == "__main__":
    ft.app(target=main)