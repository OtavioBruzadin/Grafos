# -*- coding: utf-8 -*-

class GrafoMatriz:
    TAM_MAX_DEFAULT = 100  # qtde de vértices máxima default
    INF = float('inf')  # Valor para representar ausência de conexão em grafos com peso

    def __init__(self, n=TAM_MAX_DEFAULT, rotulado=False):
        self.n = n  #
        self.m = 0
        self.rotulado = rotulado
        self.adj = [[self.INF if rotulado else 0 for _ in range(n)] for _ in range(n)]

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

    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            for w in range(self.n):
                if self.rotulado:
                    print(f"{self.adj[i][w]:6.2f} " if self.adj[i][w] != self.INF else " INF  ", end="")
                else:
                    print(f" {self.adj[i][w]} ", end="")
            print("\n")
        print("\nfim da impressao do grafo.")

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

