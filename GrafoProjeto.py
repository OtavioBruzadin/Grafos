from collections import deque

import networkx as nx
import matplotlib.pyplot as plt

class GrafoMatriz:
    TAM_MAX_DEFAULT = 10000
    INF = float('inf')

    def __init__(self, rotulado=False):
        self.n = 0
        self.m = 0
        self.rotulado = rotulado
        self.indices = {}  # mapeia índice -> nome
        self.nomes = {}    # mapeia nome -> índice
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

        # Remove o vértice dos mapeamentos originais
        del self.nomes[vertice]
        old_indices = self.indices.copy()
        del old_indices[index_removido]

        # Remove a linha correspondente e a coluna de cada linha
        del self.adj[index_removido]
        for linha in self.adj:
            del linha[index_removido]
        self.n -= 1

        # Reconstroi os mapeamentos de índices e nomes com índices de 0 a n-1
        new_indices = {}
        new_nomes = {}
        remaining = [old_indices[k] for k in sorted(old_indices.keys())]
        for novo_indice, nome in enumerate(remaining):
            new_indices[novo_indice] = nome
            new_nomes[nome] = novo_indice

        self.indices = new_indices
        self.nomes = new_nomes

        # Recalcula o número de arestas após a remoção
        novo_m = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.rotulado:
                    if self.adj[i][j] != self.INF:
                        novo_m += 1
                else:
                    if self.adj[i][j] != 0:
                        novo_m += 1
        self.m = novo_m
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
            tipo = arq.readline().strip()
            if tipo != "6":
                print("Tipo de grafo não é compativel")
                return None

            num_vertices = int(arq.readline().strip())
            for _ in range(num_vertices):
                linha = arq.readline().strip()
                partes = linha.split(maxsplit=1)
                if len(partes) < 2:
                    continue

                nome_vertice = partes[1]
                self.adicionarVertice(nome_vertice)

            num_arestas = int(arq.readline().strip())
            for _ in range(num_arestas):
                linha = arq.readline().strip()
                partes = linha.split()
                if len(partes) != 3:
                    continue
                origem_idx = int(partes[0])
                destino_idx = int(partes[1])
                try:
                    peso = float(partes[2])
                except ValueError:
                    peso = partes[2]

                origem_nome = self.indices.get(origem_idx)
                destino_nome = self.indices.get(destino_idx)
                if origem_nome is None or destino_nome is None:
                    print(f"Índices inválidos na aresta: {linha}")
                    continue
                self.insereA(origem_nome, destino_nome, peso)
        return self.adj

    def gravarArquivoMatrizAdj(self, arquivo):

        with open(arquivo, 'w') as arq:
            arq.write("6\n")
            arq.write(f"{self.n}\n")
            for i in range(self.n):
                nome = self.indices[i]
                arq.write(f"{i} {nome}\n")
            arq.write(f"{self.m}\n")
            for i in range(self.n):
                for j in range(self.n):
                    if self.rotulado:
                        if self.adj[i][j] != self.INF:
                            arq.write(f"{i} {j} {self.adj[i][j]}\n")
                    else:
                        if self.adj[i][j] != 0:
                            arq.write(f"{i} {j} {self.adj[i][j]}\n")

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

    def visitarNo(self, v, ordem_visita):

        print(f"Visitado: {self.indices[v]}")
        ordem_visita.append(self.indices[v])

    def noAdjacente(self, n, visitados):

        for i in range(self.n):
            if not visitados[i]:
                if self.rotulado:
                    if self.adj[n][i] != self.INF:
                        return i
                else:
                    if self.adj[n][i] != 0:
                        return i
        return -1

    def percursoProfundidade(self, vInicio):

        if isinstance(vInicio, str):
            if vInicio not in self.nomes:
                raise ValueError("Vértice não encontrado.")
            vInicio = self.nomes[vInicio]

        visitados = [False] * self.n
        pilha = []
        ordem_visita = []

        self.visitarNo(vInicio, ordem_visita)
        visitados[vInicio] = True
        pilha.append(vInicio)

        while pilha:
            n = pilha.pop()
            m = self.noAdjacente(n, visitados)
            while m != -1:
                self.visitarNo(m, ordem_visita)
                pilha.append(n)
                visitados[m] = True
                n = m
                m = self.noAdjacente(n, visitados)
        return ordem_visita

    def percursoLargura(self, vInicio):

        if isinstance(vInicio, str):
            if vInicio not in self.nomes:
                raise ValueError("Vértice não encontrado.")
            vInicio = self.nomes[vInicio]

        visitados = [False] * self.n
        fila = deque()
        ordem_visita = []

        self.visitarNo(vInicio, ordem_visita)
        visitados[vInicio] = True
        fila.append(vInicio)

        while fila:
            n = fila.popleft()

            m = self.noAdjacente(n, visitados)
            while m != -1:
                self.visitarNo(m, ordem_visita)
                visitados[m] = True
                fila.append(m)

                m = self.noAdjacente(n, visitados)

        return ordem_visita
    

    def listToMatrix(self):
        matrix = [[0 for _ in range(len(self.listaAdj))] for _ in range(len(self.listaAdj))]
        for v in range(len(self.listaAdj)):
            if self.listaAdj[v] is not None:
                for w in self.listaAdj[v]:
                    matrix[v][w] = 1
        self.matrizAdj = matrix
        return matrix

    def matrixToList(self):
        self.listaAdj = [[] for _ in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.n):
                if self.rotulado:
                    if self.adj[i][j] != self.INF:
                        self.listaAdj[i].append(j)
                else:
                    if self.adj[i][j] != 0:
                        self.listaAdj[i].append(j)
        
        print("\nLista de adjacência:")
        for v in range(self.n):
            if self.listaAdj[v] is not None:
                print(f"{self.indices[v]}: {' '.join(map(str, self.listaAdj[v]))}")
        return self.listaAdj

    def prim(self, inicio=None):
        validos = list(range(self.n))
        if not validos:
            return 0, []

        # determina o vértice inicial
        if inicio is None:
            u0 = validos[0]
        elif isinstance(inicio, str):
            if inicio not in self.nomes:
                raise ValueError(f"Vértice '{inicio}' não existe.")
            u0 = self.nomes[inicio]
        else:
            u0 = inicio
            if u0 not in validos:
                raise ValueError(f"Índice de vértice inválido: {u0}")

        visitados = {u0}
        mst = []
        custo_total = 0

        # constrói a MST
        while len(visitados) < self.n:
            menor = self.INF
            sel_u = sel_v = None

            for u in visitados:
                for v in validos:
                    if v in visitados:
                        continue
                    peso = self.adj[u][v]
                    # verifica existência de aresta
                    if peso != (self.INF if self.rotulado else 0):
                        if peso < menor:
                            menor = peso
                            sel_u, sel_v = u, v

            # grafo desconexo?
            if sel_v is None:
                break

            visitados.add(sel_v)
            custo_total += menor
            # adiciona aresta pelo nome dos vértices
            mst.append((self.indices[sel_u], self.indices[sel_v], menor))

        return custo_total, mst

    def dijkstra(self, origem):
        if not self.rotulado:
            raise ValueError("O algoritmo de Dijkstra requer grafos rotulados com pesos.")

        # lista de vértices válidos
        validos = [i for i, nome in self.nomes.items() if nome is not None]

        # traduz origem
        if isinstance(origem, str):
            rev = {v: k for k, v in self.nomes.items() if v is not None}
            if origem not in rev:
                raise ValueError(f"Vértice '{origem}' não existe.")
            src = rev[origem]
        else:
            src = origem
            if src not in validos:
                raise ValueError(f"Índice de vértice inválido: {src}")

        # inicialização
        d = {i: self.INF for i in validos}
        pred = {i: None for i in validos}
        d[src] = 0
        nao_visitados = set(validos)

        while nao_visitados:
            u = min(nao_visitados, key=lambda x: d[x])
            if d[u] == self.INF:
                break
            nao_visitados.remove(u)

            for v in validos:
                peso = self.adj[u][v]
                if v in nao_visitados and peso != self.INF:
                    nova_dist = d[u] + peso
                    if nova_dist < d[v]:
                        d[v] = nova_dist
                        pred[v] = u

        # mapeia resultados para nomes
        distancias = {self.nomes[i]: d[i] for i in validos}
        predecessores = {self.nomes[i]: (self.nomes[pred[i]] if pred[i] is not None else None) for i in validos}

        return distancias, predecessores
    

    def hConexidade(self):
        # Verifica a conectividade no grafo original
        visitados = [False] * self.n
        self.dfs(0, visitados)
        if not all(visitados):
            return False

        # Cria o grafo transposto (com todas as arestas invertidas)
        grafo_transposto = GrafoMatriz(rotulado=self.rotulado)
        for vertice in self.nomes:
            grafo_transposto.adicionarVertice(vertice)
        
        for i in range(self.n):
            for j in range(self.n):
                if self.rotulado:
                    if self.adj[i][j] != self.INF:
                        grafo_transposto.insereA(self.indices[i], self.indices[j], self.adj[i][j])
                else:
                    if self.adj[i][j] != 0:
                        grafo_transposto.insereA(self.indices[i], self.indices[j])

        # Verifica a conectividade no grafo transposto
        visitados = [False] * self.n
        grafo_transposto.dfs(0, visitados)
        if not all(visitados):
            return False

        return True
    

    def caminhoEuleriano(self):
        visitados = [False] * self.n
        self.dfs(0, visitados)

        if not all(visitados):
            return False

        origem, destino = 0, 0 

        for i in range(self.n):
            in_degree = self.inDegree(self.indices[i])
            out_degree = self.outDegree(self.indices[i])
            if in_degree != out_degree:

                if in_degree - out_degree == 1:
                    origem += 1

                elif out_degree - in_degree == 1:
                    destino += 1

                else:
                    return False

        return (origem == 1 and destino == 1) or (origem == 0 and destino == 0)


    def listarGraus(self):
        for nome in self.nomes:
            grau = self.degree(nome)
            print(f"Vértice: {nome}, Grau: {grau}")


    def plotarGrafo(self):
        G = nx.DiGraph() if self.rotulado else nx.Graph()

        for nome in self.nomes:
            G.add_node(nome)

        for i in range(self.n):
            for j in range(self.n):
                if self.rotulado and self.adj[i][j] != self.INF:
                    G.add_edge(self.indices[i], self.indices[j], weight=self.adj[i][j])
                elif not self.rotulado and self.adj[i][j] != 0:
                    G.add_edge(self.indices[i], self.indices[j])

        pos = nx.spring_layout(G) 
        plt.figure(figsize=(10, 8))
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")
        
        if self.rotulado:
            edge_labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        plt.title("Grafo")
        plt.show()