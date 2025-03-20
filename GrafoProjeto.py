class GrafoMatriz:
    TAM_MAX_DEFAULT = 10000
    INF = float('inf')

    def __init__(self, rotulado=False):
        self.n = 0
        self.m = 0
        self.rotulado = rotulado
        self.indices = {}
        self.nomes = {}
        self.adj = []

    def adicionarVertice(self, nome):
        if nome in self.nomes:
            raise ValueError("Vértice já existe.")

        self.indices[self.n] = nome
        self.nomes[nome] = self.n
        self.n += 1

        for linha in self.adj:
            linha.append(self.INF if self.rotulado else 0)
        self.adj.append([self.INF if self.rotulado else 0] * self.n)

    def insereA(self, origem, destino, peso=1.0):
        if origem not in self.nomes or destino not in self.nomes:
            raise ValueError("Vértice não encontrado.")

        index_origem = self.nomes[origem]
        index_destino = self.nomes[destino]

        if self.rotulado:
            if self.adj[index_origem][index_destino] == self.INF:
                self.adj[index_origem][index_destino] = peso
                self.m += 1
        else:
            if self.adj[index_origem][index_destino] == 0:
                self.adj[index_origem][index_destino] = 1
                self.m += 1

    def removerVertice(self, vertice):
        if vertice not in self.nomes:
            raise ValueError("Vértice não encontrado.")

        index_removido = self.nomes[vertice]

        del self.nomes[vertice]
        old_indices = self.indices.copy()
        del old_indices[index_removido]

        del self.adj[index_removido]
        for linha in self.adj:
            del linha[index_removido]
        self.n -= 1

        new_indices = {}
        new_nomes = {}
        remaining = [old_indices[k] for k in sorted(old_indices.keys())]
        for novo_indice, nome in enumerate(remaining):
            new_indices[novo_indice] = nome
            new_nomes[nome] = novo_indice

        self.indices = new_indices
        self.nomes = new_nomes

    def removeA(self, origem, destino):
        if origem not in self.nomes or destino not in self.nomes:
            raise ValueError("Vértice não encontrado.")

        index_origem = self.nomes[origem]
        index_destino = self.nomes[destino]

        if self.rotulado:
            if self.adj[index_origem][index_destino] != self.INF:
                self.adj[index_origem][index_destino] = self.INF
                self.m -= 1
        else:
            if self.adj[index_origem][index_destino] == 1:
                self.adj[index_origem][index_destino] = 0
                self.m -= 1

    def inDegree(self, vertice):
        if vertice not in self.nomes:
            raise ValueError("Vértice não encontrado.")
        index = self.nomes[vertice]
        return sum(1 for i in range(self.n) if self.adj[i][index] != (self.INF if self.rotulado else 0))

    def outDegree(self, vertice):
        if vertice not in self.nomes:
            raise ValueError("Vértice não encontrado.")
        index = self.nomes[vertice]
        return sum(1 for i in range(self.n) if self.adj[index][i] != (self.INF if self.rotulado else 0))

    def degree(self, vertice):
        return self.inDegree(vertice) + self.outDegree(vertice)

    def isSource(self, vertice):
        saida = self.outDegree(vertice)
        entrada = self.inDegree(vertice)
        return 1 if (saida > 0 and entrada == 0) else 0

    def isSorvedouro(self, vertice):
        saida = self.outDegree(vertice)
        entrada = self.inDegree(vertice)
        return 1 if (saida == 0 and entrada > 0) else 0

    def show(self):
        print("\nMatriz de Adjacência:")
        nomes_ordenados = [self.nomes_inv(i) for i in range(self.n)]
        print("   " + " ".join(f"{nome:3}" for nome in nomes_ordenados))
        print("   " + "---" * self.n)
        for i, nome in enumerate(nomes_ordenados):
            linha = " ".join(f"{self.adj[i][j]:3}" for j in range(self.n))
            print(f"{nome:2} | {linha}")

    def nomes_inv(self, indice):
        return self.indices.get(indice, "?")

    def lerArquivoMatrizAdj(self, arquivo):
        with open(arquivo, 'r') as arq:
            num_vertices = int(arq.readline().strip())
            for _ in range(num_vertices):
                nome_vertice = arq.readline().strip()
                self.adicionarVertice(nome_vertice)
            num_arestas = int(arq.readline().strip())
            for _ in range(num_arestas):
                partes = arq.readline().strip().split()
                if len(partes) < 2:
                    continue
                origem, destino = partes[0], partes[1]
                if self.rotulado:
                    if len(partes) != 3:
                        continue
                    peso_str = partes[2]
                    try:
                        peso = float(peso_str)
                    except ValueError:
                        peso = peso_str
                    self.insereA(origem, destino, peso)
                else:
                    self.insereA(origem, destino, 1)
        return self.adj

    def gravarArquivoMatrizAdj(self, arquivo):
        with open(arquivo, 'w') as arq:
            arq.write(f"{self.n}\n")
            for i in range(self.n):
                nome = self.indices[i]
                arq.write(f"{nome}\n")
            # Escreve o número de arestas
            arq.write(f"{self.m}\n")
            # Escreve cada aresta existente na matriz
            for i in range(self.n):
                origem = self.indices[i]
                for j in range(self.n):
                    if self.rotulado:
                        if self.adj[i][j] != self.INF:
                            destino = self.indices[j]
                            peso = self.adj[i][j]
                            arq.write(f"{origem} {destino} {peso}\n")
                    else:
                        if self.adj[i][j] != 0:
                            destino = self.indices[j]
                            arq.write(f"{origem} {destino}\n")

    def dfs(self, v, visitados):
        visitados[v] = True
        for i in range(self.n):
            if not visitados[i]:
                if self.rotulado:
                    if self.adj[v][i] != self.INF:
                        self.dfs(i, visitados)
                else:
                    if self.adj[v][i] != 0:
                        self.dfs(i, visitados)

    def categoriaConexidade(self):
        visitados = [False] * self.n
        self.dfs(0, visitados)
        if not all(visitados):
            return 0

        forteConexo = True
        for i in range(self.n):
            for j in range(self.n):
                if self.rotulado:
                    if (self.adj[i][j] != self.INF) != (self.adj[j][i] != self.INF):
                        forteConexo = False
                        break
                else:
                    if (self.adj[i][j] != 0) != (self.adj[j][i] != 0):
                        forteConexo = False
                        break
            if not forteConexo:
                break

        if forteConexo:
            return 3

        bidirecional = False
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    if self.rotulado:
                        if self.adj[i][j] != self.INF and self.adj[j][i] != self.INF:
                            bidirecional = True
                            break
                    else:
                        if self.adj[i][j] != 0 and self.adj[j][i] != 0:
                            bidirecional = True
                            break
            if bidirecional:
                break

        if bidirecional:
            return 2

        return 1

    def grafoReduzido(self):
        novo_grafo = GrafoMatriz(rotulado=self.rotulado)
        vertices_validos = [nome for nome in self.nomes if self.degree(nome) > 0]
        for nome in vertices_validos:
            novo_grafo.adicionarVertice(nome)
        for origem in vertices_validos:
            for destino in vertices_validos:
                i = self.nomes[origem]
                j = self.nomes[destino]
                if self.rotulado:
                    if self.adj[i][j] != self.INF:
                        novo_grafo.insereA(origem, destino, self.adj[i][j])
                else:
                    if self.adj[i][j] != 0:
                        novo_grafo.insereA(origem, destino)
        return novo_grafo