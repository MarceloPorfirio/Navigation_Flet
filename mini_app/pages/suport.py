import flet as ft
from datetime import datetime

def view(page: ft.Page):
    # Campo de feedback
    feedback_text = ft.TextField(
        multiline=True,
        min_lines=4,
        max_lines=6,
        hint_text="Descreva seu feedback, dúvida ou problema...",
        border_color=ft.colors.BLUE_300,
        focused_border_color=ft.colors.BLUE_700,
        filled=True,
        fill_color=ft.colors.GREY_50,
        text_size=14,
        capitalization=ft.TextCapitalization.SENTENCES,
    )

    # Variável para armazenar a avaliação selecionada
    selected_rating = 0
    hover_rating = 0

    # Componente de avaliação com estrelas interativas
    stars = [ft.Icon(ft.icons.STAR_BORDER, color=ft.colors.AMBER) for _ in range(5)]
    rating = ft.Text("0/5", color=ft.colors.GREY_600)
    
    def update_stars():
        """Atualiza a aparência das estrelas com base no hover ou seleção"""
        current_rating = hover_rating if hover_rating > 0 and selected_rating == 0 else selected_rating
        for i in range(5):
            stars[i].name = ft.icons.STAR if i < current_rating else ft.icons.STAR_BORDER
        rating.value = f"{selected_rating}/5"
        rating.update()
        for star in stars:
            star.update()

    def star_enter(e):
        """Quando o mouse entra em uma estrela"""
        nonlocal hover_rating
        idx = stars.index(e.control)
        hover_rating = idx + 1
        update_stars()
    
    def star_leave(e):
        """Quando o mouse sai de uma estrela"""
        nonlocal hover_rating
        hover_rating = 0
        update_stars()
    
    def star_click(e):
        """Quando clica em uma estrela"""
        nonlocal selected_rating
        idx = stars.index(e.control)
        selected_rating = idx + 1
        hover_rating = 0  # Reseta o hover após seleção
        update_stars()
    
    # Configura os eventos para cada estrela
    for star in stars:
        star.on_enter = star_enter
        star.on_exit = star_leave
        star.on_click = star_click

    
    def handle_hover(e):
        """Lida com o evento de hover"""
        idx = stars.index(e.control)
        if selected_rating == 0:  # Só mostra hover se nenhuma estrela foi selecionada
            update_stars(idx)
    
    def handle_hover_leave(e):
        """Lida com o evento de saída do hover"""
        if selected_rating == 0:  # Volta ao estado inicial se nenhuma estrela foi selecionada
            update_stars()
        else:  # Mantém a seleção
            update_stars()
    
    def handle_click(e):
        """Lida com o clique para selecionar a avaliação"""
        nonlocal selected_rating
        idx = stars.index(e.control)
        selected_rating = idx + 1
        update_stars()
    
    # Configura os eventos para cada estrela
    for star in stars:
        star.on_hover = handle_hover
        star.on_hover_leave = handle_hover_leave
        star.on_click = handle_click

    # Diálogo de confirmação
    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Obrigado!"),
        content=ft.Text("Seu feedback foi enviado com sucesso."),
        actions=[
            ft.TextButton("OK", on_click=lambda e: close_dialog(e)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def open_dialog(e):
        # Verifica se há texto no feedback antes de enviar
        if not feedback_text.value:
            feedback_text.error_text = "Por favor, digite seu feedback"
            feedback_text.update()
            return
        
        # Aqui você pode adicionar a lógica para enviar o feedback
        print(f"Feedback enviado: {feedback_text.value}")
        print(f"Avaliação: {rating.value}")
        
        # Limpa os campos após o envio
        feedback_text.value = ""
        feedback_text.error_text = None
        feedback_text.update()
        
        # Reseta a avaliação
        nonlocal selected_rating
        selected_rating = 0
        update_stars()
        
        # Abre o diálogo de confirmação
        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()

    def close_dialog(e):
        confirm_dialog.open = False
        page.update()

    # Layout principal (o mesmo que antes)
    support_view = ft.Container(
        width=400,
        height=550,
        padding=20,
        border_radius=16,
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            spacing=20,
            controls=[
                # Cabeçalho
                ft.Column(
                    spacing=5,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.SUPPORT_AGENT, size=28, color=ft.colors.BLUE_700),
                                ft.Text("Suporte", size=24, weight=ft.FontWeight.BOLD),
                            ],
                            spacing=10
                        ),
                        ft.Text(f"Versão 1.0.0 • {datetime.now().year}", color=ft.colors.GREY_600, size=12),
                        ft.Divider(height=10),
                    ]
                ),
                
                # Seção de contato
                ft.Column(
                    spacing=8,
                    controls=[
                        ft.Text("Contato", size=16, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.EMAIL, size=18, color=ft.colors.BLUE_500),
                                ft.Text("suporte@meuapp.com", color=ft.colors.BLUE_600),
                            ],
                            spacing=10
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.PHONE, size=18, color=ft.colors.BLUE_500),
                                ft.Text("(11) 98765-4321", color=ft.colors.BLUE_600),
                            ],
                            spacing=10
                        ),
                        ft.Divider(height=20),
                    ]
                ),
                
                # Seção de feedback
                ft.Column(
                    spacing=8,
                    controls=[
                        ft.Text("Feedback", size=16, weight=ft.FontWeight.BOLD),
                        ft.Text("Sua opinião é importante para melhorarmos!", size=12, color=ft.colors.GREY_600),
                        feedback_text,
                        ft.ElevatedButton(
                            "Enviar Feedback",
                            icon=ft.icons.SEND,
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLUE_600,
                            on_click=open_dialog,
                            width=200,
                            height=40,
                        ),
                        ft.Divider(height=20),
                    ]
                ),
                
                # Seção de avaliação
                ft.Column(
                    spacing=8,
                    controls=[
                        ft.Text("Avalie nosso app", size=16, weight=ft.FontWeight.BOLD),
                        ft.Row(
                            controls=stars + [rating],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Text("Passe o mouse e clique para avaliar", size=12, color=ft.colors.GREY_600),
                    ]
                ),
                
                # Rodapé
                ft.Column(
                    spacing=5,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Divider(),
                        ft.Text("© 2023 MeuApp Inc.", size=12, color=ft.colors.GREY_500),
                        ft.Text("Todos os direitos reservados", size=10, color=ft.colors.GREY_400),
                    ]
                )
            ]
        )
    )

    return support_view