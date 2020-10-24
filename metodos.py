# Metodos e Construtores

'''
classe 
objetos
construtor
metodos
    Quando uma classe tem uma funçao, esta e chamada de metodo.
atributos
herança
sobrecarga
poliformismo
destrutores
herança
'''

'''
Quando vc desenha a planta de uma casa isso nao quer dizer que ela existe 
Isso e uma classe.
'''
#Toda classe do Python vai herdar no minimo de Object.
# O objecto e a concretizaçao de uma classe. 
# Vou criar realmente na memoria no pc uma "pessoal" oriunda da classe.
#Atributos de uma classe sao os 'adjetivos desta. No caso de uma Classe pessoa
#   temos como possiveis atributos, nome, idade, sexo.

class Casa(object):
    cor = "Amarela"
    altura = 3
    quartos = 10

    def pintar(self, cor):
        self.cor = cor

#Vou criar um objeto.
minha_casa = Casa()     #Agora a classe foi instanciada. Ela passou a existir.
print(minha_casa.cor, str(minha_casa.altura))

print(minha_casa.pintar('branco'))

print('oi')