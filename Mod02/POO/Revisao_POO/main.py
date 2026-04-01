# FAÇA UMA CLASSE PARA REPRESENTAR UMA CONTA BANCÁRIA
# COM OS ATRIBUTOS: TITULAR, NUMERO, AGENCIA, SALDO
# E OS MÉTODOS: SACAR ( ), DEPOSITAR( ), CHECARSALDO( )
class Conta_bancaria:
    def __init__(self, titular, numero, agencia, saldo):
        self.titular = "Bruna"
        self.numero = 122365
        self.agencia = 2013
        self.saldo = 1.000
        self.saldo_retirado = float(self.saldo_retirado)
        self.valor_deposito = float(self.valor_deposito)


    def sacar(self, saldo_retirado):
        if saldo_retirado <= 0:
            print("Valor inválido")
            return

        if saldo_retirado > self.saldo:
            print("Saldo insuficiente!")
            return
    
        self.saldo -= saldo_retirado
        print("Saldo insuficiente!")


        
    def depositar(self):
        if self.saldo and self.valor_deposito != 0 and self.valor_deposito > 0:
            self.saldo += self.valor_deposito
            print("Valor desitado com sucesso!")
        else:
            print("Valor insuficiente!")
    def checar_saldo(self):
        print(f"Novo saldo: {self.saldo}")


usuario = Conta_bancaria

opcao = int(input("Digite 1 para sacar\n 2 para depositar\n3 para checar o saldo: "))
match opcao:
    case 1: 
        saldo_retirado = input("Digite o valor do saque: ")
        usuario.sacar(saldo_retirado)
        print("Valor sacado com sucesso!")

        try:
            usuario.sacar(float(saldo_retirado))

        except ValueError:
            print("Valor inválido!")
    case 2:
        usuario.depositar()
        valor_deposito = input("Digite o valor do deposito:")
    case 3:
        usuario.checar_saldo()
    case _:
        print("Operação inválida!")