import flet as ft
import requests

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

    def btn_preferencias(e):
        _stack_main.controls.clear()
        _stack_main.controls.append(preferencias)
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

    def mostrar_bem_vindo(e):
        nome_digitado = nome_input.value
        bem_vindo_text.value = f"Bem-vindo, {nome_digitado}!"
        page.update()

    def salvar_preferencias(e):
        tema_selecionado = tema_opcoes.value
        cor_selecionada = cor_opcoes.value
        notificacoes = "ativadas" if notificacoes_toggle.value else "desativadas"

        # Configurando o Snackbar
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Preferências salvas!\nTema: {tema_selecionado}\nCor: {cor_selecionada}\nNotificações: {notificacoes}"),
            bgcolor=ft.colors.GREEN,
        )
        page.snack_bar.open = True  # Ativando o Snackbar
        page.update()  # Atualizando a página para refletir a mudança


    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor='blue',on_click=btn_principal)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor="#f6f6f6ff",
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.EDIT,icon_color=ft.colors.BLUE,icon_size=28,on_click=btn_editar),
                ft.IconButton(icon=ft.icons.SETTINGS,icon_color=ft.colors.BLUE,icon_size=28,on_click=btn_preferencias),
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
        content=ft.Column(
            alignment="center",
            controls=[
                ft.Text(value="Bem-vindo ao Mini App!", color="black", size=28, weight="bold"),
                ft.Text(value="Explore as funcionalidades disponíveis abaixo.", color=ft.colors.GREY_500, size=16),
                ft.ElevatedButton(text="Começar", bgcolor=ft.colors.BLUE, color="white",on_click=btn_editar),
            ]
        )
        
    )

    nome_input = ft.TextField(label="Nome", hint_text="Digite o novo nome",color='black')
    email_input = ft.TextField(label="Email", hint_text="Digite o novo email",color='black')
    bem_vindo_text = ft.Text(value="", color="blue", size=20)

    editar = ft.Container(
    width=400,
    height=550,
    bgcolor="white",
    border_radius=16,
    padding=20,
    shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.1, color="black")),
    content=ft.Column(
        alignment="center",
        spacing=20,
        controls=[
            ft.Row(
                controls=[
                    ft.Text("Dados pessoais", size=24, weight="bold",color='black'),
                ],alignment='center'
            ),
            
            nome_input,email_input,
            ft.Row(
                controls=[
                    ft.ElevatedButton("Salvar", icon=ft.icons.SAVE, bgcolor=ft.colors.GREEN, on_click=mostrar_bem_vindo),
                ],alignment='center'
            ),
            bem_vindo_text
            
        ],
    ),
)
    



    # Container Preferências
    tema_opcoes = ft.Dropdown(
        width=300,
        label="Tema",
        hint_text="Selecione o tema do app",
        options=[
            ft.dropdown.Option("Claro"),
            ft.dropdown.Option("Escuro")
        ],
    )

    cor_opcoes = ft.Dropdown(
        width=300,
        label="Cor de Destaque",
        hint_text="Escolha sua cor favorita",
        options=[
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Amarelo"),
        ],
    )

    notificacoes_toggle = ft.Switch(label="Ativar Notificações", value=True)

    preferencias = ft.Container(
        width=400,
        height=550,
        bgcolor="white",
        border_radius=16,
        padding=20,
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.2, color="black")),
        content=ft.Column(
            alignment="start",
            spacing=20,
            controls=[
                ft.Text(value="Preferências do Usuário", size=24, weight="bold", color="black"),
                tema_opcoes,
                cor_opcoes,
                notificacoes_toggle,
                ft.ElevatedButton(
                    "Salvar Preferências",
                    icon=ft.icons.SAVE,
                    bgcolor=ft.colors.GREEN,
                    on_click=lambda e: salvar_preferencias(e),
                ),
            ],
        ),
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
            value='Aqui vai novo menu',
            color='black',
            size=32
        )
        
    )

    # Container Dashboard Compacto
    compartilhar = ft.Container(
        width=400,
        height=550,
        bgcolor="white",
        border_radius=16,
        padding=20,
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.2, color="black")),
        content=ft.Column(
            alignment="start",
            spacing=20,
            controls=[
                ft.Text(
                    value="Aqui vai novo menu",
                    color="black",
                    size=24,
                    weight="bold",
                    text_align="center",
                ),
            ]
        )
    )


    _stack_main = ft.Stack(
        controls=[
            _main
        ]
    )

    page.add(_stack_main)

ft.app(target=main)