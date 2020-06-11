from functions.mutant import verificar

matrixOk = ['CCCCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']
matrixError = ['CCCCYA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']

# declaro dos matrices para verificar que el algoritmo de verificacion de patron funcione perfecto

def testPatternOk():
    assert verificar(matrixOk) == True

def testPatternError():
    assert verificar(matrixError) == False


