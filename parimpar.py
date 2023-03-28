class ParImpar:
    numeros=[]

    def __init__(self, lista):
        self.numeros = lista

    def add(self, n):
        self.numeros.append(n)

    def sumarpares(self):
        suma = 0
        for i in self.numeros:
            if (i%2) == 0:
                suma+=i
        return suma
        
    def cuadradoLista(self):
        cuadrados=[]
        for i in self.numeros:
            cuadrados.append(i*i)
        return cuadrados
    
    def sumarImpares(self):
        suma=0
        for i in self.numeros:
            if i%2 != 0:
                suma+=i
        return suma

