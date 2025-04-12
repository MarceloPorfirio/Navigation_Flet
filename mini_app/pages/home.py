import flet as ft
from datetime import datetime

def view(navigate_to):
    # Componentes da interface
    welcome_text = ft.Text(
        value=f"Bem-vindo(a)!",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE_800
    )
    
    date_text = ft.Text(
        value=datetime.now().strftime("%A, %d de %B de %Y"),
        size=16,
        color=ft.colors.GREY_600
    )
    
    quick_actions = ft.Row(
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.IconButton(
                icon=ft.icons.ADD_TASK,
                icon_size=30,
                tooltip="Nova Tarefa",
                on_click=lambda e: navigate_to("todo"),
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.BLUE_100,
                    shape=ft.CircleBorder()
                )
            ),
            ft.IconButton(
                icon=ft.icons.NOTE_ADD,
                icon_size=30,
                tooltip="Nova Nota",
                on_click=lambda e: navigate_to("notes"),
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.GREEN_100,
                    shape=ft.CircleBorder()
                )
            ),
            ft.IconButton(
                icon=ft.icons.ANALYTICS,
                icon_size=30,
                tooltip="Dashboard",
                on_click=lambda e: navigate_to("dashboard"),
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.ORANGE_100,
                    shape=ft.CircleBorder()
                )
            ),
        ]
    )
    
    recent_tasks = ft.Column(
        spacing=10,
        controls=[
            ft.Text("Atividades Recentes", size=18, weight=ft.FontWeight.BOLD),
            ft.ListTile(
                title=ft.Text("Reunião com equipe",color='black'),
                leading=ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN),
                subtitle=ft.Text("Hoje - 10:00 AM"),
            ),
            ft.ListTile(
                title=ft.Text("Compras do mês"),
                leading=ft.Icon(ft.icons.PENDING, color=ft.colors.ORANGE),
                subtitle=ft.Text("Ontem - Pendente"),
            ),
        ]
    )
    
    weather_card = ft.Card(
        content=ft.Container(
            padding=15,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.icons.WB_SUNNY, size=40),
                            ft.Text("26°C", size=24),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Text("Canoas, RS", size=14),
                ]
            )
        ),
        elevation=2
    )
    
    return ft.Container(
        width=400,
        height=550,
        padding=20,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.icons.ACCOUNT_CIRCLE, size=80, color=ft.colors.BLUE_400),
                        welcome_text,
                        date_text,
                        ft.Divider(height=20),
                    ]
                ),
                
                ft.Text("Ações Rápidas", size=18, weight=ft.FontWeight.BOLD),
                quick_actions,
                
                ft.Divider(height=30),
                
                ft.Row(
                    controls=[
                        weather_card,
                        ft.Card(
                            content=ft.Container(
                                padding=15,
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Icon(ft.icons.ACCESS_TIME, size=30),
                                               
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER
                                        ),
                                        
                                        ft.Text(
                                            datetime.now().strftime("%H:%M"),
                                            size=28,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.colors.BLUE
                                        ),
                                    ],
                                    spacing=5,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                )
                            ),
                            elevation=2,
                            width=120
                        )
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                
                ft.Divider(height=20),
                
                recent_tasks,
                
                ft.FilledButton(
                    "Ver todas as atividades",
                    icon=ft.icons.LIST,
                    on_click=lambda e: navigate_to("todo"),
                    width=250
                )
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )