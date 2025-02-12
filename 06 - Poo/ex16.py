class ContaBancaria:
    def __init__(self, saldo: float) -> None:
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar (self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo Insuficiente!')

    def exibir_saldo(self):
        print(f'R${self.saldo:.2f}')

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo: float, juros: float) -> None:
        super().__init__(saldo)
        self.juros = juros

    def aplicar_juros(self):
        self.saldo += (self.saldo*(self.juros/100))
    
corrente = ContaBancaria(300)
poupanca = ContaPoupanca(300, 2)
    

corrente.exibir_saldo()
poupanca.exibir_saldo()
print()

corrente.depositar(30)
poupanca.depositar(30)

poupanca.aplicar_juros()

corrente.exibir_saldo()
poupanca.exibir_saldo()

