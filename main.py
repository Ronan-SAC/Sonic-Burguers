# main.py
import flet as ft
from Views.Home import main as home_main  

def main(page: ft.Page):
    home_main(page)  

ft.app(target=main)
