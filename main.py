import flet as ft
from datetime import datetime

class Task(ft.Column):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete
        self.display_task = ft.Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)

    def delete_clicked(self, e):
        self.task_delete(self)


class TodoApp(ft.Column):
    def __init__(self, back_to_main_callback, update_dashboard_callback):
        super().__init__()
        self.back_to_main = back_to_main_callback
        self.update_dashboard = update_dashboard_callback
        self.new_task = ft.TextField(
            hint_text="O que precisa ser feito?", on_submit=self.add_clicked, expand=True
        )
        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="todos"), ft.Tab(text="ativos"), ft.Tab(text="completos")],
        )

        self.items_left = ft.Text("0 itens restantes")

        self.controls = [
            ft.Row(
                [ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.back_to_main)],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Row(
                [ft.Text(value="Lista de Tarefas", style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD, on_click=self.add_clicked
                    ),
                ],
            ),
            ft.Column(
                spacing=25,
                controls=[
                    self.filter,
                    self.tasks,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            self.items_left,
                            ft.OutlinedButton(
                                text="Limpar completos", on_click=self.clear_clicked
                            ),
                        ],
                    ),
                ],
            ),
        ]

    def add_clicked(self, e):
        if self.new_task.value:
            task = Task(self.new_task.value, self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            self.new_task.focus()
            self.update()
            self.update_dashboard()

    def task_status_change(self, task):
        self.update()
        self.update_dashboard()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()
        self.update_dashboard()

    def tabs_changed(self, e):
        self.update()

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)

    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "todos"
                or (status == "ativos" and task.completed == False)
                or (status == "completos" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} item(s) ativo(s)"
        super().before_update()

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_200
    page.theme_mode = "dark"
    page.title = "Navegações"
    page.window_width = 450
    page.window_height = 700
    page.window_maximizable = False
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    # Variáveis para o Dashboard
    total_tasks = 0
    completed_tasks = 0
    pending_tasks = 0
    productivity = 0
    recent_activities = []

    def update_dashboard_stats():
        nonlocal total_tasks, completed_tasks, pending_tasks, productivity
        total_tasks = len(todo_app.tasks.controls)
        completed_tasks = sum(1 for task in todo_app.tasks.controls if task.completed)
        pending_tasks = total_tasks - completed_tasks
        productivity = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        # Atualiza os controles do dashboard
        dashboard_total.value = str(total_tasks)
        dashboard_completed.value = str(completed_tasks)
        dashboard_pending.value = str(pending_tasks)
        dashboard_productivity.value = f"{productivity:.0f}%"
        
        # Atualiza o gráfico
        line_chart.data[0].data_points = [
            ft.LineChartDataPoint(i, (i+3)*2) for i in range(1, 6)
        ]
        
        # Atualiza atividades recentes
        if len(recent_activities) > 3:
            recent_activities.pop(0)
        activities_list.controls = [
            ft.ListTile(title=ft.Text(activity)) for activity in recent_activities
        ]
        
        dashboard.update()

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
        _stack_main.controls.append(todo_container)
        _stack_main.update()
        update_dashboard_stats()
    
    def btn_compartilhar(e):
        _stack_main.controls.clear()
        _stack_main.controls.append(dashboard_container)
        _stack_main.update()
        update_dashboard_stats()

    def mostrar_bem_vindo(e):
        nome_digitado = nome_input.value
        bem_vindo_text.value = f"Bem-vindo, {nome_digitado}!"
        page.update()

    def salvar_preferencias(e):
        tema_selecionado = tema_opcoes.value
        cor_selecionada = cor_opcoes.value
        notificacoes = "ativadas" if notificacoes_toggle.value else "desativadas"

        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Preferências salvas!\nTema: {tema_selecionado}\nCor: {cor_selecionada}\nNotificações: {notificacoes}"),
            bgcolor=ft.colors.GREEN,
        )
        page.snack_bar.open = True
        page.update()

    # Configuração da barra inferior
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        bgcolor='blue',
        on_click=btn_principal
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor="#f6f6f6ff",
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.EDIT, icon_color=ft.colors.BLUE, icon_size=28, on_click=btn_editar),
                ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.BLUE, icon_size=28, on_click=btn_preferencias),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.CHECKLIST, icon_color=ft.colors.BLUE, icon_size=28, on_click=btn_config),
                ft.IconButton(icon=ft.icons.ANALYTICS, icon_color=ft.colors.BLUE, icon_size=28, on_click=btn_compartilhar),
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
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(opacity=0.2, color='black')),
        content=ft.Column(
            alignment="center",
            controls=[
                ft.Text(value="Bem-vindo ao Mini App!", color="black", size=28, weight="bold"),
                ft.Text(value="Explore as funcionalidades disponíveis abaixo.", color=ft.colors.GREY_500, size=16),
                ft.ElevatedButton(text="Começar", bgcolor=ft.colors.BLUE, color="white", on_click=btn_editar),
            ]
        )
    )

    # Componentes para outras telas (editar, preferências)
    nome_input = ft.TextField(label="Nome", hint_text="Digite o novo nome", color='black')
    email_input = ft.TextField(label="Email", hint_text="Digite o novo email", color='black')
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
                ft.Row(controls=[ft.Text("Dados pessoais", size=24, weight="bold", color='black')], alignment='center'),
                nome_input, email_input,
                ft.Row(controls=[ft.ElevatedButton("Salvar", icon=ft.icons.SAVE, bgcolor=ft.colors.GREEN, on_click=mostrar_bem_vindo)], alignment='center'),
                bem_vindo_text
            ],
        ),
    )
    
    tema_opcoes = ft.Dropdown(
        width=300,
        label="Tema",
        hint_text="Selecione o tema do app",
        options=[ft.dropdown.Option("Claro"), ft.dropdown.Option("Escuro")],
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
                    on_click=salvar_preferencias,
                ),
            ],
        ),
    )

    # Container do To-Do App
    todo_app = TodoApp(btn_principal, update_dashboard_stats)
    todo_container = ft.Container(
        width=400,
        height=550,
        bgcolor="white",
        border_radius=16,
        padding=20,
        content=todo_app
    )

    # Componentes do Dashboard
    dashboard_total = ft.Text("0", size=32, weight="bold")
    dashboard_completed = ft.Text("0", size=32, weight="bold")
    dashboard_pending = ft.Text("0", size=32, weight="bold")
    dashboard_productivity = ft.Text("0%", size=20)
    
    line_chart = ft.LineChart(
        data_series=[
            ft.LineChartData(
                data_points=[ft.LineChartDataPoint(i, (i+3)*2) for i in range(1, 6)],
                stroke_width=3,
                color=ft.colors.BLUE
            )
        ],
        left_axis=ft.ChartAxis(labels_size=40),
        bottom_axis=ft.ChartAxis(labels_size=40),
        width=350,
        height=200
    )
    
    activities_list = ft.ListView(height=150)
    
    dashboard = ft.Column(
        controls=[
            ft.Row(
                [ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=btn_principal)],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Row(
                [ft.Text(value="Dashboard", style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        width=110,
                        height=110,
                        bgcolor=ft.colors.BLUE_100,
                        border_radius=10,
                        padding=10,
                        content=ft.Column(
                            alignment="center",
                            horizontal_alignment="center",
                            controls=[
                                dashboard_total,
                                ft.Text("Total", size=14)
                            ]
                        )
                    ),
                    ft.Container(
                        width=110,
                        height=110,
                        bgcolor=ft.colors.GREEN_100,
                        border_radius=10,
                        padding=10,
                        content=ft.Column(
                            alignment="center",
                            horizontal_alignment="center",
                            controls=[
                                dashboard_completed,
                                ft.Text("Concluídas", size=14)
                            ]
                        )
                    ),
                    ft.Container(
                        width=110,
                        height=110,
                        bgcolor=ft.colors.ORANGE_100,
                        border_radius=10,
                        padding=10,
                        content=ft.Column(
                            alignment="center",
                            horizontal_alignment="center",
                            controls=[
                                dashboard_pending,
                                ft.Text("Pendentes", size=14)
                            ]
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            ft.Divider(height=20),
            ft.Text("Produtividade:", size=16),
            ft.Container(
                width=350,
                height=50,
                bgcolor=ft.colors.BLUE_50,
                border_radius=25,
                padding=5,
                content=ft.Row(
                    controls=[
                        ft.Container(
                            width=f"{productivity}%",
                            height=40,
                            bgcolor=ft.colors.BLUE,
                            border_radius=20,
                            alignment=ft.alignment.center,
                            content=dashboard_productivity
                        )
                    ]
                )
            ),
            ft.Divider(height=20),
            line_chart,
            ft.Divider(height=20),
            ft.Text("Atividades Recentes", size=18, weight="bold"),
            activities_list
        ]
    )
    
    dashboard_container = ft.Container(
        width=400,
        height=550,
        bgcolor="white",
        border_radius=16,
        padding=20,
        content=dashboard
    )

    _stack_main = ft.Stack(controls=[_main])
    page.add(_stack_main)

ft.app(target=main)