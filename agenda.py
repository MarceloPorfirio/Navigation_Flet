import flet
from flet import AppBar, ElevatedButton, Page, Text, TextField, View, Container, Column, colors

def main(page: Page):
    page.title = "Home"
    page.bgcolor = "black"

    def route_change(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton("Agendar", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                View(
                    "/store",
                    [
                        AppBar(title=Text("Agendar Horário"), bgcolor=colors.SURFACE_VARIANT),
                        Container(
                            content=Column(
                                [
                                    Text("Preencha os dados para agendamento", size=20, weight="bold", color="white"),
                                    TextField(label="Nome", hint_text="Digite seu nome"),
                                    TextField(label="Sobrenome", hint_text="Digite seu sobrenome"),
                                    TextField(label="Telefone", hint_text="Digite seu telefone"),
                                    ElevatedButton("Enviar", on_click=lambda _: print("Agendamento enviado!")),
                                ],
                                alignment="center",
                                spacing=15,
                            ),
                            alignment=flet.alignment.center,
                            padding=20,
                        ),
                    ],
                )
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)

flet.app(main)
