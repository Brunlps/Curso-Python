# Sistema de Gerenciamento de Hotel

Projeto desenvolvido como trabalho do curso de Python, no módulo de Programação Orientada a Objetos (POO).

## Objetivo

Criar um sistema simples de gerenciamento de hotel via terminal, onde é possível cadastrar clientes, visualizar quartos disponíveis, criar e modificar reservas.

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
- `dono_reserva` (objeto `Cliente`), `quarto_reservado` (objeto `Quarto`), `data_check_in`, `data_check_out`, `status_reserva`

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
0 - Sair
```

## O que já foi implementado

- [x] Classe `Cliente`
- [x] Classe `Quarto`
- [x] Classe `Reserva`
- [x] Cadastro de clientes com ID automático
- [x] Quartos pré-cadastrados ao iniciar o sistema
- [x] Verificação de quartos disponíveis
- [x] Criação de reserva (busca cliente, busca quarto, pede datas, salva reserva e marca quarto como ocupado)
- [x] Busca de reserva por ID do cliente (base para modificar e cancelar)
- [x] Menu interativo com `while` + `match`

## O que ainda falta

- [ ] Finalizar `modificar_reservas` — permitir alterar datas da reserva encontrada
- [ ] Implementar `cancelar_reservas` — cancelar reserva e liberar o quarto
- [ ] Implementar `get_clientes` — listar todos os clientes cadastrados
- [ ] Implementar `get_reserva` — listar todas as reservas ativas
- [ ] Conectar opções 4 e 5 do menu aos métodos correspondentes
- [ ] Adicionar `break` no `case "0"` para sair do programa
- [ ] Adicionar `__str__` nas classes para exibir informações de forma legível
