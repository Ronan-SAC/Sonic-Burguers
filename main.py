# main.py
import flet as ft
from Views.Home import main as home_main
from Views.LoginPage import main as login_main 
from Views.SignUp import main as sign_main

def main(page: ft.Page):
    page.title = "Toten Sonic Burguers"
    
    page.title = "SonicBurger - Criar Conta"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.AMBER_500
    page.window.width = 1080
    page.window.height = 1920 
    page.window.resizable = False
    page.window.center()
    page.window.maximizable = False
    page.window.full_screen = True
    page.padding = 0
    
    def route_change(route):
       
        page.views.clear()
        
        route_handlers = {
            "/": home_main,
            "/login": login_main,
            "/sign": sign_main
        }
        
        view_handler = route_handlers.get(page.route, home_main)
        page.views.append(view_handler(page))
        page.update() 

    def view_pop(view):
        if len(page.views) > 1:  
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    page.go(page.route if page.route else "/")

if __name__ == "__main__":
    ft.app(target=main)