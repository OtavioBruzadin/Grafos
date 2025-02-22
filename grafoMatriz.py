class GrafoMatriz:
    TAM_MAX_DEFAULT = 100
    INF = float('inf')

    def __init__(self, rotulado=False):
        self.qtd_vertices = 0
        self.qtd_arestas = 0
        self.rotulado = rotulado
        self.nomes = {}
        self.indices = {}
        self.adj = []

    def adicionarVertice(self, nome):
        if nome in self.indices:
            raise ValueError("Vértice já existe.")

        self.nomes[self.qtd_vertices] = nome
        self.indices[nome] = self.qtd_vertices
        self.qtd_vertices += 1

        for linha in self.adj:
            linha.append(self.INF if self.rotulado else 0)
        self.adj.append([self.INF if self.rotulado else 0] * self.qtd_vertices)

    def insereA(self, origem, destino, peso=1.0):
        if origem not in self.indices or destino not in self.indices:
            raise ValueError("Vértice não encontrado.")

        index_origem = self.indices[origem]
        index_destino = self.indices[destino]

        if self.rotulado:
            if self.adj[index_origem][index_destino] == self.INF:
                self.adj[index_origem][index_destino] = peso
                self.qtd_arestas += 1
        else:
            if self.adj[index_origem][index_destino] == 0:
                self.adj[index_origem][index_destino] = 1
                self.qtd_arestas += 1

    def removerVertice(self, vertice):
        if vertice not in self.indices:
            raise ValueError("Vértice não encontrado.")

        index = self.indices[vertice]
        del self.nomes[index]
        del self.indices[vertice]

        del self.adj[index]

        for linha in self.adj:
            del linha[index]

        self.qtd_vertices -= 1

    def removeA(self, origem, destino):
        if origem not in self.indices or destino not in self.indices:
            raise ValueError("Vértice não encontrado.")

        index_origem = self.indices[origem]
        index_destino = self.indices[destino]

        if self.rotulado:
            if self.adj[index_origem][index_destino] != self.INF:
                self.adj[index_origem][index_destino] = self.INF
                self.qtd_arestas -= 1
        else:
            if self.adj[index_origem][index_destino] == 1:
                self.adj[index_origem][index_destino] = 0
                self.qtd_arestas -= 1

    def inDegree(self, vertice):
        if vertice not in self.indices:
            raise ValueError("Vértice não encontrado.")
        index = self.indices[vertice]
        return sum(1 for i in range(self.qtd_vertices) if self.adj[i][index] != (self.INF if self.rotulado else 0))

    def outDegree(self, vertice):
        if vertice not in self.indices:
            raise ValueError("Vértice não encontrado.")
        index = self.indices[vertice]
        return sum(1 for i in range(self.qtd_vertices) if self.adj[index][i] != (self.INF if self.rotulado else 0))

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

    def show(self):
        print("\nMatriz de Adjacência:")
        nomes_ordenados = list(self.nomes.values())
        print("   " + " ".join(f"{nome:3}" for nome in nomes_ordenados))
        print("   " + "---" * self.qtd_vertices)
        for i, nome in enumerate(nomes_ordenados):
            linha = " ".join(f"{self.adj[i][j]:3}" for j in range(self.qtd_vertices))
            print(f"{nome:2} | {linha}")
