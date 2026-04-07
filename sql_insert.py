import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco'
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
    
    print("Eleitor inserido com ID:", cursor.lastrowid)


def listar_eleitores():
    cursor.execute("SELECT id, nome, cpf, titulo, status_voto FROM eleitores")
    
    for (id, nome, cpf, titulo, status) in cursor.fetchall():
        print(f"ID: {id} | Nome: {nome} | CPF: {cpf} | Titulo: {titulo} | Votou: {status}")


def inserir_candidato(nome, numero, partido):
    sql = "INSERT INTO candidatos (nome, numero, partido) VALUES (%s, %s, %s)"
    
    valores = (nome, numero, partido)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("Candidato inserido com ID:", cursor.lastrowid)


def listar_candidatos():
    cursor.execute("SELECT id, nome, numero, partido FROM candidatos")
    
    for (id, nome, numero, partido) in cursor.fetchall():
        print(f"ID: {id} | Nome: {nome} | Numero: {numero} | Partido: {partido}")


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


listar_eleitores()
listar_candidatos()


cursor.close()
conexao.close()