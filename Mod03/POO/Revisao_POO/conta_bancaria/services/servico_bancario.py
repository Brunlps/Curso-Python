from models.conta import ContaBancaria


def sacar(self, conta: ContaBancaria, saldo_retirado: float):
    if saldo_retirado <= 0:
        return False, "Valor inválido para saque"
        

    elif conta.saldo >= saldo_retirado:
        self.saldo -= saldo_retirado
        return True, conta.saldo

    else:
        return False, "Saldo insuficiente!"


        
def depositar(self, conta: ContaBancaria, saldo_deposito: float):
    if saldo_deposito <= 0:
        return False, "Valor inválido para depósito"

    conta.saldo += saldo_deposito
    print("Valor desitado com sucesso!")

def checar_saldo(self):
    print(f"Novo saldo: {self.saldo}")
    return