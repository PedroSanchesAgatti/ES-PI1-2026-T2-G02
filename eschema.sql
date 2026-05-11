CREATE TABLE eleitores (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
cpf VARCHAR(255) NOT NULL UNIQUE,
titulo CHAR(13) NOT NULL UNIQUE,
mesario BOOLEAN NOT NULL DEFAULT FALSE,
chave_acesso VARCHAR(255) NOT NULL,
status_voto BOOLEAN DEFAULT FALSE
);

CREATE TABLE candidatos (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
numero INT NOT NULL UNIQUE,
partido VARCHAR(50) NOT NULL
);

CREATE TABLE votos (
id INT AUTO_INCREMENT PRIMARY KEY,
id_eleitor INT NOT NULL,
id_candidato INT NULL,
data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
protocolo VARCHAR(255) NOT NULL UNIQUE,
UNIQUE (id_eleitor),
FOREIGN KEY (id_eleitor) REFERENCES eleitores(id) ON DELETE CASCADE,
FOREIGN KEY (id_candidato) REFERENCES candidatos(id) ON DELETE SET NULL
);

CREATE TABLE logs (
id INT AUTO_INCREMENT PRIMARY KEY,
data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
tipo VARCHAR(50) NOT NULL,
descricao TEXT NOT NULL
);

CREATE TABLE configuracao_votacao (
    id INT PRIMARY KEY,
    votacao_aberta BOOLEAN NOT NULL
);


INSERTS:
INSERT INTO configuracao_votacao VALUES (1, FALSE);

INSERT INTO eleitores (nome, cpf, titulo, mesario, chave_acesso, status_voto) VALUES
('Ana Souza', 'CPF001', '0000000000001', TRUE, 'CHAVE001', TRUE),
('Bruno Lima', 'CPF002', '0000000000002', FALSE, 'CHAVE002', TRUE),
('Carlos Mendes', 'CPF003', '0000000000003', FALSE, 'CHAVE003', FALSE),
('Daniela Rocha', 'CPF004', '0000000000004', TRUE, 'CHAVE004', TRUE),
('Eduardo Alves', 'CPF005', '0000000000005', FALSE, 'CHAVE005', TRUE),
('Fernanda Costa', 'CPF006', '0000000000006', FALSE, 'CHAVE006', FALSE),
('Gabriel Pinto', 'CPF007', '0000000000007', FALSE, 'CHAVE007', TRUE),
('Helena Martins', 'CPF008', '0000000000008', FALSE, 'CHAVE008', FALSE),
('Igor Ribeiro', 'CPF009', '0000000000009', TRUE, 'CHAVE009', TRUE),
('Juliana Freitas', 'CPF010', '0000000000010', FALSE, 'CHAVE010', TRUE),
('Lucas Gomes', 'CPF011', '0000000000011', FALSE, 'CHAVE011', FALSE),
('Mariana Dias', 'CPF012', '0000000000012', FALSE, 'CHAVE012', TRUE),
('Nicolas Barros', 'CPF013', '0000000000013', TRUE, 'CHAVE013', TRUE),
('Olivia Teixeira', 'CPF014', '0000000000014', FALSE, 'CHAVE014', FALSE),
('Paulo Henrique', 'CPF015', '0000000000015', FALSE, 'CHAVE015', TRUE),
('Queila Santos', 'CPF016', '0000000000016', FALSE, 'CHAVE016', FALSE),
('Rafael Nunes', 'CPF017', '0000000000017', FALSE, 'CHAVE017', TRUE),
('Sabrina Melo', 'CPF018', '0000000000018', TRUE, 'CHAVE018', TRUE),
('Tiago Cardoso', 'CPF019', '0000000000019', FALSE, 'CHAVE019', FALSE),
('Vanessa Duarte', 'CPF020', '0000000000020', FALSE, 'CHAVE020', TRUE);

INSERT INTO candidatos (nome, numero, partido) VALUES
('João Silva', 10, 'ABC'),
('Maria Oliveira', 11, 'DEF'),
('Pedro Santos', 12, 'GHI'),
('Carla Souza', 13, 'JKL'),
('Roberto Lima', 14, 'MNO'),
('Patricia Alves', 15, 'PQR'),
('Fernando Costa', 16, 'STU'),
('Luciana Rocha', 17, 'VWX'),
('Ricardo Mendes', 18, 'YZA'),
('Camila Ribeiro', 19, 'BCD'),
('André Gomes', 20, 'EFG'),
('Julio Martins', 21, 'HIJ'),
('Beatriz Freitas', 22, 'KLM'),
('Eduarda Dias', 23, 'NOP'),
('Vinicius Barros', 24, 'QRS'),
('Larissa Teixeira', 25, 'TUV'),
('Felipe Henrique', 26, 'WXY'),
('Renata Santos', 27, 'ZAB'),
('Gustavo Nunes', 28, 'CDE'),
('Aline Melo', 29, 'FGH');

INSERT INTO votos (id_eleitor, id_candidato, protocolo) VALUES
(1, 1, 'PROTO001'),
(2, 2, 'PROTO002'),
(3, NULL, 'PROTO003'),
(4, 4, 'PROTO004'),
(5, 5, 'PROTO005'),
(6, NULL, 'PROTO006'),
(7, 7, 'PROTO007'),
(8, 8, 'PROTO008'),
(9, 9, 'PROTO009'),
(10, 10, 'PROTO010'),
(11, NULL, 'PROTO011'),
(12, 12, 'PROTO012'),
(13, 13, 'PROTO013'),
(14, NULL, 'PROTO014'),
(15, 15, 'PROTO015'),
(16, 16, 'PROTO016'),
(17, 17, 'PROTO017'),
(18, 18, 'PROTO018'),
(19, NULL, 'PROTO019'),
(20, 20, 'PROTO020');

INSERT INTO logs (tipo, descricao) VALUES
('ABERTURA', 'Votação iniciada com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de acesso negado'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de voto duplo'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de acesso negado'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de voto duplo'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de acesso negado'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de voto duplo'),
('SUCESSO', 'Voto realizado com sucesso'),
('SUCESSO', 'Voto realizado com sucesso'),
('ALERTA', 'Tentativa de acesso negado'),
('ENCERRAMENTO', 'Votação finalizada com sucesso');
