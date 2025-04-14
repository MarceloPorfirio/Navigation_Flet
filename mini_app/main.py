import flet as ft
import sys
from pathlib import Path



# Configuração do caminho
sys.path.append(str(Path(__file__).parent))

def main(page: ft.Page):
    # Configurações da página (idênticas ao original)
    page.bgcolor = ft.colors.BLUE_200
    # page.theme_mode = "dark"
    page.title = "Navegações"
    page.window_width = 450
    page.window_height = 700
    page.window_maximizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    # Importações dentro da função main para evitar problemas
    from pages.home import view as home_view
    from pages.edit import view as edit_view
    from pages.notes import view as notes_view
    from pages.todo import view as todo_view
    # from pages.dashboard import view as dashboard_view
    from pages.settings import view as settings_view
    from pages.suport import view as support_view

    # Controle principal
    current_view = ft.Ref[ft.Container]()

    def create_icon_button(icon, view_name):
        return ft.IconButton(
            icon=icon,
            on_click=lambda e: change_view(view_name),
            icon_color="blue",  # Cor única para todos
        )
    
    def change_view(view_name):
        views = {
                "home": lambda: home_view(change_view, page),
                "edit": lambda: edit_view(change_view,page),
                "notes": lambda: notes_view(change_view,page),
                "todo": lambda: todo_view(change_view,page),
                "settings": lambda: settings_view(change_view,page),
                "support": lambda: support_view(change_view,page),
            }

        
        if view_name in views:
            current_view.current.content = views[view_name]()
            page.update()

    # Configuração inicial
    current_view.current = ft.Container(
        content=home_view(change_view,page),
        width=400,
        height=550,
        bgcolor="white",
        border_radius=16,
        shadow=ft.BoxShadow(blur_radius=10, color='black')
    )

    # Barra inferior (idêntica ao original)
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor="#f6f6f6",
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                create_icon_button(ft.icons.EDIT, "edit"),
                create_icon_button(ft.icons.SETTINGS, "settings"),
                ft.Container(expand=True),
                create_icon_button(ft.icons.NOTE_ADD, "notes"),
                create_icon_button(ft.icons.CHECKLIST, "todo"),
                create_icon_button(ft.icons.HELP, "support"),
            ]
        )
    )

       # Botão flutuante centralizado
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.HOME,
        on_click=lambda e: change_view("home"),
        bgcolor='blue'
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.add(current_view.current)
ft.app(target=main)