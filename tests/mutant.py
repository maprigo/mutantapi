from functions.mutant import *

matrix = ['CCCCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']


# Con la matrix definida arriba tendrian que dar resultados positivos en horizontal vertical y isMutant

def testHorizontal():
    assert horizontal(matrix) > 0


def testVertical():
    assert vertical(matrix) > 0


def testDiagonal():
    assert diagonal(matrix) == 0


def testDiagonalOne():
    assert diagOne(matrix) == 0


def testIsMutant():
    assert isMutant(matrix) == True
