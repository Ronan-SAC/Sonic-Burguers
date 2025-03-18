import flet as ft

def criar_teclados(add_to_input, backspace, clear, hide_keyboard):
    button_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10),
        side=ft.BorderSide(width=2, color=ft.Colors.BLACK)
    )

    numeric_keyboard = ft.Column(
        [
            ft.Row(
                [ft.ElevatedButton(text=str(i), on_click=add_to_input, width=65, height=65,
                                 bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                 style=button_style)
                 for i in [7, 8, 9]],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            ft.Row(
                [ft.ElevatedButton(text=str(i), on_click=add_to_input, width=65, height=65,
                                 bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                 style=button_style)
                 for i in [4, 5, 6]],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            ft.Row(
                [ft.ElevatedButton(text=str(i), on_click=add_to_input, width=65, height=65,
                                 bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                 style=button_style)
                 for i in [1, 2, 3]],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            ft.Row(
                [
                    ft.ElevatedButton(text="Apagar", on_click=backspace, width=65, height=65,
                                    bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                    style=button_style),
                    ft.ElevatedButton(text="0", on_click=add_to_input, width=65, height=65,
                                    bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                    style=button_style),
                    ft.ElevatedButton(text="Limpar", on_click=clear, width=65, height=65,
                                    bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                    style=button_style),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
        ],
        visible=False,
        spacing=10,
    )
    
    full_keyboard = ft.Column(
        [
            ft.Row(
                [ft.ElevatedButton(text=char, on_click=add_to_input, width=55, height=55,
                                 bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                 style=button_style)
                 for char in "1234567890"],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [ft.ElevatedButton(text=char, on_click=add_to_input, width=55, height=55,
                                 bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                 style=button_style)
                 for char in "QWERTYUIOP"],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [ft.ElevatedButton(text=char, on_click=add_to_input, width=55, height=55,
                                 bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                 style=button_style)
                 for char in "ASDFGHJKL"],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [ft.ElevatedButton(text=char, on_click=add_to_input, width=55, height=55,
                                 bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                 style=button_style)
                 for char in "ZXCVBNM"],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.ElevatedButton(text="Apagar", on_click=backspace, width=80, height=40,
                                    bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                    style=button_style),
                    ft.ElevatedButton(text="Limpar", on_click=clear, width=80, height=40,
                                    bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE,
                                    style=button_style),
                    ft.ElevatedButton(text="Fechar", on_click=hide_keyboard, width=80, height=40,
                                    bgcolor=ft.Colors.RED_600, color=ft.Colors.WHITE,
                                    style=button_style),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        visible=False,
        spacing=5,
    )

    return numeric_keyboard, full_keyboard