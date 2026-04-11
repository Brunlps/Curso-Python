from models.conta import ContaBancaria
from services.servico_bancario import sacar, depositar, checar_saldo


usuario = ContaBancaria("Bruna", 2.203)

opcao = int(input(f"""-=-=-=-=-=-=- Menu {usuario.titular} =-=-=-=-=-=-==-=
                  1 - sacar 
                  2 - depositar
                  3 - checar o saldo
                  Escolha uma opção:  """))
match opcao:
    case 1: 
        saldo_retirado = input("Digite o valor do saque: ")
        usuario.sacar(saldo_retirado)
        print(f"Saque de {saldo_retirado} retirado.\n Novo saldo: {conta.saldo}")


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