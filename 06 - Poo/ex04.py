class ContaBancaria:
    def __init__(self) -> None:
        self.__saldo:float = 0


    def depositar(self, valor):
        self.__saldo+=valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente!')

    def exibir_saldo(self):
        print(self.__saldo)



conta = ContaBancaria()


conta.depositar(100)
conta.sacar(30)
conta.exibir_saldo()