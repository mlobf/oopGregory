# Metodos e Construtores

"""
classe 
objetos
construtor
    E o init, este quando ja implementado, ja cria uma um objeto
    com as suas respectivas propriedades.
metodos
    Quando uma classe tem uma funçao, esta e chamada de metodo.
atributos
herança
sobrecarga
poliformismo
destrutores
herança
"""

"""
Quando vc desenha a planta de uma casa isso nao quer dizer que ela existe 
Isso e uma classe.
"""
# Toda classe do Python vai herdar no minimo de Object.
# O objecto e a concretizaçao de uma classe.
# Vou criar realmente na memoria no pc uma "pessoal" oriunda da classe.
# Atributos de uma classe sao os 'adjetivos desta. No caso de uma Classe pessoa
#   temos como possiveis atributos, nome, idade, sexo.
class Casa(object):
    cor = "Amarela"
    altura = 3
    quartos = 10

    def __init__(self, cor, altura, quartos):
        self.cor = cor
        self.altura = altura
        self.quartos = quartos

    def pintar(self, cor):
        self.cor = cor

    def aumentar_quartos(self, quartos):
        self.quartos = quartos

    def imprime_casa(self):
        print(self.cor, self.altura, self.quartos)


minha_casa = Casa("red", 3, 5)

minha_casa.imprime_casa()
