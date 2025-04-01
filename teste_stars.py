import flet as ft

def main(page: ft.Page):
    page.title = "Avaliação de 5 Estrelas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    class StarRating(ft.UserControl):
        def __init__(self):
            super().__init__()
            self.rating = 0
            self.temp_rating = 0
            self.stars = []

        def build(self):
            # Cria 5 estrelas vazias inicialmente
            for i in range(5):
                star = ft.Container(
                    content=ft.Icon(ft.icons.STAR_OUTLINE, color=ft.colors.AMBER),
                    data=i+1,
                    on_click=self.rate,
                    on_hover=self.hover,
                    padding=5
                )
                self.stars.append(star)
            
            return ft.Row(self.stars, spacing=0)

        def hover(self, e):
            if e.data == "true":
                self.temp_rating = e.control.data
                self.update_stars()
            else:
                self.temp_rating = 0
                self.update_stars()

        def rate(self, e):
            self.rating = e.control.data
            self.temp_rating = 0
            self.update_stars()
            self.show_confirmation()

        def update_stars(self):
            for i, star in enumerate(self.stars):
                if (i+1) <= (self.temp_rating or self.rating):
                    star.content = ft.Icon(ft.icons.STAR, color=ft.colors.AMBER)
                else:
                    star.content = ft.Icon(ft.icons.STAR_OUTLINE, color=ft.colors.AMBER)
            self.update()

        def show_confirmation(self):
            dlg = ft.AlertDialog(
                title=ft.Text("Obrigado!"),
                content=ft.Text(f"Avaliação: {self.rating} estrela(s)"),
                on_dismiss=lambda e: print("Dialog dismissed!")
            )
            page.dialog = dlg
            dlg.open = True
            page.update()

    # Layout da página
    page.add(
        ft.Column(
            [
                ft.Text("Avalie nosso serviço:", size=20),
                StarRating()
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)