-- Criar banco de dados
CREATE DATABASE IF NOT EXISTS endfinance;
USE endfinance;

-- Tabela de bancos
CREATE TABLE IF NOT EXISTS bancos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Tabela de formas de pagamento
CREATE TABLE IF NOT EXISTS pagamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Tabela de entradas
CREATE TABLE IF NOT EXISTS entradas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255),
    valor DECIMAL(10,2) NOT NULL,
    banco_id INT,
    pagamento_id INT,
    data DATE NOT NULL,
    FOREIGN KEY (banco_id) REFERENCES bancos(id),
    FOREIGN KEY (pagamento_id) REFERENCES pagamentos(id)
);

-- Tabela de saídas
CREATE TABLE IF NOT EXISTS saidas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255),
    valor DECIMAL(10,2) NOT NULL,
    banco_id INT,
    pagamento_id INT,
    data DATE NOT NULL,
    FOREIGN KEY (banco_id) REFERENCES bancos(id),
    FOREIGN KEY (pagamento_id) REFERENCES pagamentos(id)
);
