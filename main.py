# main.py
import flet as ft
from Views.Interlude import interlude_page as interlude  # Importa a tela inicial

def main(page: ft.Page):
    interlude(page)  # Chama a função que renderiza a tela inicial

ft.app(target=main)