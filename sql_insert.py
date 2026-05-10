import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@@PHSAg3474',
    database='PIteste'
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
    WHERE nome LIKE %s OR cpf = %s
    """
    
    cursor.execute(sql, (f"%{valor}%", valor))
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
    WHERE cpf = %s or titulo = %s
    """
    cursor.execute(sql, (valor, valor))
    conexao.commit()

    print("\nEleitor deletado com sucesso!")


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
