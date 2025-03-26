import flet as ft

def view(navigate_to):
    # Componentes do formulário
    nome_input = ft.TextField(
        label="Nome completo",
        hint_text="Digite seu nome",
        border_color=ft.colors.GREY_400,
        capitalization=ft.TextCapitalization.WORDS
    )
    
    email_input = ft.TextField(
        label="Email",
        hint_text="seu@email.com",
        border_color=ft.colors.GREY_400,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    
    idade_input = ft.TextField(
        label="Idade",
        hint_text="Digite sua idade",
        border_color=ft.colors.GREY_400,
        keyboard_type=ft.KeyboardType.NUMBER,
        input_filter=ft.NumbersOnlyInputFilter(),
        max_length=3
    )
    
    endereco_input = ft.TextField(
        label="Endereço completo",
        hint_text="Rua, número, complemento",
        border_color=ft.colors.GREY_400,
        multiline=True,
        min_lines=2,
        max_lines=4
    )

    # Componente de feedback
    status_text = ft.Text("", color=ft.colors.GREEN_600)

    def salvar_dados(e):
        # Validação básica
        if not nome_input.value.strip():
            status_text.value = "Nome é obrigatório!"
            status_text.color = ft.colors.RED
            status_text.update()
            return
            
        # Dados coletados (apenas para demonstração)
        dados = {
            "nome": nome_input.value,
            "email": email_input.value,
            "idade": idade_input.value,
            "endereco": endereco_input.value
        }
        
        # Feedback visual
        status_text.value = f"Dados salvos!\nNome: {dados['nome']}"
        status_text.color = ft.colors.GREEN_600
        status_text.update()

        # Volta para home
        navigate_to("home")

    return ft.Container(
        width=400,
        height=550,
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(20),
        border_radius=10,
        border=ft.border.all(1, ft.colors.GREY_300),
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
                
                ft.Text("Editar Perfil", 
                       size=24,
                       weight=ft.FontWeight.BOLD,
                       color=ft.colors.BLACK),
                
                ft.Divider(height=20),
                
                # Campos do formulário
                nome_input,
                email_input,
                idade_input,
                endereco_input,
                
                # Botão de salvar
                ft.ElevatedButton(
                    "Salvar Alterações",
                    icon=ft.icons.SAVE,
                    on_click=salvar_dados,
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