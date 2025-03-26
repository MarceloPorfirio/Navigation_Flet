import flet as ft

def view(navigate_to):
    # Variáveis para armazenar as configurações
    tema_selecionado = "Escuro"
    cor_selecionada = "Azul"
    notificacoes_ativas = True

    # Componentes da UI
    tema_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Claro"),
            ft.dropdown.Option("Escuro"),
            ft.dropdown.Option("Sistema")
        ],
        value=tema_selecionado,
        width=200,
        border_color=ft.colors.GREY_400,
        on_change=lambda e: set_tema(e.control.value)
    )

    cor_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Amarelo"),
            ft.dropdown.Option("Roxo")
        ],
        value=cor_selecionada,
        width=200,
        border_color=ft.colors.GREY_400,
        on_change=lambda e: set_cor(e.control.value)
    )

    notificacoes_switch = ft.Switch(
        value=notificacoes_ativas,
        active_color=ft.colors.BLUE,
        on_change=lambda e: set_notificacoes(e.control.value)
    )

    status_text = ft.Text("", color=ft.colors.GREEN_600)

    # Funções para atualizar as configurações
    def set_tema(tema):
        nonlocal tema_selecionado
        tema_selecionado = tema

    def set_cor(cor):
        nonlocal cor_selecionada
        cor_selecionada = cor

    def set_notificacoes(ativas):
        nonlocal notificacoes_ativas
        notificacoes_ativas = ativas

    def salvar_configuracoes(e):
        # Aqui você pode adicionar a lógica para aplicar as configurações
        # Exemplo: page.theme_mode = tema_selecionado.lower()
        
        status_text.value = (
            f"Configurações salvas!\n"
            f"Tema: {tema_selecionado}\n"
            f"Cor: {cor_selecionada}\n"
            f"Notificações: {'Ativadas' if notificacoes_ativas else 'Desativadas'}"
        )
        status_text.color = ft.colors.GREEN_600
        status_text.update()

    return ft.Container(
        width=400,
        height=550,
        bgcolor=ft.colors.WHITE,
        padding=20,
        border_radius=10,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                # Cabeçalho
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            icon_color=ft.colors.BLACK,
                            on_click=lambda e: navigate_to("home")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                
                ft.Text("Configurações", 
                       size=24,
                       weight=ft.FontWeight.BOLD,
                       color=ft.colors.BLACK),
                
                ft.Divider(height=20),
                
                # Seção de Aparência
                ft.Text("Aparência", size=18, weight=ft.FontWeight.BOLD),
                
                ft.Row(
                    controls=[
                        ft.Text("Tema:", width=100),
                        tema_dropdown
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                
                ft.Row(
                    controls=[
                        ft.Text("Cor:", width=100),
                        cor_dropdown
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                
                ft.Divider(height=20),
                
                # Seção de Notificações
                ft.Text("Notificações", size=18, weight=ft.FontWeight.BOLD),
                
                ft.Row(
                    controls=[
                        ft.Text("Receber notificações:", width=150),
                        notificacoes_switch
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                
                ft.Divider(height=30),
                
                # Botão de salvar
                ft.ElevatedButton(
                    "Salvar Configurações",
                    icon=ft.icons.SAVE,
                    on_click=salvar_configuracoes,
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLUE_700,
                        color=ft.colors.WHITE,
                        padding={"left": 30, "right": 30, "top": 15, "bottom": 15},
                        elevation=2
                    ),
                    width=300
                ),
                
                status_text
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )