import flet as ft
from datetime import datetime

def view(page: ft.Page):  # Recebemos a página como parâmetro
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

    # Componente de avaliação com estrelas interativas
    stars = [ft.Icon(ft.icons.STAR_BORDER, color=ft.colors.AMBER) for _ in range(5)]
    rating = ft.Text("0/5", color=ft.colors.GREY_600)
    
    def rate_app(e, index):
        for i in range(5):
            stars[i].name = ft.icons.STAR if i <= index else ft.icons.STAR_BORDER
        rating.value = f"{index+1}/5"
        rating.update()
        for star in stars:
            star.update()
    
    for i, star in enumerate(stars):
        star.on_click = lambda e, idx=i: rate_app(e, idx)

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
        for i in range(5):
            stars[i].name = ft.icons.STAR_BORDER
        rating.value = "0/5"
        for star in stars:
            star.update()
        rating.update()
        
        # Abre o diálogo de confirmação
        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()

    def close_dialog(e):
        confirm_dialog.open = False
        page.update()

    # Layout principal
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
                        ft.Text("Toque nas estrelas para avaliar", size=12, color=ft.colors.GREY_600),
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