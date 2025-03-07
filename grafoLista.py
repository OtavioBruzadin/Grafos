class GrafoLista:
    TAM_MAX_DEFAULT = 100 
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n 
        self.m = 0 
        self.listaAdj = [[] for i in range(self.n)]
        
    def insereA(self, v, w):
        self.listaAdj[v].append(w)
        self.m+=1
     
    def removeA(self, v, w):
        self.listaAdj[v].remove(w)
        self.m-=1

    def removerVertice(self, v):
            if v >= self.n:
                print("Vértice inválido")
                return
            for i in range(self.n):
                if v in self.listaAdj[i]:
                    self.listaAdj[i].remove(v)
                    self.m -= 1
            self.listaAdj.pop(v)
            self.n -= 1
            for i in range(len(self.listaAdj)):
                self.listaAdj[i] = [x - 1 if x > v else x for x in self.listaAdj[i]]

    def inDegree(self,v):
        grauVertice = 0
        for i in range(self.n):
            if v in self.listaAdj[i]:
                grauVertice += 1
        return grauVertice
    
    def outDegree(self,v):
        return len(self.listaAdj[v])

    def degree(self, v):
        grauVerticeIn = self.inDegree(v)
        grauVerticeOut = self.outDegree(v)
        totalGrau = grauVerticeIn + grauVerticeOut
        return totalGrau
    
    def isEqual(ex25,ex29):
        if ex25.listaAdj == ex29.listaAdj:
            return True
        else:
            return False
        
    def listToMatrix(self):
        matrix = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for v in range(self.n):
            for w in self.listaAdj[v]:
                matrix[v][w] = 1
        return matrix
    
    def matrixToList(self, matrix):
        self.n = len(matrix)
        self.listaAdj = [[] for _ in range(self.n)]
        for v in range(self.n):
            for w in range(self.n):
                if matrix[v][w] != 0:
                    self.insereA(v, w)
        print("\nLista de adjacência:")
        for v in range(self.n):
            print(f"{v}: {' '.join(map(str, self.listaAdj[v]))}")
        return self.listaAdj

    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            print(f"\n{i:2d}: ", end="")
            for w in range(len(self.listaAdj[i])):
                val = self.listaAdj[i][w]
                print(f"{val:2d}", end="") 
        print("\n\nfim da impressao do grafo." )
    
    def inverter_adj(self):
        for v in range(len(self.listaAdj)):
            self.listaAdj[v].reverse()

    def eh_completo(self):
        total_vertices = len(self.listaAdj)
        for v in range(len(self.listaAdj)):
            if len(self.listaAdj[v]) != total_vertices - 1:
                return False
        return True

@classmethod
    def from_arquivo(cls, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            vertices = int(arquivo.readline().strip())
            arestas = int(arquivo.readline().strip())
            grafo = cls(vertices)
            for _ in range(arestas):
                u, v = map(int, arquivo.readline().strip().split())
                grafo.add_aresta(u, v)
        return grafo

class TGrafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.lista_adj = {i: [] for i in range(vertices)}
    
    def insereA(self, u, v):
        self.lista_adj[u].append(v)

    def remover_vertice(self, vertice):
        if vertice in self.lista_adj:
            del self.lista_adj[vertice]
            for v in self.lista_adj:
                if vertice in self.lista_adj[v]:
                    self.lista_adj[v].remove(vertice)
    
    def eh_fonte(self, vertice):
        grau_entrada = {i: 0 for i in range(self.vertices)}
        
        for v in self.lista_adj:
            for vizinho in self.lista_adj[v]:
                grau_entrada[vizinho] += 1
        
        if grau_entrada[vertice] == 0 and len(self.lista_adj[vertice]) > 0:
            return 1
        return 0
    
    def show(self):
        for vertice, vizinhos in self.lista_adj.items():
            print(f"{vertice}: {vizinhos}")
    
    def eh_sorvedouro(self, vertice):
        grau_entrada = {i: 0 for i in range(self.vertices)}
        
        for v in self.lista_adj:
            for vizinho in self.lista_adj[v]:
                grau_entrada[vizinho] += 1
        
        if grau_entrada[vertice] > 0 and len(self.lista_adj[vertice]) == 0:
            return 1
        return 0
    
    def eh_simetrico(self):
        for u in self.lista_adj:
            for v in self.lista_adj[u]:
                if u not in self.lista_adj[v]:
                    return 0
        return 1
    
    def eh_completo(self):
        total_vertices = len(self.lista_adj)
        for v in self.lista_adj:
            if len(self.lista_adj[v]) != total_vertices - 1:
                return False
        return True
