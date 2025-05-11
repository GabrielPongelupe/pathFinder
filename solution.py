import heapq

# Calcula a heurística (distância de Manhattan)
def calcular_heuristica(ponto1, ponto2):
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

def busca_a_estrela(mapa, origem, destino):
    linhas, colunas = len(mapa), len(mapa[0])
    fronteira = []
    heapq.heappush(fronteira, (0, origem))

    caminho = {}
    custo_acumulado = {origem: 0}

    while fronteira:
        _, atual = heapq.heappop(fronteira)

        if atual == destino:
            rota = []
            while atual in caminho:
                rota.append(atual)
                atual = caminho[atual]
            rota.append(origem)
            rota.reverse()
            return rota

        for desloc_x, desloc_y in [(-1,0), (1,0), (0,-1), (0,1)]:
            vizinho = (atual[0] + desloc_x, atual[1] + desloc_y)

            if 0 <= vizinho[0] < linhas and 0 <= vizinho[1] < colunas:
                if mapa[vizinho[0]][vizinho[1]] != 1:
                    novo_custo = custo_acumulado[atual] + 1

                    if vizinho not in custo_acumulado or novo_custo < custo_acumulado[vizinho]:
                        custo_acumulado[vizinho] = novo_custo
                        prioridade = novo_custo + calcular_heuristica(vizinho, destino)
                        heapq.heappush(fronteira, (prioridade, vizinho))
                        caminho[vizinho] = atual

    return None

def exibir_mapa_com_rota(mapa, rota):
    visual = [['S' if (i, j) == rota[0] else 'E' if (i, j) == rota[-1] else '1' if mapa[i][j] == 1 else '0' for j in range(len(mapa[0]))] for i in range(len(mapa))]
    for i, j in rota[1:-1]:
        visual[i][j] = '*'
    for linha in visual:
        print(' '.join(str(celula) for celula in linha))

if __name__ == "__main__":
    labirinto = [
        ['S', 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 'E', 1]
    ]

    inicio = destino = None
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == 'S':
                inicio = (i, j)
                labirinto[i][j] = 0
            elif labirinto[i][j] == 'E':
                destino = (i, j)
                labirinto[i][j] = 0

    if not inicio or not destino:
        print("Erro: Início ou destino não identificado no labirinto.")
    else:
        resultado = busca_a_estrela(labirinto, inicio, destino)
        if resultado:
            print("Rota encontrada:", resultado)
            print("\nVisualização do caminho:")
            exibir_mapa_com_rota(labirinto, resultado)
        else:
            print("Nenhuma rota possível.")
