import flet as ft
from components.keyboards import criar_teclados
from components.utils import validar_cpf
from Controllers.UsersControllers import Controller_user

def main(page: ft.Page):
    controller = Controller_user()
    keyboard = criar_teclados(page)
    
    def show_keyboard(field, keyboard_type):
        page.campo_ativo = field
        if keyboard_type == "numeric":
            keyboard.numeric_keyboard.visible = True
            keyboard.full_keyboard.visible = False
        else:
            keyboard.numeric_keyboard.visible = False
            keyboard.full_keyboard.visible = True
        page.update()

    logo = ft.Image(src="assets/icons/MainLogo.png", width=650, height=650)
    mensagem = ft.Text("", color=ft.Colors.BLACK, size=32)

    CPF_TEXT = ft.TextField(
        label="Digite seu CPF",
        width=825,
        border_radius=10,
        border_color=ft.Colors.BLUE_900,
        focused_border_color=ft.Colors.YELLOW_400,
        text_style=ft.TextStyle(color=ft.Colors.WHITE, font_family="Arial"),
        bgcolor=ft.Colors.BLUE_700,
        icon=ft.Icons.SPEED,
        read_only=True,
        on_focus=lambda e: show_keyboard(CPF_TEXT, "numeric"),
        max_length=14
    )
    
    Senha = ft.TextField(
        label="Digite sua senha",
        password=True,
        can_reveal_password=True,
        width=825,
        border_radius=10,
        border_color=ft.Colors.BLUE_900,
        focused_border_color=ft.Colors.YELLOW_400,
        text_style=ft.TextStyle(color=ft.Colors.WHITE, font_family="Arial"),
        bgcolor=ft.Colors.BLUE_700,
        icon=ft.Icons.LOCK,
        read_only=True,
        on_focus=lambda e: show_keyboard(Senha, "full")
    )

    def on_login_click(e):
        cpf_limpo = ''.join(filter(str.isdigit, CPF_TEXT.value))
        if not CPF_TEXT.value or not Senha.value:
            mensagem.value = "Por favor, preencha CPF e senha"
            mensagem.color = ft.Colors.RED
        elif len(cpf_limpo) != 11:
            mensagem.value = "CPF deve ter 11 dígitos"
            mensagem.color = ft.Colors.RED
        elif not validar_cpf(cpf_limpo):
            mensagem.value = "CPF inválido"
            mensagem.color = ft.Colors.RED
        else:
            try:
                success, result = controller.verificar(cpf_limpo, Senha.value)
                if success:
                    page.session.set("user_id", result["id_user"])
                    page.session.set("user_name", result["nome"])
                    mensagem.value = "Login bem-sucedido!"
                    mensagem.color = ft.Colors.GREEN
                    page.go("/tipo_pedido")
                else:
                    mensagem.value = result
                    mensagem.color = ft.Colors.RED
            except Exception as e:
                mensagem.value = f"Erro ao verificar login: {str(e)}"
                mensagem.color = ft.Colors.RED
        page.update()

    Logar = ft.ElevatedButton(
        "Correr!",
        bgcolor=ft.Colors.RED_600,
        color=ft.Colors.WHITE,
        width=400,
        height=50,
        elevation=8,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=on_login_click,
    )

    voltar_button = ft.ElevatedButton(
        "Voltar",
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
        width=350,
        height=50,
        elevation=8,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=lambda e: page.go("/home"),
    )

    login_form = ft.Column(
        controls=[
            logo,
            CPF_TEXT,
            Senha,
            ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.DIRECTIONS_RUN, color=ft.Colors.GREY_700, size=36),
                    Logar,
                    voltar_button
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Container(height=5),
            mensagem,
            keyboard.numeric_keyboard,
            keyboard.full_keyboard,
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    return ft.View(
        route="/login",
        controls=[login_form],
        bgcolor=ft.Colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )

if __name__ == "__main__":
    ft.app(target=main)