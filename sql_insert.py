import mysql.connector
import datetime
import os

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Seppal1914#',
    database='sistema_votacao'
)

cursor = conexao.cursor()

def inserir_eleitor(nome, cpf, titulo, mesario, chave_acesso):
    sql = """
    INSERT INTO eleitores 
    (nome, cpf, titulo, mesario, chave_acesso) 
    VALUES (%s, %s, %s, %s, %s)
    """
    
    valores = (nome, cpf, titulo, mesario, chave_acesso)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("Eleitor cadastrado com sucesso!")

def buscar_eleitor(valor):
    sql = """
    SELECT id, nome, cpf, titulo, status_voto 
    FROM eleitores
    WHERE titulo = %s OR cpf = %s
    """
    
    cursor.execute(sql, (valor, valor))
    resultado = cursor.fetchall()

    if resultado:
        for id, nome, cpf, titulo, status in resultado:
            print(f"ID: {id} | Nome: {nome} | CPF: {cpf} | Titulo: {titulo} | Votou: {status}")
    else:
        print("Nenhum eleitor encontrado.")

def listar_eleitores():
    cursor.execute("SELECT id, nome, cpf, titulo, status_voto FROM eleitores")
    
    for (id, nome, cpf, titulo, status) in cursor.fetchall():
        print(f"ID: {id} | Nome: {nome} | CPF: {cpf} | Titulo: {titulo} | Votou: {status}")


def inserir_candidato(nome, numero, partido):
    sql = "INSERT INTO candidatos (nome, numero, partido) VALUES (%s, %s, %s)"
    
    valores = (nome, numero, partido)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("Candidato cadastrado com sucesso!")


def listar_candidatos():
    cursor.execute("SELECT id, nome, numero, partido FROM candidatos")
    
    for (id, nome, numero, partido) in cursor.fetchall():
        print(f"ID: {id} | Nome: {nome} | Numero: {numero} | Partido: {partido}")


def excluir_eleitor(valor):
    sql = """
    DELETE FROM eleitores
    WHERE cpf = %s OR titulo = %s
    """

    cursor.execute(sql, (valor, valor))

    if cursor.rowcount > 0:
        conexao.commit()
        print("\nEleitor deletado com sucesso!")
    else:
        print("\nNenhum eleitor encontrado.")


def registrar_voto(id_eleitor, id_candidato, protocolo):
    sql = """
    INSERT INTO votos (id_eleitor, id_candidato, protocolo)
    VALUES (%s, %s, %s)
    """

    valores = (id_eleitor, id_candidato, protocolo)
    cursor.execute(sql, valores)

    cursor.execute("""
        UPDATE eleitores
        SET status_voto = TRUE
        WHERE id = %s
    """, (id_eleitor,))

    conexao.commit()

    registrar_log("SUCESSO: Voto realizado com sucesso.")

    print("Voto registrado!")


def listar_votos():
    cursor.execute("""
    SELECT e.nome, c.nome, v.data_hora
    FROM votos v
    LEFT JOIN eleitores e ON v.id_eleitor = e.id
    LEFT JOIN candidatos c ON v.id_candidato = c.id
    """)
    
    for eleitor, candidato, data in cursor.fetchall():
        print(f"Eleitor: {eleitor} | Candidato: {candidato} | Data: {data}")

def verificar_titulo_eleitor(titulo):
    sql = """
    SELECT COUNT(*) FROM eleitores
    WHERE titulo = %s
    """
    cursor.execute(sql, (titulo,))
    resultado = cursor.fetchone()[0]
    return resultado > 0

def fechar_conexao():
    cursor.close()
    conexao.close()

def abrir_votacao():
    cursor.execute("UPDATE configuracao_votacao SET votacao_aberta = TRUE WHERE id = 1")
    conexao.commit()

    registrar_log("ABERTURA: Votação iniciada com sucesso. Total de votos zerado.")

    print("Votação aberta!")

def encerrar_votacao():
    cursor.execute("UPDATE configuracao_votacao SET votacao_aberta = FALSE WHERE id = 1")
    conexao.commit()

    registrar_log("ENCERRAMENTO: Votação finalizada com sucesso.")

    print("Votação encerrada!")

def votacao_esta_aberta():
    cursor.execute("SELECT votacao_aberta FROM configuracao_votacao WHERE id = 1")
    return cursor.fetchone()[0]


def verificao_mesarrio(cpf, chave):
    sql = """
    SELECT cpf, chave_acesso, mesario
    FROM eleitores
    WHERE chave_acesso = %s
    """

    cursor.execute(sql, (chave,))
    resultado = cursor.fetchone()

    if resultado is None:
        return False

    cpf_db, chave_db, mesario = resultado

    return cpf_db[:3] == cpf[:3] and chave_db == chave and mesario==1

def verificao_votacao(cpf, chave):
    sql = """
    SELECT cpf, chave_acesso, status_voto
    FROM eleitores
    WHERE chave_acesso = %s
    """

    cursor.execute(sql, (chave,))
    resultado = cursor.fetchone()

    if resultado is None:
        return False

    cpf_db, chave_db, status = resultado

    return cpf_db[:3] == cpf[:3] and chave_db == chave and status==0

def registrar_log(mensagem):
    data_hora = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    with open("logs_ocorrencias.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{data_hora} {mensagem}\n")
def exibir_logs():
    if not os.path.exists("logs_ocorrencias.txt"):
        print("Nenhum log encontrado.")
        return

    print("\n================ LOGS DE OCORRÊNCIAS ================\n")

    with open("logs_ocorrencias.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
def exibir_protocolos():
    cursor.execute("""
        SELECT protocolo
        FROM votos
        ORDER BY protocolo ASC
    """)

    resultados = cursor.fetchall()

    print("\n================ PROTOCOLOS DE VOTAÇÃO ================\n")

    if resultados:
        for protocolo in resultados:
            print(protocolo[0])
    else:
        print("Nenhum protocolo encontrado.")

exibir_protocolos()