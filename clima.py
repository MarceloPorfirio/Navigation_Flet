import flet as ft
import requests

# Função para obter o clima atual
def obter_clima(cidade, chave_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"
    
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        
        temperatura = dados['main']['temp']
        condicao = dados['weather'][0]['description']
        cidade_nome = dados['name']
        
        clima_info = f"Clima em {cidade_nome}: {temperatura}°C, {condicao.capitalize()}"
        return clima_info
    else:
        return "Erro ao obter dados de clima. Verifique a chave de API e a cidade."

# Função para exibir o clima no painel Flet
def clima_painel(page):
    chave_api = "69c0ee855bf16de9a58651b7b768d514"  # Sua chave de API
    cidade = "São Paulo"  # Substitua pela cidade desejada

    clima_atual = obter_clima(cidade, chave_api)
    
    # Criando os widgets para o painel de clima
    clima_text = ft.Text(clima_atual, size=20, color=ft.colors.BLACK)
    
    # Exibindo no painel
    page.add(
        ft.Column(
            [
                ft.Text("Clima Atual", size=24, weight="bold"),
                clima_text
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# Configuração do Flet
def main(page):
    page.title = "Clima do Tempo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Adicionando o painel de clima à página
    clima_painel(page)

ft.app(target=main)
