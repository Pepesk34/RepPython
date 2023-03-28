from parimpar import ParImpar

def test_add():
    objeto = ParImpar([])
    assert len(objeto.numeros) == 0
    objeto.add(2)
    assert len(objeto.numeros) == 1

def test_sumarpares():
    objeto = ParImpar([])
    objeto.numeros.clear()
    assert len(objeto.numeros) == 0
    objeto.add(1)
    objeto.add(2)
    objeto.add(3)
    assert len(objeto.numeros) == 3
    assert objeto.sumarpares() == 2

def test_sumarImpares():
    objeto = ParImpar([])
    objeto.numeros.clear()
    assert len(objeto.numeros) == 0
    objeto.add(1)
    objeto.add(2)
    objeto.add(3)
    assert len(objeto.numeros) == 3
    assert objeto.sumarImpares() == 4

def test_cuadradoLista():
    objeto = ParImpar([])
    objeto.numeros.clear()
    objeto.add(1)
    objeto.add(2)
    objeto.add(3)
    assert len(objeto.numeros) == 3
    assert objeto.cuadradoLista() == [1, 4, 9]

