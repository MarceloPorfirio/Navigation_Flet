import flet as ft
import datetime
import sqlite3

# Criação do banco de dados e da tabela
def create_db():
    conn = sqlite3.connect("agendamentos.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS agendamentos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        sobrenome TEXT,
                        telefone TEXT,
                        servico TEXT,
                        data_agendamento TEXT,
                        horario TEXT,
                        data_registro TEXT
                    )''')
    conn.commit()
    conn.close()

# Função para inserir agendamento no banco de dados
def save_agendamento(nome, sobrenome, telefone, servico, data_agendamento, horario):
    conn = sqlite3.connect("agendamentos.db")
    cursor = conn.cursor()
    data_registro = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''INSERT INTO agendamentos (nome, sobrenome, telefone, servico, data_agendamento, horario, data_registro) 
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                   (nome, sobrenome, telefone, servico, data_agendamento, horario, data_registro))
    conn.commit()
    conn.close()

def main(page: ft.Page):
    page.title = "Home"
    page.bgcolor = "black"

    # Criação do banco de dados
    create_db()

    # Campo de texto para exibir a data
    retirada_textfield = ft.TextField(
        value="Agendar Data",  # Texto inicial
        read_only=True,  # Impede edição direta
        width=305,
        height=50,
        filled=True,
        border_color="transparent",
        bgcolor="white",
        text_size=15,
    )

    # Função para atualizar o TextField com a data selecionada
    def atualizar_textfield(e):
        if e.control.value:  # Verifica se uma data foi selecionada
            retirada_textfield.value = e.control.value.strftime('%d/%m/%Y')  # Formata a data
            page.update()

    # DatePicker
    datepicker = ft.DatePicker(
        first_date=datetime.datetime(year=2018, month=10, day=1),
        last_date=datetime.datetime(year=2040, month=10, day=1),
        on_change=atualizar_textfield,  # Atualiza o TextField com a data selecionada
    )

    def show_dialog(e, nome_input, sobrenome_input, telefone_input, servico_dropdown, retirada_textfield, horario_dropdown):
        # Salva o agendamento no banco de dados
        save_agendamento(
            nome_input.value, 
            sobrenome_input.value, 
            telefone_input.value, 
            servico_dropdown.value, 
            retirada_textfield.value,  # data_agendamento
            horario_dropdown.value     # horario
        )
        
        # Limpa os campos após salvar
        nome_input.value = ""
        sobrenome_input.value = ""
        telefone_input.value = ""
        servico_dropdown.value = None
        retirada_textfield.value = "Agendar Data"
        horario_dropdown.value = None
        page.update()

        # Exibe o dialog de sucesso
        dialog = ft.AlertDialog(
            title=ft.Text('Agendamento feito com sucesso!')
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def route_change(e):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Home"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Agendar", on_click=lambda _: page.go("/store")),
                    ft.ElevatedButton("Consultar Agendamentos", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            # Definir os campos de entrada dentro da rota
            nome_input = ft.TextField(label="Nome", hint_text="Digite seu nome")
            sobrenome_input = ft.TextField(label="Sobrenome", hint_text="Digite seu sobrenome")
            telefone_input = ft.TextField(label="Telefone", hint_text="Digite seu telefone")
            servico_dropdown = ft.Dropdown(
                options=[
                    ft.dropdown.Option('Colocação'),
                    ft.dropdown.Option('Manutenção'),
                ],
                label='Serviço',
            )
            horario_dropdown = ft.Dropdown(
                label='Selecionar Horário',
                options=[
                    ft.dropdown.Option('14:00'),
                    ft.dropdown.Option('16:00'),
                ],
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
                                                            ft.Icon(ft.icons.LOCK_CLOCK, size=30),
                                                            horario_dropdown,
                                                        ],
                                                        alignment="center",
                                                    )
                                                ],
                                                col={'sm': 12, 'md': 6}  # Ocupa toda a largura na tela pequena
                                            ),
                                        ],
                                    ),
                                    ft.ElevatedButton("Enviar", on_click=lambda e: show_dialog(
                                        e, 
                                        nome_input, 
                                        sobrenome_input, 
                                        telefone_input, 
                                        servico_dropdown, 
                                        retirada_textfield,  # data_agendamento
                                        horario_dropdown     # horario
                                    )),
                                ],
                                alignment="center",
                                spacing=15,
                            ),
                            padding=20,
                        ),
                    ],
                )
            )
       
       
        # Adiciona o DatePicker ao overlay da página
        page.overlay.append(datepicker)
        page.update()
        
    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(main)
