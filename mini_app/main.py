import flet as ft
import sys
from pathlib import Path

# Configuração do caminho
sys.path.append(str(Path(__file__).parent))

def main(page: ft.Page):
    # Configurações da página (idênticas ao original)
    page.bgcolor = ft.colors.BLUE_200
    page.theme_mode = "dark"
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

    def change_view(view_name):
        views = {
            "home": home_view,
            "edit": edit_view,
            "notes": notes_view,
            "todo": todo_view,
            # "dashboard": dashboard_view,
            "settings": settings_view,
            "support": support_view
        }
        
        if view_name in views:
            current_view.current.content = views[view_name](change_view)
            page.update()

    # Configuração inicial
    current_view.current = ft.Container(
        content=home_view(change_view),
        width=400,
        height=550,
        bgcolor="white",
        border_radius=16,
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(0.2, 'black'))
    )

    # Barra inferior (idêntica ao original)
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor="#f6f6f6ff",
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e: change_view("edit")),
                ft.IconButton(icon=ft.icons.SETTINGS, on_click=lambda e: change_view("settings")),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.NOTE_ADD, on_click=lambda e: change_view("notes")),
                ft.IconButton(icon=ft.icons.CHECKLIST, on_click=lambda e: change_view("todo")),
                ft.IconButton(icon=ft.icons.HELP, on_click=lambda e: change_view("support")),
            ]
        )
    )

    # Botão flutuante (idêntico ao original)
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.HOME,
        on_click=lambda e: change_view("home"),
        bgcolor='blue'
    )

    page.add(current_view.current)

ft.app(target=main)