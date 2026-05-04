class Cliente:
    def __init__(self, id_cliente, nome, telefone, email):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.email = email



class Quarto:
    def __init__(self, numero_quarto, tipo_quarto, preco_diaria, status):
        self.numero_quarto = numero_quarto
        self.tipo_quarto = tipo_quarto
        self.preco_diaria = preco_diaria
        self.status = status



class Reserva:
    def __init__(self, dono_reseva, quarto_resevado, data_chek_in, data_chek_out, status_reserva):
        self.dono_reserva = dono_reseva
        self.quarto_resevado = quarto_resevado
        self.data_chek_in = data_chek_in
        self.data_chek_out = data_chek_out
        self.status_reserva = status_reserva


class GerenciadorDeReserva(Cliente, Quarto, Reserva):
    def __init__(self, nome, cnpj, endereco, telefone):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.id_atual = 1
        self.lista_clientes = []
        self.lista_quartos = []
        self.historico_reservas = []

    def quartos(self, numero_quarto, tipo_quarto, preco_diaria, status):
        novo_quarto = Quarto(numero_quarto, tipo_quarto, preco_diaria, status="Disponível")

        self.lista_quartos.append(novo_quarto)

    def cadastro_clientes(self):
        print("-=-=-=-=-=-=-=Clientes=-=-==-=-=-=-=-")
        self.nome = input("Nome: ")
        self.email = input("E-mail: ")
        self.telefone = input("Telefone: ")

        novo_cliente = Cliente(id_cliente= self.id_atual, 
                               nome= self.nome, 
                               telefone= self.telefone, 
                               email=self.email)

        self.lista_clientes.append(novo_cliente)

        self.id_atual += 1

        return novo_cliente

    def verificar_disponibilidade_quartos(self):

        for quartos in self.lista_quartos:
            if quartos.status == "Disponível":
                print(f"Quartos disponíveis: {quartos}")

    def criar_reservas(self):
        # Buscando clientes
        id_buscador = int(input("ID do cliente: "))

        cliente_encotrado = None

        for cliente in self.lista_clientes:
            if cliente.id_cliente == id_buscador:
                cliente_encotrado = cliente

        if cliente_encotrado is None:
            print("Cliente não encontrado.")
            return
        
        # Buscando quartos
        numero_buscador = input("Número do quarto: ")

        quarto_encotrado = None

        for quarto in self.lista_quartos:
            if quarto.numero_quarto == numero_buscador:
                if quarto.status == "Disponível":
                    quarto_encotrado = quarto

        if quarto_encotrado is None:
            print("Quarto não encontrado.")
            return
        
        # Add datas
        data_check_in = input("Data de check-in (dd/mm/aaaa): ")
        data_check_out = input("Data de check-out (dd/mm/aaaa): ")

        # Criando Reserva
        nova_reserva = Reserva(
            dono_reseva=cliente_encotrado,
            quarto_resevado=quarto_encotrado,
            data_chek_in=data_check_in,
            data_chek_out=data_check_out,
            status_reserva="Ativa")
        
        self.historico_reservas.append(nova_reserva)

        quarto_encotrado.status = "Ocupado"

        print("Reserva criada com sucesso!")

    def modificar_reservas(self):
        id_buscador = int(input("ID do cliente: "))

        reserva_encotrado = None

        for reserva in self.historico_reservas:
            if reserva.dono_reserva.id_cliente == id_buscador:
                reserva_encotrado = reserva

        if reserva_encotrado is None:
            print("Reserva não encontrado.")
            return

    def cancelar_reservas(self):
        ...

    def get_reserva(self):
        ...

    def get_clientes(self):
        ...




# print(client = Reserva.cadastro_clientes)

# Hotel e quartos
hotel = GerenciadorDeReserva(nome="Hotel", cnpj="000.000.000/0001-00", endereco="Rua A, 123", telefone="1203-4556")
hotel.quartos("101", "Single", 200, "Disponível")
hotel.quartos("102", "Double", 350, "Disponível")
hotel.quartos("103", "Suite", 600, "Disponível")


while True:

    opcao = input("""
        1 - cadastrar
        2 - Verificar disponibilidade de quartos
        3 - Criar reserva
        4 - Modificar reservar
        5 - Cancelar Reserva
        0 - Sair
                    """)
    
    match opcao:

        case "1":

            hotel.cadastro_clientes()
            print(hotel.lista_clientes)

        case "2":

            hotel.verificar_disponibilidade_quartos()

        case "3":
            hotel.criar_reservas()

        case "4":
            ...
        case "5":
            ...
        case "0":
            ...
