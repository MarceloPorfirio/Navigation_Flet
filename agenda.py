import flet as ft
import datetime
import sqlite3
from banco_db import *
from validations import *
from utils import *


def main(page: ft.Page):
    page.title = "Home"
    page.theme_mode = ft.ThemeMode.DARK

    # Inicializando o logo
    logo = ft.Image(
        src='assets/logo (2).png',  # Logo inicial
        scale=ft.transform.Scale(1.5)
    )

    def toggle_theme(e):
            page.theme_mode = (
                ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
            )
             # Alterna o logo com base no tema
            if page.theme_mode == ft.ThemeMode.DARK:
                logo.src = 'assets/logo (2).png'
            else:
                logo.src = 'assets/logo.jpg'
                 
            
            page.update()
        
    

    # Criação do banco de dados
    create_db()

    # Campo de texto para exibir a data
    retirada_textfield = ft.TextField(
        value="Agendar Data",  # Texto inicial
        read_only=True,  # Impede edição direta
        width=305,
        height=50,
        text_size=15,
    )
    
    

    # Função para buscar horários ocupados para uma data específica
    def buscar_horarios_ocupados(data_agendamento):
        conn = sqlite3.connect("agendamentos.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT horario FROM agendamentos WHERE data_agendamento = ?''', (data_agendamento,))
        horarios_ocupados = [row[0] for row in cursor.fetchall()]
        conn.close()
        return horarios_ocupados

    def atualizar_horarios_disponiveis(e):
        if retirada_textfield.value != "Agendar Data":  # Verifica se uma data foi selecionada
            data_selecionada = retirada_textfield.value  # Data selecionada no formato DD/MM/YYYY
            
            # Buscar horários ocupados no banco de dados
            horarios_ocupados = buscar_horarios_ocupados(data_selecionada)
            
            # Gerar lista de horários disponíveis
            horarios_disponiveis = [horario for horario in gerar_horarios() if horario not in horarios_ocupados]
            
            # Atualizar o dropdown com os horários disponíveis
            horario_dropdown.options = [
                ft.dropdown.Option(horario) for horario in horarios_disponiveis
            ]
            horario_dropdown.value = None  # Limpar seleção anterior
            page.update()

    # Função para atualizar o TextField com a data selecionada
    def atualizar_textfield(e):
        if e.control.value:  # Verifica se uma data foi selecionada
            retirada_textfield.value = e.control.value.strftime('%d/%m/%Y')  # Formata a data
            atualizar_horarios_disponiveis(e)  # Atualizar horários disponíveis
            page.update()

    # DatePicker
    datepicker = ft.DatePicker(
        first_date=datetime.datetime(year=2018, month=10, day=1),
        last_date=datetime.datetime(year=2040, month=10, day=1),
        on_change=atualizar_textfield,  # Atualiza o TextField com a data selecionada
    )
    page.overlay.append(datepicker)

    
    def show_dialog(e, nome_input, sobrenome_input, telefone_input, servico_dropdown, retirada_textfield, horario_dropdown):
        erros = validar_campos(
            nome_input.value,
            sobrenome_input.value,
            telefone_input.value,
            servico_dropdown.value,
            retirada_textfield.value,
            horario_dropdown.value
        )

        if erros:
            # Exibe os erros no diálogo
            dialog = ft.AlertDialog(
                title=ft.Text("Erro ao salvar agendamento", size=20, color="red"),
                content=ft.Column(
                    height=200,
                    controls=
                    [
                        ft.Text(erro, size=15, color="black") for erro in erros],
                    spacing=5
                ),
                
            )
            dialog.open = True
            page.dialog = dialog
            page.update()
            return

        # Salva o agendamento no banco de dados
        save_agendamento(
            nome_input.value, 
            sobrenome_input.value, 
            telefone_input.value, 
            servico_dropdown.value, 
            retirada_textfield.value,  
            horario_dropdown.value    
        )

        # Limpa os campos após salvar
        nome_input.value = ""
        sobrenome_input.value = ""
        telefone_input.value = ""
        servico_dropdown.value = None
        retirada_textfield.value = "Agendar Data"
        horario_dropdown.value = None
        page.update()

        # Exibe o diálogo de sucesso
        dialog = ft.AlertDialog(
            title=ft.Column([
                ft.Text('Agendamento feito com sucesso!', size=25),
                ft.Divider(color='transparent', height=20),
                ft.Container(
                    content=ft.Icon(
                        name=ft.icons.CHECK_CIRCLE_OUTLINED,
                        color="green",
                        size=50
                    ),
                    alignment=ft.alignment.center
                ),
            ]),
        )
        dialog.open = True
        page.dialog = dialog
        page.update()

    
   
    # Criar Dropdown com a lista de horários
    horario_dropdown = ft.Dropdown(
        label='Selecionar Horário',
        options=[
            ft.dropdown.Option(horario) for horario in gerar_horarios()
        ],
    )
   

    def route_change(e):
       
        style = ft.ButtonStyle(
            color={ft.MaterialState.HOVERED: ft.colors.AMBER},
            shape={ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10),
            },
            padding={ft.MaterialState.DEFAULT:ft.padding.all(40)},
        
            
        )
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                
                [
                    ft.AppBar(title=ft.Text("Home"), bgcolor=ft.colors.SURFACE_VARIANT,
                              actions=[
                              
                              ft.IconButton(
                                  icon=ft.icons.BRIGHTNESS_6,
                                  on_click=toggle_theme,
                                  tooltip='Alternar tema'
                              )
                ],
                              ),
                    ft.Divider(color='transparent',height=30),
                    ft.Row(
                        controls=[
                            ft.Container(
                                width=200,
                                height=200,
                                padding=5,  # Espaçamento interno ao redor do logo
                                content=logo,
                                border=ft.border.all(2, ft.colors.AMBER),  # Borda dourada
                                border_radius=ft.border_radius.all(100),  # Bordas arredondadas
                                
                            ),
                            
                            ft.Container(
                                width=400,
                                height=250,
                                border_radius=ft.border_radius.all(60),
                                # border=ft.border.all(2, ft.colors.AMBER),
                                padding=20,
                                content=ft.Text('✨ "Bem-vinda ao nosso Studio! Aqui, cada detalhe é pensado para realçar sua beleza e oferecer uma experiência única. Agende seu momento de cuidado e fique ainda mais deslumbrante!" 💖',
                                                size=20,
                                                text_align="justify", 
                                                max_lines=6, 
                                                )
                            )
                        ],alignment=ft.MainAxisAlignment.SPACE_EVENLY
                    ),
                    ft.Container(
                        height=80
                            ),
                        
                    ft.Row(
                        controls=[
                                ft.ElevatedButton( 
                                                  on_click=lambda _: page.go("/agendar"),
                                                  icon=ft.icons.ADD,
                                                  text='AGENDAR',
                                                  icon_color="white",  # Cor do ícone
                                                  style=style
                                                  
                                                  ),
                                ft.ElevatedButton("CONSULTAR", on_click=lambda _: page.go("/consulta"),
                                                  style=style,
                                                  icon=ft.icons.SEARCH),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY
                    ),
                    
                ],
            )
        )
        
        if page.route == "/agendar":
            # Definir os campos de entrada dentro da rota
            nome_input = ft.TextField(label="Nome", hint_text="Digite seu nome",capitalization=ft.TextCapitalization.WORDS,autofocus=True)
            sobrenome_input = ft.TextField(label="Sobrenome", hint_text="Digite seu sobrenome",capitalization=ft.TextCapitalization.WORDS)
            telefone_input = ft.TextField(label="Telefone", hint_text="Digite seu telefone",input_filter=ft.NumbersOnlyInputFilter())
            servico_dropdown = ft.Dropdown(
                options=[
                    ft.dropdown.Option('Colocação'),
                    ft.dropdown.Option('Manutenção'),
                ],
                label='Serviço',
            )
            


            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Agendar Horário"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Preencha os dados para agendamento", size=20, weight="bold"),
                                    nome_input,
                                    sobrenome_input,
                                    telefone_input,
                                    servico_dropdown,
                                    ft.ResponsiveRow(
                                        controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Row(
                                                        controls=[
                                                            ft.IconButton(
                                                                icon=ft.icons.CALENDAR_MONTH,
                                                                icon_size=25,
                                                                on_click=lambda _: datepicker.pick_date()  # Abre o DatePicker
                                                            ),
                                                            retirada_textfield,  # Campo de texto para data  
                                                        ],
                                                        alignment="center",
                                                    )
                                                ],
                                                col={'sm': 12, 'md': 6}  # Ocupa toda a largura na tela pequena
                                            ),
                                            ft.Column(
                                                controls=[
                                                    ft.Row(
                                                        controls=[
                                                            ft.Icon(ft.icons.ACCESS_TIME, size=30),
                                                            horario_dropdown,
                                                        ],
                                                        alignment="center",
                                                    )
                                                ],
                                                col={'sm': 12, 'md': 6}  # Ocupa toda a largura na tela pequena
                                            ),
                                        ],
                                    ),
                                    ft.Divider(color='transparent'),
                                    ft.Row(
                                        controls=[
                                        ft.ElevatedButton("Agendar",width=200, on_click=lambda e: show_dialog(
                                        e, 
                                        nome_input, 
                                        sobrenome_input, 
                                        telefone_input, 
                                        servico_dropdown, 
                                        retirada_textfield,  # data_agendamento
                                        horario_dropdown     # horario
                                    )),
                                        ],alignment='center'
                                    )
                                    
                                ],
                                alignment="center",
                                spacing=15,
                            ),
                            padding=20,
                        ),
                    ],
                )
            )

        if page.route == "/consulta":
            buscar_nomes = ft.TextField(
                    icon=ft.icons.SEARCH,
                    hint_text='Buscar por nome',
                    on_change=lambda e: atualizar_tabela(e.control.value)
                )
            def handle_delete(id_agendamento):
                confirm_dialog = ft.AlertDialog(
                    title=ft.Text("Confirmar Exclusão"),
                    content=ft.Text("Você tem certeza que deseja excluir este agendamento?"),
                    actions=[
                        ft.TextButton(
                            "Cancelar",
                            on_click=lambda e: close_dialog()
                        ),
                        ft.TextButton(
                            "Excluir",
                            on_click=lambda e: confirm_delete(id_agendamento)
                        ),
                    ],
                )
                page.dialog = confirm_dialog
                confirm_dialog.open = True
                page.update()

            def close_dialog():
                page.dialog.open = False
                page.update()

            def confirm_delete(id_agendamento):
                delete_agendamento(id_agendamento)
                atualizar_tabela()
                close_dialog()
                

            def toogle_selected(e):
                    e.control.selected = not e.control.selected
                    e.control.update()
                

            def atualizar_tabela(nome_busca=""):
                # Buscar os agendamentos atualizados (ou filtrados pelo nome)
                agendamentos = buscar_agendamentos_nome(nome_busca)

                # Atualizar a tabela com os novos dados
                tabela_agendamentos.rows = [
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(agendamento[1])),  # Nome
                            ft.DataCell(ft.Text(agendamento[2])),  # Sobrenome
                            ft.DataCell(ft.Text(agendamento[3])),  # Telefone
                            ft.DataCell(ft.Text(agendamento[4])),  # Serviço
                            ft.DataCell(ft.Text(agendamento[5])),  # Data
                            ft.DataCell(ft.Text(agendamento[6])),  # Horário
                            ft.DataCell(ft.IconButton(
                                icon=ft.icons.DELETE,
                                icon_color='red',
                                on_click=lambda e, a=agendamento[0]: handle_delete(a)
                            )),
                        ],
                    )
                    for agendamento in agendamentos
                ]
                page.update()


            

            # Buscar os agendamentos
            agendamentos = buscar_agendamentos_nome("")  # Inicializa com todos os agendamentos
            
            tabela_agendamentos = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Nome")),
                    ft.DataColumn(ft.Text("Sobrenome")),
                    ft.DataColumn(ft.Text("Telefone")),
                    ft.DataColumn(ft.Text("Serviço")),
                    ft.DataColumn(ft.Text("Data")),
                    ft.DataColumn(ft.Text("Horário")),
                    ft.DataColumn(ft.Text("Ações")),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(agendamento[1])),  # Nome
                            ft.DataCell(ft.Text(agendamento[2])),  # Sobrenome
                            ft.DataCell(ft.Text(agendamento[3])),  # Telefone
                            ft.DataCell(ft.Text(agendamento[4])),  # Serviço
                            ft.DataCell(ft.Text(agendamento[5])),  # Data
                            ft.DataCell(ft.Text(agendamento[6])),  # Horário
                            ft.DataCell(
                                ft.IconButton(
                                    icon=ft.icons.DELETE,
                                    icon_color='red',
                                    on_click=lambda e, id_agendamento=agendamento[0]: handle_delete(id_agendamento)
                                )
                            ),
                        ],
                        
                        on_select_changed=toogle_selected,
                        
                    )
                    for agendamento in agendamentos
                ],
                bgcolor=ft.colors.WHITE10,
                border=ft.border.all(width=1,color='black'),
                border_radius=ft.border_radius.all(5)

            )

            page.views.append(
                ft.View(
                    "/consulta",
                    [
                        ft.AppBar(title=ft.Text("Consultar Agendamentos"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Row(
                            controls=[
                                buscar_nomes
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            controls=[
                                ft.Text("Agendamentos Realizados", size=25, weight="bold"),
                            ],alignment='center'
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Column(
                                        height=600,
                                        controls=
                                        [
                                            
                                            tabela_agendamentos,
                                        ],
                                        scroll=ft.ScrollMode.AUTO,
                                        spacing=15,
                                        
                                    ),
                                    padding=20,
                                
                                ),
                            ],alignment="center"
                        )
                        
                    ],
                )
            )

        page.update()
        
    def view_pop(e):
        if len(page.views) > 1:  # Verifica se há mais de uma view
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            print("Não há mais views para retornar.")

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(main)
