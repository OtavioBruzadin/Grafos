from grafoMatriz import GrafoMatriz

print('Lista 1 Teoria dos Grafos')

print('\nExercicio 1')
ex1 = GrafoMatriz()
ex1_rotulado = GrafoMatriz(True)

for nome in ["A", "B", "C", "D", "E"]:
    ex1.adicionarVertice(nome)
    ex1_rotulado.adicionarVertice(nome)

ex1.insereA("A", "B")
ex1.insereA("C", "B")
ex1.insereA("D", "B")
ex1.insereA("E", "B")

ex1_rotulado.insereA("A", "B", 1.0)
ex1_rotulado.insereA("C", "B", 2.0)
ex1_rotulado.insereA("D", "B", 3.0)
ex1_rotulado.insereA("E", "B", 4.0)

print("Grau de entrada do vértice B:", ex1.inDegree("B"))
print("Grau de entrada do vértice A:", ex1.inDegree("A"))

print('\nExercicio 2')
ex2 = GrafoMatriz()
ex2_rotulado = GrafoMatriz(True)

for nome in ["X", "Y", "Z", "W", "V"]:
    ex2.adicionarVertice(nome)
    ex2_rotulado.adicionarVertice(nome)

ex2.insereA("X", "Y")
ex2.insereA("X", "Z")
ex2.insereA("Y", "W")
ex2.insereA("Y", "V")

ex2_rotulado.insereA("X", "Y", 4.0)
ex2_rotulado.insereA("X", "Z", 8.0)
ex2_rotulado.insereA("Y", "W", 16.0)
ex2_rotulado.insereA("Y", "V", 32.0)

print("Grau de saída do vértice X:", ex2.outDegree("X"))
print("Grau de saída do vértice X (rotulado):", ex2_rotulado.outDegree("X"))

print('\nExercicio 3')
ex3 = GrafoMatriz()
ex3_rotulado = GrafoMatriz(True)

for nome in ["P", "Q", "R", "S", "T"]:
    ex3.adicionarVertice(nome)
    ex3_rotulado.adicionarVertice(nome)

ex3.insereA("P", "Q")
ex3.insereA("P", "R")
ex3.insereA("P", "S")
ex3.insereA("P", "T")
ex3.insereA("Q", "P")
ex3.insereA("R", "P")
ex3.insereA("S", "T")
ex3.insereA("T", "R")

ex3_rotulado.insereA("P", "Q", 1.0)
ex3_rotulado.insereA("P", "R", 2.0)
ex3_rotulado.insereA("P", "S", 3.0)
ex3_rotulado.insereA("P", "T", 4.0)
ex3_rotulado.insereA("Q", "P", 5.0)
ex3_rotulado.insereA("R", "P", 6.0)
ex3_rotulado.insereA("S", "T", 7.0)
ex3_rotulado.insereA("T", "R", 8.0)

print("Vértice P é sorvedouro?:", ex3.degree("P"))
print("Vértice Q é sorvedouro?:", ex3.degree("Q")) 

print("Vértice P rotulado é sorvedouro?:", ex3_rotulado.degree("P"))
print("Vértice Q rotulado é sorvedouro?:", ex3_rotulado.degree("Q"))

print('\nExercicio 4')
ex4 = GrafoMatriz()
ex4_rotulado = GrafoMatriz(True)

for nome in ["M", "N", "O", "P", "Q"]:
    ex4.adicionarVertice(nome)
    ex4_rotulado.adicionarVertice(nome)

ex4.insereA("M", "N")
ex4.insereA("M", "O")
ex4.insereA("O", "P")
ex4.insereA("P", "Q")

ex4_rotulado.insereA("M", "N", 2.0)
ex4_rotulado.insereA("M", "O", 4.0)
ex4_rotulado.insereA("Q", "P", 6.0)
ex4_rotulado.insereA("P", "Q", 8.0)

ex4.show()
print("Vértice M é fonte?:", ex4.isSource("M"))
print("Vértice Q é fonte?:", ex4.isSource("Q"))
ex4_rotulado.show()
print("Vértice M rotulado é fonte?:", ex4_rotulado.isSource("M"))
print("Vértice Q rotulado é fonte?:", ex4_rotulado.isSource("Q"))

print('\nExercicio 5')
ex5 = GrafoMatriz()
ex5_rotulado = GrafoMatriz(True)

for nome in ["U", "V", "W", "X", "Y"]:
    ex5.adicionarVertice(nome)
    ex5_rotulado.adicionarVertice(nome)

ex5.insereA("U", "V")
ex5.insereA("W", "V")
ex5.insereA("W", "X")
ex5.insereA("X", "Y")

ex5_rotulado.insereA("U", "V", 2.0)
ex5_rotulado.insereA("W", "V", 3.0)
ex5_rotulado.insereA("W", "X", 4.0)
ex5_rotulado.insereA("X", "Y", 5.0)


ex5.show()
print("Vértice U é sorvedouro?:", ex5.isSorvedouro("U"))
print("Vértice V é sorvedouro?:", ex5.isSorvedouro("V"))

ex5_rotulado.show()
print("Vértice rotulado U é sorvedouro?:", ex5_rotulado.isSorvedouro("U"))
print("Vértice rotulado V é sorvedouro?:", ex5_rotulado.isSorvedouro("V"))

print('\nExercicio 5')
ex12= GrafoMatriz()
ex12_rotulado = GrafoMatriz(True)

for nome in ["Joao", "Marcos", "Paulo", "Vinicius", "Lucas"]:
    ex12.adicionarVertice(nome)
    ex12_rotulado.adicionarVertice(nome)

ex12.insereA("Joao", "Vinicius")
ex12.insereA("Vinicius", "Marcos")
ex12.insereA("Marcos", "Paulo")
ex12.insereA("Lucas", "Joao")

ex12_rotulado.insereA("Joao", "Vinicius", 2.0)
ex12_rotulado.insereA("Vinicius", "Marcos", 3.0)
ex12_rotulado.insereA("Marcos", "Paulo", 4.0)
ex12_rotulado.insereA("Lucas", "Joao", 5.0)

ex12.show()
ex12.removerVertice("Vinicius")
ex12.show()

ex12_rotulado.show()
ex12_rotulado.removerVertice("Vinicius")
ex12_rotulado.show()
