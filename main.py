# main.py
import flet as ft
from Views.Home import main as home_main  # Importa a tela inicial

def main(page: ft.Page):
    home_main(page)  # Chama a função que renderiza a tela inicial

ft.app(target=main)
