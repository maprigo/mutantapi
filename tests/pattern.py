from functions.mutant import verificar

matrixOk = ['CCCCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']
matrixError = ['CCCCYA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']


def testPatternOk():
    assert verificar(matrixOk) == True

def testPatternError():
    assert verificar(matrixError) == False


