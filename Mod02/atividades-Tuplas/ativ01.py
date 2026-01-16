# 🧠 Exercício 1 — Dados fixos do sistema

# Crie uma tupla chamada config com:

    # ("EndFinance", "1.0", "produção")

# Depois:
    # mostre o nome do sistema
    # mostre a versão
    # mostre o ambiente
    
config = ('EndFinance', '1.0', 'produção')
print(f"""
    Nome do Sistema: {config[0]}
    Versão: {config[1]}
    Ambiente: {config[2]}""")
