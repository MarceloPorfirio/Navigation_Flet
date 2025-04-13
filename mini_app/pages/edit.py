import flet as ft

def view(navigate_to):
    def salvar_dados(e):
        if not nome_input.value.strip():
            # Se não houver nome, apenas retorna sem salvar
            return

        # Criar e abrir o dialog
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Boas-vindas!"),
            content=ft.Text(f"Bem-vindo, {nome_input.value}!"),
            actions=[
                ft.TextButton("OK", on_click=lambda e: (
                    e.page.close(dialog),
                    navigate_to("home")
                ))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        # Adiciona o dialog na página
        dialog.open = True
         # Atualiza a página para garantir que o dialog seja mostrado
    # Campos do formulário
    nome_input = ft.TextField(
        label="Nome completo",
        hint_text="Digite seu nome",
        border_color=ft.colors.GREY_400,
        capitalization=ft.TextCapitalization.WORDS,
        on_focus=True,
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
                ft.Text("Editar Perfil", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                ft.Divider(height=20),
                nome_input,
                email_input,
                idade_input,
                endereco_input,
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
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
