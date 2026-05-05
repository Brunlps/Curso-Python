# Sistema de Gerenciamento de Hotel

Projeto desenvolvido como trabalho do curso de Python, no módulo de Programação Orientada a Objetos (POO).

## Objetivo

Criar um sistema simples de gerenciamento de hotel via terminal, onde é possível cadastrar clientes, visualizar quartos disponíveis, criar, modificar e cancelar reservas.

## Estrutura do projeto

O projeto é composto por um único arquivo `main.py` com as seguintes classes:

### `Cliente`
Representa um hóspede do hotel.
- `id_cliente`, `nome`, `telefone`, `email`

### `Quarto`
Representa um quarto do hotel.
- `numero_quarto`, `tipo_quarto`, `preco_diaria`, `status` (`"Disponível"` ou `"Ocupado"`)

### `Reserva`
Representa uma reserva feita por um cliente.
- `dono_reserva` (objeto `Cliente`), `quarto_resevado` (objeto `Quarto`), `data_check_in`, `data_check_out`, `status_reserva`

### `GerenciadorDeReserva`
Classe principal que gerencia clientes, quartos e reservas do hotel.
- Mantém listas de clientes, quartos e histórico de reservas
- Contém todos os métodos de operação do sistema

## Como executar

```bash
python main.py
```

O programa inicia com 3 quartos pré-cadastrados (101, 102, 103) e abre um menu interativo no terminal.

## Menu de opções

```
1 - Cadastrar cliente
2 - Verificar disponibilidade de quartos
3 - Criar reserva
4 - Modificar reserva
5 - Cancelar reserva
6 - Listar reservas
7 - Listar clientes
8 - Listar quartos
0 - Sair
```

## Funcionalidades implementadas

- [x] Classe `Cliente` com `__str__`
- [x] Classe `Quarto` com `__str__`
- [x] Classe `Reserva` com `__str__`
- [x] Cadastro de clientes com ID automático
- [x] Quartos pré-cadastrados ao iniciar o sistema (101, 102, 103)
- [x] Verificação de quartos disponíveis
- [x] Criação de reserva — busca cliente e quarto, pede datas, salva e marca quarto como ocupado
- [x] Modificação de reserva — altera datas por ID do cliente
- [x] Cancelamento de reserva — cancela e libera o quarto automaticamente
- [x] Listagem de clientes cadastrados
- [x] Listagem de reservas do histórico
- [x] Listagem de quartos
- [x] Menu interativo com `while` + `match` + `break` para sair
