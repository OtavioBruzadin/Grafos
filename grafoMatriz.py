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
        if isinstance(vertice, int):
            if vertice not in self.nomes or self.nomes[vertice] is None:
                raise ValueError("Vértice não existe.")
        else:
            if vertice not in self.nomes.values():
                raise ValueError("Vértice não existe.")
            vertice = list(self.nomes.keys())[list(self.nomes.values()).index(vertice)]

        self.nomes[vertice] = None
        for i in range(self.n):
            self.adj[vertice][i] = self.INF if self.rotulado else 0
            self.adj[i][vertice] = self.INF if self.rotulado else 0

    def inDegree(self, vertice):
        if isinstance(vertice, int):
            if vertice not in self.nomes or self.nomes[vertice] is None:
                raise ValueError("Vértice não existe.")
        else:
            if vertice not in self.nomes.values():
                raise ValueError("Vértice não existe.")
            vertice = list(self.nomes.keys())[list(self.nomes.values()).index(vertice)]

        return sum(1 for i in range(self.n) if self.adj[i][vertice] != self.INF and self.adj[i][vertice] != 0)

    def outDegree(self, vertice):
        if isinstance(vertice, int):
            if vertice not in self.nomes or self.nomes[vertice] is None:
                raise ValueError("Vértice não existe.")
        else:
            if vertice not in self.nomes.values():
                raise ValueError("Vértice não existe.")
            vertice = list(self.nomes.keys())[list(self.nomes.values()).index(vertice)]

        return sum(1 for j in range(self.n) if self.adj[vertice][j] != self.INF and self.adj[vertice][j] != 0)

    def degree(self, vertice):
        return self.inDegree(vertice) + self.outDegree(vertice)

    def show(self):
        nomes_ordenados = [i for i in sorted(self.nomes.keys()) if self.nomes[i] is not None]
        print("   " + " ".join(f"{self.nomes[i]:3}" for i in nomes_ordenados))
        for vertice in nomes_ordenados:
            linha = " ".join(f"{self.adj[vertice][j]:3}" for j in nomes_ordenados)
            print(f"{self.nomes[vertice]:2} | {linha}")

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

    def isComplete(self):
        n = len(self.adj)
        for i in range(n):
            for j in range(n):
                if i != j and (self.adj[i][j] == 0 or self.adj[i][j] == self.INF):
                    return False
        return True

    def complementar(self):
        grafo_comp = GrafoMatriz(self.n, self.rotulado)
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    if not self.rotulado:
                        grafo_comp.adj[i][j] = 1 if self.adj[i][j] == 0 else 0
                    else:
                        if self.adj[i][j] == self.INF:
                            grafo_comp.adj[i][j] = 1
                        else:
                            grafo_comp.adj[i][j] = self.INF

        return grafo_comp

    def grafoReduzido(self):
        vertices_validos = [v for v in range(self.n) if self.degree(v) > 0]

        if not vertices_validos:
            return []

        tamanho = len(vertices_validos)
        novo_grafo = [[self.INF if self.rotulado else 0 for _ in range(tamanho)] for _ in range(tamanho)]

        converte = {old: new for new, old in enumerate(vertices_validos)}

        for i in vertices_validos:
            for j in vertices_validos:
                if self.adj[i][j] != (self.INF if self.rotulado else 0):
                    novo_grafo[converte[i]][converte[j]] = self.adj[i][j]

        return novo_grafo


    def lerArquivo(self, arquivo):
        with open(arquivo, 'r') as arquivo:
            self.n = int(arquivo.readline().strip())
            self.m = int(arquivo.readline().strip())

            self.nomes = {i: f"V{i}" for i in range(self.n)}
            valor_padrao = self.INF if self.rotulado else 0
            self.adj = [[valor_padrao for _ in range(self.n)] for _ in range(self.n)]

            for _ in range(self.m):
                u, v = map(int, arquivo.readline().strip().split())
                self.insereA(u, v)


    def simetrico(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] != self.INF and self.adj[j][i] != self.INF:
                    if self.adj[i][j] != self.adj[j][i]:
                        return 0
                elif self.adj[i][j] != self.adj[j][i]:
                    return 0
        return 1

    def isConected(self):
        visitados = set()

        def verifica(v):
            visitados.add(v)
            for j in range(self.n):
                if self.adj[v][j] != 0 and self.adj[v][j] != self.INF and j not in visitados:
                    verifica(j)

        for v in range(self.n):
            if self.nomes[v] is not None:
                verifica(v)

                break

        for v in range(self.n):
            if self.nomes[v] is not None and v not in visitados:
                return 1
        return 0

    def dfs(self, vertice, visitados):
        visitados[vertice] = True
        for i in range(self.n):
            if self.adj[vertice][i] != self.INF and self.adj[vertice][i] != 0 and not visitados[i]:
                self.dfs(i, visitados)

    def categoriaConexidade(self):
        visitados = [False for _ in range(self.n)]
        self.dfs(0, visitados)
        for v in visitados:
            if not v:
                return 0

        grafo = self.adj
        n = self.n

        forteConexo = True
        for i in range(n):
            for j in range(n):
                if grafo[i][j] != grafo[j][i]:
                    forteConexo = False
                    break
            if not forteConexo:
                break

        if forteConexo:
            return 3

        resultados = []

        for i in range(n):
            for j in range(n):
                if (grafo[i][j] == 1) and (grafo[j][i] == 1):
                    resultados.append(True)
                else:
                    resultados.append(False)
        if any(resultados):
            return 2

        return 1

    def dijkstra(self, origem):
        if not self.rotulado:
            raise ValueError("O algoritmo de Dijkstra requer grafos rotulados com pesos.")

        d = [self.INF] * self.n
        rot = [None] * self.n
        d[origem] = 0

        nao_visitados = {i for i in range(self.n) if self.nomes[i] is not None}

        while nao_visitados:
            u = min(nao_visitados, key=lambda x: d[x])

            if d[u] == self.INF:
                break

            nao_visitados.remove(u)

            for v in range(self.n):
                peso = self.adj[u][v]
                if v in nao_visitados and peso != self.INF:
                    nova_distancia = d[u] + peso
                    if nova_distancia < d[v]:
                        d[v] = nova_distancia
                        rot[v] = u

        return d, rot

    def prim(self, inicio=None):
        validos = [i for i, nome in self.nomes.items() if nome is not None]
        if not validos:
            return 0, []

        # traduz ponto de partida
        if inicio is None:
            u0 = validos[0]
        elif isinstance(inicio, str):
            # busca índice pelo nome
            rev = {v: k for k, v in self.nomes.items() if v is not None}
            if inicio not in rev:
                raise ValueError(f"Vértice '{inicio}' não existe.")
            u0 = rev[inicio]
        else:
            u0 = inicio
            if u0 not in validos:
                raise ValueError(f"Índice de vértice inválido: {u0}")

        visitados = {u0}
        mst = []
        custo_total = 0

        while len(visitados) < len(validos):
            menor = self.INF
            sel_u = sel_v = None

            for u in visitados:
                for v in validos:
                    if v in visitados:
                        continue
                    peso = self.adj[u][v]
                    if (self.rotulado and peso != self.INF or
                            not self.rotulado and peso != 0):
                        if peso < menor:
                            menor = peso
                            sel_u, sel_v = u, v

            if sel_v is None:
                # grafo desconexo
                break

            visitados.add(sel_v)
            custo_total += menor
            mst.append((self.nomes[sel_u], self.nomes[sel_v], menor))

        return custo_total, mst

class GrafoMatrizND:
    TAM_MAX_DEFAULT = 100
    INF = float('inf')

    def __init__(self, n=TAM_MAX_DEFAULT, rotulado=False):
        self.n = n  #
        self.m = 0  #
        self.rotulado = rotulado
        self.nomes = {i: f"V{i}" for i in range(n)}
        valor_padrao = self.INF if rotulado else 0
        self.adj = [[valor_padrao for _ in range(n)] for _ in range(n)]

    def insereA(self, vertice_origem, vertice_alvo, peso=1.0):
        if self.rotulado:
            if self.adj[vertice_origem][vertice_alvo] == self.INF:
                self.adj[vertice_origem][vertice_alvo] = peso
                self.adj[vertice_alvo][vertice_origem] = peso
                self.m += 1
        else:
            if self.adj[vertice_origem][vertice_alvo] == 0:
                self.adj[vertice_origem][vertice_alvo] = 1
                self.adj[vertice_alvo][vertice_origem] = 1
                self.m += 1

    def removeA(self, vertice_origem, vertice_alvo):
        if self.rotulado:
            if self.adj[vertice_origem][vertice_alvo] != self.INF:
                self.adj[vertice_origem][vertice_alvo] = self.INF
                self.adj[vertice_alvo][vertice_origem] = self.INF
                self.m -= 1
        else:
            if self.adj[vertice_origem][vertice_alvo] == 1:
                self.adj[vertice_origem][vertice_alvo] = 0
                self.adj[vertice_alvo][vertice_origem] = 0
                self.m -= 1

    def grau(self, vertice):
        if isinstance(vertice, int):
            if vertice not in self.nomes or self.nomes[vertice] is None:
                raise ValueError("Vértice não existe.")
        else:
            if vertice not in self.nomes.values():
                raise ValueError("Vértice não existe.")
            vertice = list(self.nomes.keys())[list(self.nomes.values()).index(vertice)]

        return sum(1 for j in range(self.n) if self.adj[vertice][j] != self.INF and self.adj[vertice][j] != 0)

    def removeV(self, vertice):
        if isinstance(vertice, int):
            if vertice not in self.nomes or self.nomes[vertice] is None:
                raise ValueError("Vértice não existe.")
        else:
            if vertice not in self.nomes.values():
                raise ValueError("Vértice não existe.")
            vertice = list(self.nomes.keys())[list(self.nomes.values()).index(vertice)]

        self.nomes[vertice] = None
        for i in range(self.n):
            self.adj[vertice][i] = 0
            self.adj[i][vertice] = 0
        self.m = sum(
            1 for i in range(self.n) for j in range(i, self.n) if self.adj[i][j] != 0 and self.adj[i][j] != self.INF)

    def completo(self):
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.nomes[i] is not None and self.nomes[j] is not None:
                    if self.adj[i][j] == 0 or self.adj[i][j] == self.INF:
                        return False
        return True

    def show(self):
        nomes_ordenados = [i for i in sorted(self.nomes.keys()) if self.nomes[i] is not None]
        print("   " + " ".join(f"{self.nomes[i]:3}" for i in nomes_ordenados))
        for vertice in nomes_ordenados:
            linha = " ".join(f"{self.adj[vertice][j]:3}" for j in nomes_ordenados)
            print(f"{self.nomes[vertice]:2} | {linha}")

    def complementar(self):
        grafoComp = GrafoMatrizND(self.n, self.rotulado)
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    if not self.rotulado:
                        grafoComp.adj[i][j] = 1 if self.adj[i][j] == 0 else 0
                    else:
                        if self.adj[i][j] == self.INF:
                            grafoComp.adj[i][j] = 1
                        else:
                            grafoComp.adj[i][j] = self.INF
        return grafoComp

    def prim(self, inicio=None):
        validos = [i for i, nome in self.nomes.items() if nome is not None]
        if not validos:
            return 0, []

        if inicio is None:
            u0 = validos[0]
        elif isinstance(inicio, str):
            rev = {v: k for k, v in self.nomes.items() if v is not None}
            if inicio not in rev:
                raise ValueError(f"Vértice '{inicio}' não existe.")
            u0 = rev[inicio]
        else:
            u0 = inicio
            if u0 not in validos:
                raise ValueError(f"Índice de vértice inválido: {u0}")

        visitados = {u0}
        mst = []
        custo_total = 0

        while len(visitados) < len(validos):
            menor = self.INF
            sel_u = sel_v = None

            for u in visitados:
                for v in validos:
                    if v in visitados:
                        continue
                    peso = self.adj[u][v]
                    if (self.rotulado and peso != self.INF or
                            not self.rotulado and peso != 0):
                        if peso < menor:
                            menor = peso
                            sel_u, sel_v = u, v

            if sel_v is None:
                # desconexo
                break

            visitados.add(sel_v)
            custo_total += menor
            mst.append((self.nomes[sel_u], self.nomes[sel_v], menor))

        return custo_total, mst


    def coloracao(self):
        validos = [i for i, nome in self.nomes.items() if nome is not None]
        classes = []
        for u in validos:
            k = 0
            while True:
                if k >= len(classes):
                    classes.append(set())
                vizinhos = [v for v in validos if self.adj[u][v] != 0 and self.adj[u][v] != self.INF]
                if not any(v in classes[k] for v in vizinhos):
                    classes[k].add(u)
                    break
                k += 1
        return [{self.nomes[v] for v in classe} for classe in classes]