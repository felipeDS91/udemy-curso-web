# To use debug
# import pdb;pdb.set_trace()

class ContaBancaria(object):
    # Constructor class "__init__"
    def __init__(self):
        self.saldo = 0
        self.conexao = 'http://meusite.com.br:3306'

    def depositar(self, valor):
        self.saldo += valor
        self.consulta_saldo()

    def sacar(self, valor):
        self.saldo -= valor
        self.consulta_saldo()

    def consulta_saldo(self):
        print(self.saldo)

    # Destructor class "__del__"
    def __del__(self):
        print('Fechando conexao com o banco de dados em seguranca')
        self.conexao = None



class ContaPoupanca(ContaBancaria):
    rentabilidade_total = 1.6

    # Methods that has a "_" on start are "private methods" of class
    def _consulta_rentabilidade(self):
        return self.rentabilidade_total

    def rentabilidade(self):
        rentabilidade = self._consulta_rentabilidade()

        if rentabilidade < 0.5:
            print('Consulte seu gerente')
        else:
            print(rentabilidade)

    def depositar(self, valor):
        self.saldo += valor

        if self.saldo >= 1000:
            self.rentabilidade_total += 0.1
            print('Parabens, sua rentabilidade aumentou para: ')
            self.rentabilidade()


class ContaCorrente(ContaBancaria):
    # Rewriting a father method (override)
    def depositar(self, valor):
        if valor < 100:
            raise Exception('Valor minimo e 100')
        else:
            # Reuses the original method of your inheritance class (super)
            super(ContaCorrente, self).depositar(valor)


conta_poupanca = ContaPoupanca()
#conta_poupanca.rentabilidade()
#conta_poupanca.depositar(2000)
#conta_poupanca.sacar(50)

conta_corrente = ContaCorrente()
conta_corrente.depositar(100)

    