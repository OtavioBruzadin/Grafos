# -*- coding: utf-8 -*-

class GrafoMatriz:
    TAM_MAX_DEFAULT = 100  # qtde de vértices máxima default
    INF = float('inf')  # Valor para representar ausência de conexão em grafos com peso

    def __init__(self, n=TAM_MAX_DEFAULT, rotulado=False):
        self.n = n  # Quantidade de vértices
        self.m = 0  # Quantidade de arestas
        self.rotulado = rotulado  # Define se o grafo é rotulado
        self.nomes = {i: f"V{i}" for i in range(n)}  # Nome dos vértices
        valor_padrao = self.INF if rotulado else 0
        self.adj = [[valor_padrao for _ in range(n)] for _ in range(n)]  # Matriz de adjacência

    def insereA(self, vertice_origem, vertice_alvo, peso=1.0):
        if self.rotulado:
            if self.adj[vertice_origem][vertice_alvo] == self.INF:
                self.adj[vertice_origem][vertice_alvo] = peso
                self.m += 1
        else:
            if self.adj[vertice_origem][vertice_alvo] == 0:
                self.adj[vertice_origem][vertice_alvo] = 1
                self.m += 1

    def removeA(self, vertice_origem, vertice_alvo):
        if self.rotulado:
            if self.adj[vertice_origem][vertice_alvo] != self.INF:
                self.adj[vertice_origem][vertice_alvo] = self.INF
                self.m -= 1
        else:
            if self.adj[vertice_origem][vertice_alvo] == 1:
                self.adj[vertice_origem][vertice_alvo] = 0
                self.m -= 1

    def removeV(self, vertice):
        """Remove um vértice do grafo, excluindo sua linha e coluna na matriz de adjacência."""
        if vertice not in self.nomes:
            raise ValueError("Vértice inválido")

        # Obtém índice do vértice e remove o nome
        idx = list(self.nomes.keys()).index(vertice)
        del self.nomes[vertice]

        # Remove a linha correspondente ao vértice
        del self.adj[idx]

        # Remove a coluna correspondente ao vértice
        for i in range(len(self.adj)):
            del self.adj[i][idx]

        # Atualiza o número de vértices
        self.n -= 1

    def show(self):

        nomes_ordenados = sorted(self.nomes.keys())
        print("\nMatriz de Adjacência:")
        print("   " + " ".join(f"{self.nomes[i]:3}" for i in nomes_ordenados))
        print("   " + "---" * len(nomes_ordenados))
        for i, vertice in enumerate(nomes_ordenados):
            linha = " ".join(f"{self.adj[i][j]:3}" for j in range(len(nomes_ordenados)))
            print(f"{self.nomes[vertice]:2} | {linha}")

    def inDegree(self, vertice):
        if vertice < 0 or vertice >= self.n:
            raise ValueError("Vértice fora do intervalo válido.")
        return sum(1 for i in range(self.n) if self.adj[i][vertice] != (self.INF if self.rotulado else 0))

    def outDegree(self, vertice):
        if vertice < 0 or vertice >= self.n:
            raise ValueError("Vértice fora do intervalo válido.")
        return sum(1 for i in range(self.n) if self.adj[vertice][i] != (self.INF if self.rotulado else 0))

    def degree(self, vertice):
        return self.inDegree(vertice) + self.outDegree(vertice)

    def isSource(self, vertice):
        saida = self.outDegree(vertice)
        entrada = self.inDegree(vertice)

        if saida > 0 and entrada == 0:
            return 1
        else:
            return 0

    def isSorvedouro(self, vertice):
        saida = self.outDegree(vertice)
        entrada = self.inDegree(vertice)

        if saida == 0 and entrada > 0:
            return 1
        else:
            return 0

