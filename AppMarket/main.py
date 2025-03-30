import flet as ft
from mapa.mapa import criar_mapa, adicionar_piscar

def main(page: ft.Page):
    
    mapa = criar_mapa()

    
    def buscar_produto(e):
        produto = e.control.value.lower().strip()  
        if produto:  
            resultado = adicionar_piscar(produto, mapa, page)
            resultado_texto.value = resultado
        else:
            resultado_texto.value = "Digite um nome válido para o produto."
        page.update()

   
    barra_pesquisa = ft.TextField(
        label="Digite o nome do produto",
        on_submit=buscar_produto,  
    )

    
    resultado_texto = ft.Text()

    
    page.add(
        ft.Column(
            [
                ft.Text("Supermercado", size=24, weight="bold"),
                barra_pesquisa,
                resultado_texto,
                mapa,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
