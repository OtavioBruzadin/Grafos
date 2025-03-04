from grafoMatriz import GrafoMatriz

print('Lista 1 Teoria dos Grafos')
# Coluna Recebe e Linha envia Linha -> coluna
print('\nExercicio 1')
ex1 = GrafoMatriz(5)

ex1.insereA(0, 1)
ex1.insereA(2, 1)
ex1.insereA(3, 1)
ex1.insereA(4, 1)

print("Grau de entrada do vértice não rotulado 1:", ex1.inDegree(1))    #expected 4
print("Grau de entrada do vértice não rotulado 0:", ex1.inDegree(0))    #expected 0

print('\nExercicio 2')
ex2 = GrafoMatriz(5)
ex2rotulado = GrafoMatriz(5, True)

ex2.insereA(0, 1)
ex2.insereA(0, 2)
ex2.insereA(0, 3)
ex2.insereA(0, 4)

ex2rotulado.insereA(0, 1, 4.0)
ex2rotulado.insereA(0, 2, 8.0)
ex2rotulado.insereA(1, 3, 16.0)
ex2rotulado.insereA(1, 4, 32.0)

print("Grau de saída do vértice 0:", ex2.outDegree(0))   #expected 4
print("Grau de saída do vértice 1:", ex2.outDegree(1))   #expected 0

print("Grau de saída do vértice rotulado 0:", ex2rotulado.outDegree(0))   #expected 2
print("Grau de saída do vértice rotulado 1:", ex2rotulado.outDegree(1))   #expected 2

print('\nExercicio 3')

ex3 = GrafoMatriz(5)
ex3rotulado = GrafoMatriz(5, True)

ex3.insereA(0, 1)
ex3.insereA(0, 2)
ex3.insereA(0, 3)
ex3.insereA(0, 4)
ex3.insereA(1, 0)
ex3.insereA(2, 0)
ex3.insereA(3, 0)
ex3.insereA(4, 0)

ex3rotulado.insereA(0, 1, 4.0)
ex3rotulado.insereA(0, 2, 8.0)
ex3rotulado.insereA(2, 3, 16.0)
ex3rotulado.insereA(1, 4, 32.0)
ex3rotulado.show()
ex3rotulado.removeV(1)
ex3rotulado.show()
print("Grau do vértice 0:", ex3.degree(0))   #expected 8
print("Grau do vértice 1:", ex3.degree(1))   #expected 2

print("Grau do vértice rotulado 0:", ex3rotulado.degree(0))       #expected 1
print("Grau do vértice rotulado 2:", ex3rotulado.degree(2))       #expected 2

print('\nExercicio 4')

ex4 = GrafoMatriz(5)
ex4rotulado = GrafoMatriz(5, True)

ex4.insereA(0, 1)
ex4.insereA(0, 2)
ex4.insereA(0, 3)
ex4.insereA(0, 4)
ex4.insereA(2, 1)
ex4.insereA(3, 1)

ex4rotulado.insereA(0, 1, 4.0)
ex4rotulado.insereA(0, 2, 8.0)
ex4rotulado.insereA(1, 3, 16.0)
ex4rotulado.insereA(1, 4, 32.0)

print("Vértice 0 é fonte?:", ex4.isSource(0))   #expected 1
print("Vértice 1 é fonte?:", ex4.isSource(1))   #expected 0

print("Vértice rotulado 0 é fonte?:", ex4rotulado.isSource(0)) #expected 1
print("Vértice rotulado 1 é fonte?:", ex4rotulado.isSource(1)) #expected 0

print('\nExercicio 5')

ex5 = GrafoMatriz(5)
ex5rotulado = GrafoMatriz(5, True)

ex5.insereA(0, 1)
ex5.insereA(0, 2)
ex5.insereA(0, 3)
ex5.insereA(0, 4)
ex5.insereA(2, 1)
ex5.insereA(3, 1)

ex5rotulado.insereA(0, 1, 4.0)
ex5rotulado.insereA(0, 2, 8.0)
ex5rotulado.insereA(1, 3, 16.0)
ex5rotulado.insereA(1, 4, 32.0)

print("Vértice 0 é Sorvedouro?:", ex5.isSorvedouro(0)) #expected 0
print("Vértice 1 é Sorvedouro?:", ex5.isSorvedouro(1)) #expected 1

print("Vértice rotulado 0 é Sorvedouro?:", ex5rotulado.isSorvedouro(0)) #expected 0
print("Vértice rotulado 3 é Sorvedouro?:", ex5rotulado.isSorvedouro(3)) #expected 1

print('\nExercicio 30')


ex30 = GrafoMatriz(5)
ex30rotulado = GrafoMatriz(5, True)

ex30.insereA(0, 1)
ex30.insereA(0, 2)
ex30.insereA(1, 3)
ex30.insereA(2, 4)

print('\nANTES')
ex30.show()
ex30.removeV(2)
print('\nDEPOIS')

ex30.show()

ex30rotulado.insereA(0, 1, 4.0)
ex30rotulado.insereA(0, 2, 8.0)
ex30rotulado.insereA(2, 3, 16.0)
ex30rotulado.insereA(1, 4, 32.0)

print('\nANTES')
ex30rotulado.show()
ex30rotulado.removeV(1)
print('\nDEPOIS')

ex30rotulado.show()


print('\nExercicio 13')

ex13 = GrafoMatriz(3)
ex13rotulado = GrafoMatriz(3, True)

ex13.insereA(0, 1)
ex13.insereA(0, 2)
ex13.insereA(1, 0)
ex13.insereA(1, 2)
ex13.insereA(2, 0)
ex13.show()
print('\nO grafo não rotulado é completo? : ', ex13.isComplete()) #expected False

ex13rotulado.insereA(0, 1, 4.0)
ex13rotulado.insereA(0, 2, 8.0)
ex13rotulado.insereA(1, 0, 16.0)
ex13rotulado.insereA(1, 2, 32.0)
ex13rotulado.insereA(2, 0, 64.0)
ex13rotulado.insereA(2, 1, 128.0)
ex13rotulado.show()
print('\nO grafo rotulado é completo? : ', ex13rotulado.isComplete()) #expected True

print('\nExercicio 13')

ex14 = GrafoMatriz(3)
ex14rotulado = GrafoMatriz(3, True)

ex14.insereA(0, 1)
ex14.insereA(0, 2)
ex14.insereA(1, 0)
ex14.insereA(2, 0)

print('\nGrafo original: ')
ex14.show()
print('\nGrafo complementar: ')

ex14.grafo_complementar().show()

ex14rotulado.insereA(0, 1, 4.0)
ex14rotulado.insereA(0, 2, 8.0)
ex14rotulado.insereA(1, 2, 32.0)
ex14rotulado.insereA(2, 1, 128.0)
print('\nGrafo rotulado original: ')
ex14rotulado.show()
print('\nGrafo rotualdo complementar: ')
ex14rotulado.grafo_complementar().show()