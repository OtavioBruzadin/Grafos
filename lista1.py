from grafoMatriz import GrafoMatriz

print('Lista 1 Teoria dos Grafos')
# Coluna Recebe e Linha envia Linha -> coluna
print('\nExercicio 1')
ex1naoRotulado = GrafoMatriz(5)

ex1naoRotulado.insereA(0, 1)
ex1naoRotulado.insereA(2, 1)
ex1naoRotulado.insereA(3, 1)
ex1naoRotulado.insereA(4, 1)

print("Grau de entrada do vértice não rotulado 1:", ex1naoRotulado.inDegree(1))
print("Grau de entrada do vértice não rotulado 0:", ex1naoRotulado.inDegree(0))

print('\nExercicio 2')
ex2naoRotulado = GrafoMatriz(5)
ex2rotulado = GrafoMatriz(5, True)

ex2naoRotulado.insereA(0, 1)
ex2naoRotulado.insereA(0, 2)
ex2naoRotulado.insereA(0, 3)
ex2naoRotulado.insereA(0, 4)

ex2rotulado.insereA(0, 1, 4.0)
ex2rotulado.insereA(0, 2, 8.0)
ex2rotulado.insereA(1, 3, 16.0)
ex2rotulado.insereA(1, 4, 32.0)

print("Grau de saída do vértice não rotulado 0:", ex2naoRotulado.outDegree(0))
print("Grau de saída do vértice não rotulado 1:", ex2naoRotulado.outDegree(1))

print("Grau de saída do vértice rotulado 0:", ex2rotulado.outDegree(0))
print("Grau de saída do vértice rotulado 1:", ex2rotulado.outDegree(1))

print('\nExercicio 3')

ex3naoRotulado = GrafoMatriz(5)
ex3rotulado = GrafoMatriz(5, True)

ex3naoRotulado.insereA(0, 1)
ex3naoRotulado.insereA(0, 2)
ex3naoRotulado.insereA(0, 3)
ex3naoRotulado.insereA(0, 4)
ex3naoRotulado.insereA(1, 0)
ex3naoRotulado.insereA(2, 0)
ex3naoRotulado.insereA(3, 0)
ex3naoRotulado.insereA(4, 0)

ex3rotulado.insereA(0, 1, 4.0)
ex3rotulado.insereA(0, 2, 8.0)
ex3rotulado.insereA(2, 3, 16.0)
ex3rotulado.insereA(1, 4, 32.0)
ex3rotulado.show()
ex3rotulado.removeV(1)
ex3rotulado.show()
print("Grau do vértice não rotulado 0:", ex3naoRotulado.degree(0))
print("Grau do vértice não rotulado 1:", ex3naoRotulado.degree(1))

print("Grau do vértice rotulado 0:", ex3rotulado.degree(0))
print("Grau do vértice rotulado 1:", ex3rotulado.degree(1))

print('\nExercicio 4')

ex4naoRotulado = GrafoMatriz(5)
ex4rotulado = GrafoMatriz(5, True)

ex4naoRotulado.insereA(0, 1)
ex4naoRotulado.insereA(0, 2)
ex4naoRotulado.insereA(0, 3)
ex4naoRotulado.insereA(0, 4)
ex4naoRotulado.insereA(2, 1)
ex4naoRotulado.insereA(3, 1)

ex4rotulado.insereA(0, 1, 4.0)
ex4rotulado.insereA(0, 2, 8.0)
ex4rotulado.insereA(1, 3, 16.0)
ex4rotulado.insereA(1, 4, 32.0)

print("Vértice não rotulado 0 é fonte?:", ex4naoRotulado.isSource(0))
print("Vértice não rotulado 1 é fonte?:", ex4naoRotulado.isSource(1))

print("Vértice rotulado 0 é fonte?:", ex4rotulado.isSource(0))
print("Vértice rotulado 1 é fonte?:", ex4rotulado.isSource(1))

print('\nExercicio 5')

ex5naoRotulado = GrafoMatriz(5)
ex5rotulado = GrafoMatriz(5, True)

ex5naoRotulado.insereA(0, 1)
ex5naoRotulado.insereA(0, 2)
ex5naoRotulado.insereA(0, 3)
ex5naoRotulado.insereA(0, 4)
ex5naoRotulado.insereA(2, 1)
ex5naoRotulado.insereA(3, 1)

ex5rotulado.insereA(0, 1, 4.0)
ex5rotulado.insereA(0, 2, 8.0)
ex5rotulado.insereA(1, 3, 16.0)
ex5rotulado.insereA(1, 4, 32.0)

print("Vértice não rotulado 0 é Sorvedouro?:", ex5naoRotulado.isSorvedouro(0))
print("Vértice não rotulado 1 é Sorvedouro?:", ex5naoRotulado.isSorvedouro(1))

print("Vértice rotulado 0 é Sorvedouro?:", ex5rotulado.isSorvedouro(0))
print("Vértice rotulado 3 é Sorvedouro?:", ex5rotulado.isSorvedouro(3))