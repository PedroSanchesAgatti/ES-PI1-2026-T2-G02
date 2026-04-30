import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Seppal1914#',
    database='sistema_votacao'
)

cursor = conexao.cursor()


def inserir_eleitor(nome, cpf, titulo, mesario, chave_acesso):
    try:
        sql = """
        INSERT INTO eleitores 
        (nome, cpf, titulo, mesario, chave_acesso) 
        VALUES (%s, %s, %s, %s, %s)
        """
        valores = (nome, cpf, titulo, mesario, chave_acesso)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Eleitor cadastrado com sucesso!")
    except mysql.connector.Error as erro:
        print("Erro ao inserir eleitor:", erro)


def buscar_eleitor(valor):
    sql = """
    SELECT id, nome, cpf, titulo, status_voto 
    FROM eleitores
    WHERE cpf = %s OR titulo = %s
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


def remover_eleitor(id):
    try:
        sql = "DELETE FROM eleitores WHERE id = %s"
        cursor.execute(sql, (id,))
        conexao.commit()
        print("Eleitor removido com sucesso!")
    except mysql.connector.Error as erro:
        print("Erro ao remover:", erro)


def editar_eleitor(id, nome, cpf, titulo, mesario):
    try:
        sql = """
        UPDATE eleitores
        SET nome = %s, cpf = %s, titulo = %s, mesario = %s
        WHERE id = %s
        """
        valores = (nome, cpf, titulo, mesario, id)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Eleitor atualizado com sucesso!")
    except mysql.connector.Error as erro:
        print("Erro ao atualizar:", erro)


def verificar_titulo_eleitor(titulo):
    sql = "SELECT COUNT(*) FROM eleitores WHERE titulo = %s"
    cursor.execute(sql, (titulo,))
    resultado = cursor.fetchone()[0]
    return resultado > 0



def inserir_candidato(nome, numero, partido):
    try:
        sql = "INSERT INTO candidatos (nome, numero, partido) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, numero, partido))
        conexao.commit()
        print("Candidato cadastrado com sucesso!")
    except mysql.connector.Error as erro:
        print("Erro:", erro)


def listar_candidatos():
    cursor.execute("SELECT id, nome, numero, partido FROM candidatos")
    
    for (id, nome, numero, partido) in cursor.fetchall():
        print(f"ID: {id} | Nome: {nome} | Numero: {numero} | Partido: {partido}")

def buscar_candidato(valor):
    sql = """
    SELECT id, nome, numero, partido 
    FROM candidatos
    WHERE nome LIKE %s OR numero = %s
    """
    
    cursor.execute(sql, (f"%{valor}%", valor))
    resultado = cursor.fetchall()

    if resultado:
        for id, nome, numero, partido in resultado:
            print(f"ID: {id} | Nome: {nome} | Número: {numero} | Partido: {partido}")
    else:
        print("Nenhum candidato encontrado.")

def editar_candidato(id, nome, numero, partido):
    try:
        sql = """
        UPDATE candidatos
        SET nome = %s, numero = %s, partido = %s
        WHERE id = %s
        """
        
        cursor.execute(sql, (nome, numero, partido, id))
        conexao.commit()
        print("Candidato atualizado com sucesso!")
    except mysql.connector.Error as erro:
        print("Erro ao atualizar:", erro)

def remover_candidato(id):
    try:
        sql = "DELETE FROM candidatos WHERE id = %s"
        cursor.execute(sql, (id,))
        conexao.commit()
        print("Candidato removido com sucesso!")
    except mysql.connector.Error as erro:
        print("Erro ao remover:", erro)


def registrar_voto(id_eleitor, id_candidato, protocolo):
    try:
        sql = """
        INSERT INTO votos (id_eleitor, id_candidato, protocolo)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (id_eleitor, id_candidato, protocolo))

        cursor.execute("""
            UPDATE eleitores 
            SET status_voto = TRUE 
            WHERE id = %s
        """, (id_eleitor,))

        conexao.commit()
        print("Voto registrado!")
    except mysql.connector.Error as erro:
        print("Erro ao votar:", erro)


def listar_votos():
    cursor.execute("""
    SELECT e.nome, c.nome, v.data_hora
    FROM votos v
    LEFT JOIN eleitores e ON v.id_eleitor = e.id
    LEFT JOIN candidatos c ON v.id_candidato = c.id
    """)
    
    for eleitor, candidato, data in cursor.fetchall():
        print(f"Eleitor: {eleitor} | Candidato: {candidato} | Data: {data}")


def verificar_cpf_existente(cpf):
    sql = "SELECT COUNT(*) FROM eleitores WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    return cursor.fetchone()[0] > 0

def fechar_conexao():
    cursor.close()
    conexao.close()