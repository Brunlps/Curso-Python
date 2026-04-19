"""
    Faça uma classe para representar uma conta bancária
    com os atributos: titula, numero, agencia, saldo, senha
    e os métodos:
    sacar()
    depositar()
    checar_saldo()
    """


class Conta_Bancaria:
    def __init__(self, titular, numero, agencia, saldo, senha):
        self.__titular = titular
        self.__numero = numero
        self.__agencia = agencia
        self.__saldo = saldo
        self.__senha = senha

    def set_sacar_saldo(self, sacar_novo_saldo) -> None:
        self.sacar_novo_saldo -= self.__saldo

    def set_depositar_saldo(self, depositar_novo_saldo) -> None:
        self.depositar_novo_saldo += self.__saldo
    
    def get_chacar_saldo(self) -> None:
        print(f"Nome: {self.__titular} \nSaldo:{self.__saldo}")
