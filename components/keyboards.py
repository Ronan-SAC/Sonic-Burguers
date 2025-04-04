import flet as ft

def criar_teclados(page):
    """Cria e retorna teclados numérico e completo estilizados"""
    
    # Cores e estilos consistentes com o tema
    BG_COLOR = ft.colors.BLUE_700
    KEY_COLOR = ft.colors.AMBER_500
    TEXT_COLOR = ft.colors.WHITE
    SPECIAL_KEY_COLOR = ft.colors.RED_600
    KEY_WIDTH = 80
    KEY_HEIGHT = 60
    KEY_RADIUS = 10
    
    def add_to_input(e):
        if hasattr(page, 'campo_ativo') and page.campo_ativo:
            char = e.control.data if hasattr(e.control, 'data') else e.control.text
            # Special case for "Espaço" to add a space character
            if char == "Espaço":
                char = " "
            page.campo_ativo.value += char
            page.update()

    def backspace(e):
        if hasattr(page, 'campo_ativo') and page.campo_ativo and page.campo_ativo.value:
            page.campo_ativo.value = page.campo_ativo.value[:-1]
            page.update()

    def clear(e):
        if hasattr(page, 'campo_ativo') and page.campo_ativo:
            page.campo_ativo.value = ""
            page.update()

    def hide_keyboard(e):
        numeric_keyboard.visible = False
        full_keyboard.visible = False
        page.update()

    def create_key_button(key, is_special=False, custom_width=None):
        return ft.Container(
            content=ft.Text(
                key,
                size=24,
                weight=ft.FontWeight.BOLD,
                color=TEXT_COLOR,
            ),
            width=custom_width if custom_width else KEY_WIDTH,
            height=KEY_HEIGHT,
            alignment=ft.alignment.center,
            bgcolor=SPECIAL_KEY_COLOR if is_special else KEY_COLOR,
            border_radius=ft.border_radius.all(KEY_RADIUS),
            animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_OUT),
            on_click=backspace if key == '⌫' else 
                   clear if key == 'Limpar' else 
                   add_to_input,
            data=key,
            on_hover=lambda e: (
                setattr(e.control, "bgcolor", ft.colors.AMBER_400 if e.data == "true" else 
                       (SPECIAL_KEY_COLOR if is_special else KEY_COLOR)),
                e.control.update()
            )
        )

    # Teclado numérico estilizado com botão "Limpar"
    numeric_keys = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['Limpar', '0', '⌫']
    ]
    
    # Teclado completo estilizado com botão "Espaço" maior
    full_keys = [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '⌫'],
        ['Espaço', 'Limpar']
    ]

    def create_keyboard(keys):
        rows = []
        for row in keys:
            cols = []
            for key in row:
                is_special = key in ['⌫', 'Limpar']
                custom_width = 400 if key == 'Espaço' else None
                cols.append(create_key_button(key, is_special, custom_width))
            rows.append(
                ft.Row(
                    cols,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5
                )
            )
        
        # Botão "X" para fechar o teclado
        close_button = ft.Container(
            content=ft.Text(
                "X",
                size=24,
                weight=ft.FontWeight.BOLD,
                color=TEXT_COLOR,
            ),
            width=40,
            height=40,
            alignment=ft.alignment.center,
            bgcolor=SPECIAL_KEY_COLOR,
            border_radius=ft.border_radius.all(20),
            on_click=hide_keyboard,
            on_hover=lambda e: (
                setattr(e.control, "bgcolor", ft.colors.AMBER_400 if e.data == "true" else SPECIAL_KEY_COLOR),
                e.control.update()
            )
        )

        # Usar Column em vez de Stack para evitar sobreposição
        keyboard_content = ft.Column(
            controls=[
                ft.Row(
                    controls=[close_button],
                    alignment=ft.MainAxisAlignment.END
                ),
                ft.Column(
                    rows,
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=5
        )

        return ft.Container(
            content=keyboard_content,
            padding=ft.padding.all(15),
            bgcolor=BG_COLOR,
            border_radius=ft.border_radius.only(
                top_left=20,
                top_right=20
            ),
            animate_opacity=300
        )

    numeric_keyboard = create_keyboard(numeric_keys)
    full_keyboard = create_keyboard(full_keys)
    
    # Esconde inicialmente
    numeric_keyboard.visible = False
    full_keyboard.visible = False

    class Keyboards:
        def __init__(self):
            self.numeric_keyboard = numeric_keyboard
            self.full_keyboard = full_keyboard

    return Keyboards()