import flet as ft
from datetime import datetime

def view(navigate_to,page):
    # Variáveis para armazenar as notas
    notas = []
    nota_input = ft.TextField(
        hint_text="Digite sua nota...",
        multiline=True,
        min_lines=3,
        max_lines=5,
        border_color=ft.colors.GREY_400,
        expand=True
    )

    # Lista de notas (ListView para scroll)
    notas_list = ft.ListView(expand=True, spacing=10)

    def adicionar_nota(e):
        if nota_input.value.strip():
            nota = {
                "texto": nota_input.value,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            notas.append(nota)
            nota_input.value = ""
            atualizar_lista_notas()
            nota_input.focus()
            nota_input.update()

    def deletar_nota(index):
        notas.pop(index)
        atualizar_lista_notas()

    def atualizar_lista_notas():
        notas_list.controls.clear()
        for i, nota in enumerate(notas):
            notas_list.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(nota["texto"]),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            nota["data"],
                                            size=12,
                                            color=ft.colors.GREY_600
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            icon_color=ft.colors.RED,
                                            tooltip="Excluir nota",
                                            on_click=lambda e, idx=i: deletar_nota(idx)
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                )
                            ],
                            spacing=5
                        ),
                        padding=10
                    ),
                    elevation=2
                )
            )
        notas_list.update()

    return ft.Container(
        width=400,
        height=550,
        bgcolor=ft.colors.WHITE,
        padding=20,
        border_radius=10,
        content=ft.Column(
            controls=[
                # Cabeçalho
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            icon_color=ft.colors.BLACK,
                            on_click=lambda e: navigate_to("home")
                        ),
                        ft.Text("Notas Rápidas", 
                               size=24,
                               weight=ft.FontWeight.BOLD,
                               expand=True)
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                
                ft.Divider(height=20),
                
                # Área de entrada
                nota_input,
                
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Adicionar Nota",
                            icon=ft.icons.ADD,
                            on_click=adicionar_nota,
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.BLUE_700,
                                color=ft.colors.WHITE,
                                padding=15
                            )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END
                ),
                
                ft.Divider(height=20),
                
                # Título da lista
                ft.Text("Suas Notas", size=18, weight=ft.FontWeight.BOLD),
                
                # Lista de notas
                notas_list
            ],
            spacing=15
        )
    )