import math

class Calculadora:
    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Não é possível fazer divisão por zero!")
        return a / b
    
    def potencia(self, a, b):
        return a ** b
    
    def fatorial(self, a):
        if a < 0:
            raise ValueError("Não é possível calcular o fatorial de números negativos!")
        if not isinstance(a, int):
            raise ValueError("Fatorial é definido apenas para números inteiros!")
        return math.factorial(a)
    
    def raiz_quadrada(self, a):
        if a < 0:
            raise ValueError("Não é possível calcular raiz quadrada de números negativos!")
        return math.sqrt(a)
