import flet as ft

def view(navigate_to,page):
    # Variáveis para armazenar as configurações
    tema_selecionado = "Escuro"
    cor_selecionada = "Azul"
    notificacoes_ativas = True

    # Dividers com variáveis distintas
    div_aparencia = ft.Divider(height=20)
    div_cor = ft.Divider(height=20)
    div_notificacoes = ft.Divider(height=20)

    # Função para aplicar as configurações
    def aplicar_configuracoes():
        # Aplica o tema visual localmente
        if tema_selecionado == "Claro":
            container.bgcolor = ft.colors.WHITE
            tema_text.color = ft.colors.BLACK
            titulo_aparencia.color = ft.colors.BLACK
            titulo_notificacoes.color = ft.colors.BLACK
            tema_label.color = ft.colors.BLACK
            cor_label.color = ft.colors.BLACK
            notificacoes_label.color = ft.colors.BLACK
            tema_dropdown.text_color = ft.colors.BLACK
            cor_dropdown.text_color = ft.colors.BLACK
        elif tema_selecionado == "Escuro":
            container.bgcolor = ft.colors.BLACK
            tema_text.color = ft.colors.WHITE
            titulo_aparencia.color = ft.colors.WHITE
            titulo_notificacoes.color = ft.colors.WHITE
            tema_label.color = ft.colors.WHITE
            cor_label.color = ft.colors.WHITE
            notificacoes_label.color = ft.colors.WHITE
            tema_dropdown.text_color = ft.colors.WHITE
            cor_dropdown.text_color = ft.colors.WHITE
        elif tema_selecionado == "Sistema":
            container.bgcolor = ft.colors.SURFACE_VARIANT
            tema_text.color = ft.colors.PRIMARY
            titulo_aparencia.color = ft.colors.PRIMARY
            titulo_notificacoes.color = ft.colors.PRIMARY
            tema_label.color = ft.colors.PRIMARY
            cor_label.color = ft.colors.PRIMARY
            notificacoes_label.color = ft.colors.PRIMARY
            tema_dropdown.text_color = ft.colors.PRIMARY
            cor_dropdown.text_color = ft.colors.PRIMARY

        # Define função auxiliar para aplicar a cor primária
        def aplicar_cor_primaria(cor):
            tema_text.color = cor
            titulo_aparencia.color = cor
            titulo_notificacoes.color = cor
            tema_label.color = cor
            cor_label.color = cor
            notificacoes_label.color = cor
            tema_dropdown.color = cor
            cor_dropdown.color = cor
            div_aparencia.color = cor
            div_cor.color = cor
            div_notificacoes.color = cor

        if cor_selecionada == "Azul":
            aplicar_cor_primaria(ft.colors.BLUE_700)
        elif cor_selecionada == "Verde":
            aplicar_cor_primaria(ft.colors.GREEN_700)
        elif cor_selecionada == "Vermelho":
            aplicar_cor_primaria(ft.colors.RED_700)
        elif cor_selecionada == "Amarelo":
            aplicar_cor_primaria(ft.colors.YELLOW_700)
        elif cor_selecionada == "Roxo":
            aplicar_cor_primaria(ft.colors.DEEP_PURPLE_700)

        container.update()

    # Componentes da UI
    tema_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Claro"),
            ft.dropdown.Option("Escuro"),
            ft.dropdown.Option("Sistema")
        ],
        color=cor_selecionada,
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
        color=cor_selecionada,
        width=200,
        border_color=ft.colors.GREY_400,
        on_change=lambda e: set_cor(e.control.value)
    )

    notificacoes_switch = ft.Switch(
        value=notificacoes_ativas,
        active_color=ft.colors.BLUE,
        on_change=lambda e: set_notificacoes(e.control.value)
    )

    # Funções para atualizar as configurações
    def set_tema(tema):
        nonlocal tema_selecionado
        tema_selecionado = tema
        aplicar_configuracoes()

    def set_cor(cor):
        nonlocal cor_selecionada
        cor_selecionada = cor
        aplicar_configuracoes()

    def set_notificacoes(ativas):
        nonlocal notificacoes_ativas
        notificacoes_ativas = ativas
        aplicar_configuracoes()

    # Título da seção "Aparência"
    tema_text = ft.Text("Configurações", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)

    titulo_aparencia = ft.Text("Aparência", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)
    titulo_notificacoes = ft.Text("Notificações", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)

    tema_label = ft.Text("Tema", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)
    cor_label = ft.Text("Cor", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)
    notificacoes_label = ft.Text("Receber notificações", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)

    container = ft.Container(
        width=400,
        height=500,
        bgcolor=ft.colors.WHITE,
        padding=20,
        border_radius=10,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                tema_text,
                div_aparencia,
                titulo_aparencia,
                tema_label,
                tema_dropdown,
                div_cor,
                cor_label,
                cor_dropdown,
                div_notificacoes,
                titulo_notificacoes,
                notificacoes_label,
                notificacoes_switch
            ]
        )
    )

    return container
