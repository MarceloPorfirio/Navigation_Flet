import flet as ft


def main(page:ft.Page):
    page.bgcolor = ft.colors.BLUE_200
    page.theme_mode = "dark"
    page.title = "Navegações"
    page.window_width = 450
    page.window_height = 700
    page.window_maximizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    def btn_editar(e):
        _stack_main.controls.clear()
        _stack_main.controls.append(editar)
        _stack_main.update()

    def btn_pesquisar(e):
        _stack_main.controls.clear()
        _stack_main.controls.append(pesquisar)
        _stack_main.update()

    def btn_principal(e):
        _stack_main.controls.clear()
        _stack_main.controls.append(_main)
        _stack_main.update()

    def btn_config(e):
        _stack_main.controls.clear()
        _stack_main.controls.append(configurar)
        _stack_main.update()
    
    def btn_compartilhar(e):
        _stack_main.controls.clear()
        _stack_main.controls.append(compartilhar)
        _stack_main.update()

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor='blue',on_click=btn_principal)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor="#f6f6f6ff",
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,icon_size=28,on_click=btn_editar),
                ft.IconButton(icon=ft.icons.SEARCH,icon_color=ft.colors.BLUE,icon_size=28,on_click=btn_pesquisar),
                ft.Container(expand = True),
                ft.IconButton(icon=ft.icons.MENU,icon_color=ft.colors.BLUE,icon_size=28,on_click=btn_config),
                ft.IconButton(icon=ft.icons.MENU,icon_color=ft.colors.BLUE,icon_size=28,on_click=btn_compartilhar ),

            ]
        )
    )

    # Container Principal
    _main = ft.Container(
        width=400,
        height=550,
        bgcolor="white",
        alignment=ft.alignment.center,
        border_radius=16,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.2,color='black')),
        content=ft.Text(
            value='Inicio',
            color='black',
            size=32
        )
        
    )

    # Container Editar
    editar = ft.Container(
        width=400,
        height=550,
        bgcolor="white",
        alignment=ft.alignment.center,
        border_radius=16,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.2,color='black')),
        content=ft.Text(
            value='Editar',
            color='black',
            size=32
        )
        
    )

    # Container Pesquisar
    pesquisar = ft.Container(
        width=400,
        height=550,
        bgcolor="white",
        alignment=ft.alignment.center,
        border_radius=16,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.2,color='black')),
        content=ft.Text(
            value='Pesquisar',
            color='black',
            size=32
        )
        
    )

    # Container Configurar
    configurar = ft.Container(
        width=400,
        height=550,
        bgcolor="white",
        alignment=ft.alignment.center,
        border_radius=16,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.2,color='black')),
        content=ft.Text(
            value='Configurar',
            color='black',
            size=32
        )
        
    )

    # Container Compartilhar
    compartilhar = ft.Container(
        width=400,
        height=550,
        bgcolor="white",
        alignment=ft.alignment.center,
        border_radius=16,
        shadow=ft.BoxShadow(blur_radius=10,color=ft.colors.with_opacity(opacity=0.2,color='black')),
        content=ft.Text(
            value='Compartilhar',
            color='black',
            size=32
        )
        
    )

    _stack_main = ft.Stack(
        controls=[
            _main
        ]
    )

    page.add(_stack_main)

ft.app(target=main)