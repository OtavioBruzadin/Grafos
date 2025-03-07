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
            self.adj[vertice][i] = 0
            self.adj[i][vertice] = 0

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

    def grafo_complementar(self):
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
    
      

    def dfs(self, vertice, visitados):
        visitados[vertice] = True  
        for i in range(self.n):
            if self.adj[vertice][i] != self.INF and self.adj[vertice][i] != 0 and not visitados[i]:
                self.dfs(i, visitados)


    def categoriaConexidade(self):
        visitados = [False for _ in range(self.n)]
        self.dfs(0,visitados)
        for v in visitados:
            if not v:
                print("0") 
                return
            
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
            print("3")
            return

        comparacaoSuperior = True
        for i in range(n):
            for j in range(n):
                if i > j and grafo[i][j] == 0:
                    comparacaoSuperior = False
                    break
            if not comparacaoSuperior:
                break

        if comparacaoSuperior:
            print("2")
            return

        comparacaoInferior = True
        for i in range(n):
            for j in range(n):
                if i < j and grafo[i][j] == 0:
                    comparacaoInferior = False
                    break
            if not comparacaoInferior:
                break

        if comparacaoInferior:
            print("2")
            return
        
        print("1")