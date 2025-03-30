import flet as ft
from mapa.mapa import adicionar_piscar


ultimo_produto = None

def criar_pesquisa(mapa, page):
    """Cria o componente de pesquisa."""
    
    resultado_texto = ft.Text("")  

    
    barra_pesquisa = ft.TextField(
        label="Digite o nome do produto",
        on_change=lambda e: atualizar_resultado(e.control.value.lower(), mapa, page, resultado_texto),
    )

    
    return ft.Column(
        [
            ft.Text("Pesquisa de Produtos", size=20, weight="bold"),
            barra_pesquisa,
            resultado_texto,  
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

def atualizar_resultado(produto, mapa, page, resultado_texto):
    """Atualiza o texto do resultado e chama a função para piscar a divisão no mapa."""
    global ultimo_produto

    
    if ultimo_produto:
        resultado_texto.value = ""
        ultimo_produto = None

    
    resultado = adicionar_piscar(produto, mapa, page)

    
    resultado_texto.value = resultado

    
    if resultado.startswith("O produto"):
        ultimo_produto = produto

    
    page.update()
