# Herança e Metodos Privados


class ContaBancaria(object):
    def __init__(self, *args, **kwargs):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        self.consultar_saldo()

    def sacar(self, valor):
        self.saldo -= valor
        self.consultar_saldo()

    def consultar_saldo(self):
        print(self.saldo)


class ContaPoupanca(ContaBancaria):
    def _consulta_rentabilidade(self):  # Este e um metodo privado!
        return 1.6

    def rentabilidade(self):
        rentabilidade = self._consulta_rentabilidade()

        if rentabilidade < 0.5:
            print("Consulte o seu Gerente")

        else:
            print(rentabilidade)


conta_poupanca = ContaPoupanca()
conta_poupanca.rentabilidade()
conta_poupanca.depositar(100)
conta_poupanca.sacar(100)