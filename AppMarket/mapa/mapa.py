import flet as ft
import time

# Dicionário atualizado para incluir corredor, prateleira e gaveta
produtos = {
    "arroz": ("corredor_1", "prateleira_1", "gaveta_1"),
    "feijão": ("corredor_1", "prateleira_1", "gaveta_2"),
    "macarrão": ("corredor_2", "prateleira_2", "gaveta_1"),
    "óleo": ("corredor_2", "prateleira_2", "gaveta_2"),
    "alho": ("corredor_4", "prateleira_5", "gaveta_3"),
    "sazon": ("corredor_5", "prateleira_4", "gaveta_4")
}

def criar_mapa():
    MAPA_LARGURA = 800
    MAPA_ALTURA = 500

    corredores = []
    espacamento_vertical = 100

    for i in range(5):
        corredor_var = f"corredor_{i + 1}"
        prateleiras = []

        for j in range(4):
            prateleira_var = f"prateleira_{j + 1}"
            gavetas = [
                ft.Container(
                    width=MAPA_LARGURA // 4 - 2,
                    height=50,
                    bgcolor="lightgrey",
                    border=ft.border.all(1, "black"),
                    data={
                        "corredor": corredor_var,
                        "prateleira": prateleira_var,
                        "gaveta": f"gaveta_{k + 1}"
                    },
                )
                for k in range(3)
            ]

            prateleiras.append(
                ft.Container(
                    width=MAPA_LARGURA // 2 - 4,
                    height=50,
                    bgcolor="white",
                    border=ft.border.all(1, "black"),
                    data={"corredor": corredor_var, "prateleira": prateleira_var},
                    content=ft.Row(gavetas, spacing=2),
                )
            )

        corredores.append(
            ft.Container(
                width=MAPA_LARGURA,
                height=100,
                bgcolor="lightgrey",
                border=ft.border.all(3, "black"),
                data={"corredor": corredor_var},
                content=ft.Column(prateleiras, spacing=10),
            )
        )

    mapa = ft.Container(
        width=MAPA_LARGURA,
        height=MAPA_ALTURA,
        bgcolor="lightgrey",
        border=ft.border.all(3, "black"),
        content=ft.Column(corredores, spacing=10),
    )
    return mapa

def criar_mapa_gaveta( gaveta_var):
    """Cria um mapa para uma gaveta específica."""
    GAVETA_LARGURA = 600
    GAVETA_ALTURA = 100
    divisao_largura = GAVETA_LARGURA // 4

    divisores = [
        ft.Container(
            width=divisao_largura - 1,
            height=GAVETA_ALTURA - 1,
            bgcolor="blue" if f"gaveta_{j + 1}" == gaveta_var else "lightgrey",
            border=ft.border.all(1, "black"),
            data={"gaveta": f"gaveta_{j + 1}"},
        )
        for j in range(4)
    ]

    gaveta = ft.Container(
        width=GAVETA_LARGURA,
        height=GAVETA_ALTURA,
        bgcolor="white",
        border=ft.border.all(2, "black"),
        content=ft.Row(divisores, spacing=2),
    )
    return gaveta

def piscar_gaveta(gaveta, page):
    """Faz a gaveta piscar em vermelho."""
    for _ in range(4):
        gaveta.bgcolor = "blue"
        page.update()
        time.sleep(0.5)
        gaveta.bgcolor = "lightgrey"
        page.update()
        time.sleep(0.5)

def adicionar_piscar(produto, mapa, page, gaveta_menor_container):
    """Faz a gaveta onde o produto está piscar."""
    if produto in produtos:
        corredor_var, prateleira_var, gaveta_var = produtos[produto]

        for corredor in mapa.content.controls:
            if corredor.data.get("corredor") == corredor_var:
                for prateleira in corredor.content.controls:
                    if prateleira.data.get("prateleira") == prateleira_var:
                        for gaveta in prateleira.content.controls:
                            if gaveta.data.get("gaveta") == gaveta_var:
                                piscar_gaveta(gaveta, page)

                                gaveta_menor_container.content = criar_mapa_gaveta(
                                     gaveta_var
                                )
                                page.update()

                                return f"O produto {produto} está no {corredor_var}, {prateleira_var}, {gaveta_var}."
        return f"Produto {produto} não encontrado no mapa."
    else:
        return f"Produto {produto} não encontrado!"

def main(page: ft.Page):
    mapa = criar_mapa()

    resultado_texto = ft.Text()
    gaveta_menor_container = ft.Container()

    def buscar_produto(e):
        produto = barra_pesquisa.value.lower().strip()
        if produto:
            resultado_texto.value = ""
            resultado = adicionar_piscar(produto, mapa, page, gaveta_menor_container)
            resultado_texto.value = resultado
        else:
            resultado_texto.value = "Digite um nome válido para o produto."
        page.update()

    barra_pesquisa = ft.TextField(
        label="Digite o nome do produto",
        expand=True
    )
    btn = ft.ElevatedButton(
        "Buscar",
        on_click=buscar_produto
    )

    page.add(
        ft.Column(
            [
                ft.Text("Supermercado", size=24, weight="bold"),
                barra_pesquisa,
                btn,
                resultado_texto,
                mapa,
                gaveta_menor_container,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
