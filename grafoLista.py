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
    
    def isEqual(grafoA,grafoB):
        if grafoA.listaAdj == grafoB.listaAdj:
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
