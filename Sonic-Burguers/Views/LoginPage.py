# views/login.py
import flet as ft
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mysql.connector
from components.keyboards import criar_teclados
from components.utils import validar_e_formatar_cpf

def main(page: ft.Page):
    page.window.maximizable = False
    page.title = "SonicBurger - Login"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.AMBER_100
    page.window.width = 1080
    page.window.height = 2000
    page.window.resizable = False
    page.window.center()

    logo = ft.Image(src="../assets/icons/MainLogo.png")
    mensagem = ft.Text("", color=ft.Colors.BLACK, size=32)

    def on_login_click(e):
        cpf_valido, cpf_resultado = validar_e_formatar_cpf(CPF_TEXT.value)
        CPF_TEXT.value = cpf_resultado
        if cpf_valido:
            mensagem.value = "Corrida concluída!"
            mensagem.color = ft.Colors.GREEN
            page.controls.clear()
        else:
            mensagem.value = "CPF inválido"
            mensagem.color = ft.Colors.RED
        page.update()

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
    )
    Senha = ft.TextField(
        label="Digite sua senha",
        password=True,
        width=825,
        border_radius=10,
        border_color=ft.Colors.BLUE_900,
        focused_border_color=ft.Colors.YELLOW_400,
        text_style=ft.TextStyle(color=ft.Colors.WHITE, font_family="Arial"),
        bgcolor=ft.Colors.BLUE_700,
        icon=ft.Icons.LOCK,
        read_only=True,
    )

    campo_ativo = None

    def add_to_input(e):
        char = e.control.text
        if campo_ativo == CPF_TEXT:
            CPF_TEXT.value += char
            valido, resultado = validar_e_formatar_cpf(CPF_TEXT.value)
            CPF_TEXT.value = resultado
            if len(''.join(filter(str.isdigit, CPF_TEXT.value))) == 11:
                if valido:
                    CPF_TEXT.border_color = ft.Colors.GREEN
                    mensagem.value = "CPF válido!"
                    mensagem.color = ft.Colors.GREEN
                else:
                    CPF_TEXT.border_color = ft.Colors.RED
                    mensagem.value = "CPF inválido"
                    mensagem.color = ft.Colors.RED
            else:
                CPF_TEXT.border_color = ft.Colors.BLUE_900
                mensagem.value = ""
        elif campo_ativo == Senha:
            Senha.value += char
        page.update()

    def backspace(e):
        if campo_ativo == CPF_TEXT:
            CPF_TEXT.value = CPF_TEXT.value[:-1]
            valido, resultado = validar_e_formatar_cpf(CPF_TEXT.value)
            CPF_TEXT.value = resultado
            if len(''.join(filter(str.isdigit, CPF_TEXT.value))) < 11:
                CPF_TEXT.border_color = ft.Colors.BLUE_900
                mensagem.value = ""
            else:
                if valido:
                    CPF_TEXT.border_color = ft.Colors.GREEN
                    mensagem.value = "CPF válido!"
                    mensagem.color = ft.Colors.GREEN
                else:
                    CPF_TEXT.border_color = ft.Colors.RED
                    mensagem.value = "CPF inválido"
                    mensagem.color = ft.Colors.RED
        elif campo_ativo == Senha:
            Senha.value = Senha.value[:-1]
        page.update()

    def clear(e):
        if campo_ativo == CPF_TEXT:
            CPF_TEXT.value = ""
            CPF_TEXT.border_color = ft.Colors.BLUE_900
            mensagem.value = ""
        elif campo_ativo == Senha:
            Senha.value = ""
        page.update()

    def hide_keyboard(e):
        numeric_keyboard.visible = False
        full_keyboard.visible = False
        page.update()

    numeric_keyboard, full_keyboard = criar_teclados(add_to_input, backspace, clear, hide_keyboard)

    def show_keyboard(e):
        nonlocal campo_ativo
        campo_ativo = e.control
        if campo_ativo == CPF_TEXT:
            numeric_keyboard.visible = True
            full_keyboard.visible = False
        elif campo_ativo == Senha:
            full_keyboard.visible = True
            numeric_keyboard.visible = False
        page.update()

    CPF_TEXT.on_click = show_keyboard
    Senha.on_click = show_keyboard

    Logar = ft.ElevatedButton(
        "Correr!",
        bgcolor=ft.Colors.RED_600,
        color=ft.Colors.WHITE,
        width=790,
        height=50,
        elevation=8,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=on_login_click,
        tooltip="Corrida concluída",
    )

    running_icon = ft.Icon(name=ft.Icons.DIRECTIONS_RUN, color=ft.Colors.GREY_700, size=36)

    button_row = ft.Row(
        controls=[running_icon, Logar],
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    login_form = ft.Column(
        controls=[
            logo,
            CPF_TEXT,
            Senha,
            button_row,
            ft.Container(height=5),
            mensagem,
            numeric_keyboard,
            full_keyboard,
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(login_form)
    page.update()

# Não chamar ft.app aqui, pois será chamado por Home.py