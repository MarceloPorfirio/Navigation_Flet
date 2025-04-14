import flet as ft
from datetime import datetime

def view(navigate_to,page):
    # Variável de tarefas movida para dentro da função view
    tarefas = []

    nova_tarefa = ft.TextField(
        hint_text="O que precisa ser feito?",
        expand=True,
        border_color=ft.colors.GREY_400,
        on_submit=lambda e: adicionar_tarefa(e)
    )

    lista_tarefas = ft.ListView(expand=True, spacing=5)
    filtro_atual = ft.Ref[ft.Tabs]()

    def adicionar_tarefa(e):
        if nova_tarefa.value.strip():
            tarefas.append({
                "descricao": nova_tarefa.value,
                "completa": False,
                "data": datetime.now().strftime("%d/%m %H:%M")
            })
            nova_tarefa.value = ""
            nova_tarefa.focus()
            atualizar_lista()

    def alternar_status(index):
        tarefas[index]["completa"] = not tarefas[index]["completa"]
        atualizar_lista()

    def excluir_tarefa(index):
        tarefas.pop(index)
        atualizar_lista()

    def filtrar_tarefas(e):
        atualizar_lista()

    def limpar_completas(e):
        nonlocal tarefas  # Indica que estamos modificando a variável da função externa
        tarefas = [t for t in tarefas if not t["completa"]]
        atualizar_lista()

    def atualizar_lista():
        lista_tarefas.controls.clear()
        
        filtro = filtro_atual.current.tabs[filtro_atual.current.selected_index].text
        tarefas_filtradas = [
            t for t in tarefas
            if filtro == "Todas" or 
               (filtro == "Ativas" and not t["completa"]) or
               (filtro == "Completas" and t["completa"])
        ]

        for i, tarefa in enumerate(tarefas_filtradas):
            lista_tarefas.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        leading=ft.Checkbox(
                            value=tarefa["completa"],
                            on_change=lambda e, idx=i: alternar_status(idx)
                        ),
                        title=ft.Text(
                            tarefa["descricao"],
                            style=ft.TextStyle(
                                decoration=ft.TextDecoration.LINE_THROUGH 
                                if tarefa["completa"] else None
                            )
                        ),
                        subtitle=ft.Text(tarefa["data"], size=12),
                        trailing=ft.IconButton(
                            icon=ft.icons.DELETE,
                            on_click=lambda e, idx=i: excluir_tarefa(idx)
                        )
                    ),
                    bgcolor=ft.colors.GREY_100 if tarefa["completa"] else None,
                    border_radius=5,
                    padding=5
                )
            )
        
        lista_tarefas.update()

    return ft.Container(
        width=400,
        height=550,
        bgcolor=ft.colors.WHITE,
        padding=20,
        border_radius=10,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            icon_color=ft.colors.BLACK,
                            on_click=lambda e: navigate_to("home")
                        ),
                        ft.Text("Lista de Tarefas", 
                              size=24,
                              weight=ft.FontWeight.BOLD,
                              expand=True)
                    ]
                ),
                
                ft.Divider(height=20),
                
                ft.Row(
                    controls=[
                        nova_tarefa,
                        ft.IconButton(
                            icon=ft.icons.ADD,
                            icon_color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLUE_700,
                            on_click=adicionar_tarefa
                        )
                    ]
                ),
                
                ft.Tabs(
                    ref=filtro_atual,
                    selected_index=0,
                    on_change=filtrar_tarefas,
                    tabs=[
                        ft.Tab(text="Todas"),
                        ft.Tab(text="Ativas"),
                        ft.Tab(text="Completas")
                    ]
                ),
                
                lista_tarefas,
                
                ft.Row(
                    controls=[
                        ft.Text(f"{len([t for t in tarefas if not t['completa']])} itens restantes"),
                        ft.OutlinedButton(
                            text="Limpar completas",
                            on_click=limpar_completas
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ],
            spacing=15
        )
    )