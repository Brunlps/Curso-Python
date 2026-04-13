from exercicio_tv import Televisao


def exibir_menu():
    print("\n===== CONTROLE DA TV =====")
    print("1 - Canal acima")
    print("2 - Canal abaixo")
    print("3 - Voltar ao canal anterior")
    print("0 - Sair")
    print("==========================")


def main():
    tv = Televisao(1, 99)
    print(f"TV ligada! {tv}")

    while True:
        exibir_menu()
        option = input("Escolha: ").strip()

        match option:

            case 1:
                tv. mudar_canal_baixo()
            case 2:
                tv. mudar_canal_cima()
            case 3:
                tv.voltar_canal()
            case 4:
                tv.status()
            case 0:
                print("Encerrando...")
                break

            case _:
                print("Entrada inválida!")


if __name__ == "__main__":
    main()
