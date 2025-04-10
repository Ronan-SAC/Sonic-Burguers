import flet as ft
from components.keyboards import criar_teclados
from components.utils import validar_nome, validar_telefone, validar_cpf, validar_senha

def main(page: ft.Page):
    # Initialize keyboard
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

    # UI Elements
    logo = ft.Image(src="assets/icons/MainLogo.png", width=650, height=650)
    mensagem = ft.Text("", color=ft.Colors.BLACK, size=32)

    # Input Fields
    Nome = ft.TextField(
        label="Digite seu Nome Completo",
        width=825,
        border_radius=10,
        border_color=ft.Colors.BLUE_900,
        focused_border_color=ft.Colors.YELLOW_400,
        text_style=ft.TextStyle(color=ft.Colors.WHITE, font_family="Arial"),
        bgcolor=ft.Colors.BLUE_700,
        icon=ft.Icons.PERSON,
        read_only=True,
        on_focus=lambda e: show_keyboard(Nome, "full")
    )

    Telefone = ft.TextField(
        label="Digite seu Telefone",
        width=825,
        border_radius=10,
        border_color=ft.Colors.BLUE_900,
        focused_border_color=ft.Colors.YELLOW_400,
        text_style=ft.TextStyle(color=ft.Colors.WHITE, font_family="Arial"),
        bgcolor=ft.Colors.BLUE_700,
        icon=ft.Icons.PHONE,
        read_only=True,
        on_focus=lambda e: show_keyboard(Telefone, "numeric"),
        max_length=15  
    )

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

    def on_sign_click(e):
        # Validações (removendo a máscara antes de validar)
        nome_valido, msg_nome = validar_nome(Nome.value)
        telefone_valido, msg_telefone = validar_telefone(''.join(filter(str.isdigit, Telefone.value)))
        cpf_valido, msg_cpf = validar_cpf(''.join(filter(str.isdigit, CPF_TEXT.value)))
        senha_valido, msg_senha = validar_senha(Senha.value)

        if not Nome.value or not Telefone.value or not CPF_TEXT.value or not Senha.value:
            mensagem.value = "Por favor, preencha todos os campos"
            mensagem.color = ft.Colors.RED
        elif not nome_valido:
            mensagem.value = msg_nome
            mensagem.color = ft.Colors.RED
        elif not telefone_valido:
            mensagem.value = msg_telefone
            mensagem.color = ft.Colors.RED
        elif not cpf_valido:
            mensagem.value = msg_cpf
            mensagem.color = ft.Colors.RED
        elif not senha_valido:
            mensagem.value = msg_senha
            mensagem.color = ft.Colors.RED
        else:
            mensagem.value = "Conta criada com sucesso!"
            mensagem.color = ft.Colors.GREEN
            page.go("/menu")
        page.update()

    # Buttons
    Logar = ft.ElevatedButton(
        "Criar Conta!",
        bgcolor=ft.Colors.RED_600,
        color=ft.Colors.WHITE,
        width=400,
        height=50,
        elevation=8,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        tooltip="Criar nova conta",
        on_click=on_sign_click
    )

    voltar_home = ft.ElevatedButton(
        "Voltar",
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
        width=350,
        height=50,
        elevation=8,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=lambda e: page.go("/home"),
        tooltip="Voltar para a tela inicial",
    )

    # Layout
    sign_form = ft.Column(
        controls=[
            logo,
            Nome,
            Telefone,
            CPF_TEXT,
            Senha,
            ft.Row(
                controls=[
                    ft.Icon(name=ft.Icons.DIRECTIONS_RUN, color=ft.Colors.GREY_700, size=36),
                    Logar,
                    voltar_home
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

    # Initially hide keyboards
    keyboard.numeric_keyboard.visible = False
    keyboard.full_keyboard.visible = False

    return ft.View(
        route="/sign",
        controls=[sign_form],
        bgcolor=ft.Colors.AMBER_100,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )

if __name__ == "__main__":
    ft.app(target=main)