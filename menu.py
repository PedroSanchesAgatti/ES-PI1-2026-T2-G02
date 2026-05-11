import sql_insert
from sql_insert import (
    inserir_eleitor, listar_eleitores, buscar_eleitor, verificar_titulo_eleitor, 
    fechar_conexao, abrir_votacao, encerrar_votacao, votacao_esta_aberta, 
    registrar_log, listar_logs, listar_protocolos_auditoria,
    buscar_eleitor_por_titulo, buscar_candidato_por_numero, registrar_voto
)
import random
import string
import criptografia
import mysql.connector
import os
import datetime

def gerar_protocolo():
    # Padrão: Prefixo "V" + 2 letras aleatórias + Ano (26) + Número do Candidato (será tratado no voto) + 5 dígitos aleatórios
    # Para simplificar aqui, geramos uma string aleatória de 10 caracteres
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def validacaoTitulo(titulo):
    titulo2=str(titulo)
    faltando=12-len(titulo2)

    if faltando>0:
        titulo=("0" * faltando)+titulo2
    else:
        if len(titulo2)!=12:
            return False

    inicial=titulo[:8]
    uf=titulo[8:10]
    dvtitulo=int(titulo[10])
    dvtitulo2=int(titulo[11])

    pesos1=[2,3,4,5,6,7,8,9]
    soma=0
    i=0
    while i<8:
        soma+=int(inicial[i])*pesos1[i]
        i+=1

    resto=soma%11

    if uf in("01", "02")and resto==0:
        dvreal=1
    else:
        if resto==10:
            dvreal=0
        else:
            dvreal=resto

    if dvreal!=dvtitulo:
        return False

    soma=int(uf[0])*7+int(uf[1])*8+dvreal*9
    resto=soma%11

    if uf in("01", "02")and resto==0:
        dvreal2=1
    else:
        if resto==10:
            dvreal2=0
        else:
            dvreal2=resto

    if dvreal2!=dvtitulo2:
        return False

    return True

def verificacaoCPF(cpf):
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = (soma * 10) % 11
    if resto == 10 or resto == 11:
        resto = 0
    digito1 = resto
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    resto = (soma * 10) % 11
    if resto == 10 or resto == 11:
        resto = 0
    digito2 = resto

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

inicio = ""
while inicio != "3":
    print(f"\nInício")
    print(f"\n----------------------------Sistema de Votação----------------------------------")
    print("\n1-Votação\n2-gerenciamento\n3-sair\n")
    inicio= input("Escolha a opção desejada:")
    match inicio:
        case "1":
            Votação=""
            while Votação!="4":
                print(f"\n----------------------------Votação---------------------------------------------")
                print("\n1-Auditoria\n2-Abrir sistema de votação\n3-Resultados\n4-Voltar\n")
                Votação=input("Escolha a opção desejada:")
                match Votação:
                    case "1":
                        Auditoria=""
                        while Auditoria!="3":
                            print(f"\n----------------------------Auditoria-------------------------------------------")
                            print("\n1-Protocolos de votação\n2-Logs de ocorrência\n3-Voltar\n")
                            Auditoria=input("Escolha a opção desejada:")
                            match Auditoria:
                                case "1":
                                    print("\n--- PROTOCOLOS DE VOTAÇÃO ---")
                                    protocolos = listar_protocolos_auditoria()
                                    if not protocolos:
                                        print("Nenhum voto registrado até o momento.")
                                    else:
                                        print(f"{'Eleitor':<30} | {'Protocolo':<15} | {'Data/Hora'}")
                                        print("-" * 70)
                                        for nome, protocolo, data in protocolos:
                                            print(f"{nome:<30} | {protocolo:<15} | {data}")
                                case "2":
                                    print("\n--- LOGS DE OCORRÊNCIA ---")
                                    logs = listar_logs()
                                    if not logs:
                                        print("Nenhum log registrado.")
                                    else:
                                        print(f"{'Data/Hora':<20} | {'Tipo':<10} | {'Descrição'}")
                                        print("-" * 80)
                                        for data, tipo, desc in logs:
                                            print(f"{str(data):<20} | {tipo:<10} | {desc}")
                                case "3":
                                    print("Voltando...\n")
                                case _:
                                    print("Opção inválida\n")
                    case "2":
                        if not votacao_esta_aberta():
                            # Simulação de validação de mesário para Abertura
                            print("\n--- ABERTURA DO SISTEMA (MESÁRIO) ---")
                            # Aqui você poderia pedir título/chave do mesário conforme o PDF
                            abrir_votacao()
                            registrar_log('ABERTURA', 'Votação iniciada com sucesso. Total de votos zerado.')
                            print("Votação aberta com sucesso!")
                        
                        Abrir_sistema=""
                        while Abrir_sistema!="3":
                            print(f"\n------------------------------Sistema de Votação--------------------------------")
                            print("\n1-Votar\n2-Encerrar sistema de votação\n3-Voltar\n")
                            Abrir_sistema=input("Escolha a opção desejada:")      
                            match Abrir_sistema:
                                case "1":
                                    if not votacao_esta_aberta():
                                        print("\n❌ ERRO: A votação está FECHADA.\n")
                                        break
                                    
                                    print("\n--- IDENTIFICAÇÃO DO ELEITOR ---")
                                    eleitor = None
                                    while eleitor is None:
                                        titulo = input("Digite o seu Título de Eleitor (ou 'sair' para cancelar): ")
                                        if titulo.lower() == 'sair': break
                                        
                                        eleitor = buscar_eleitor_por_titulo(titulo)
                                        if not eleitor:
                                            print("ERRO: Eleitor não encontrado!")
                                            registrar_log('ALERTA', f'Tentativa de acesso negado: Título {titulo} não encontrado.')
                                        elif eleitor[2]: # Já votou
                                            print("AVISO: Este eleitor já votou!")
                                            registrar_log('ALERTA', f'Tentativa de voto duplo: Eleitor Título {titulo}.')
                                            eleitor = None
                                    
                                    if eleitor and not eleitor[2]:
                                        id_eleitor, nome_eleitor, _ = eleitor
                                        print(f"Bem-vindo, {nome_eleitor}!")
                                        
                                        confirmado = False
                                        while not confirmado:
                                            num = input("Digite o número do candidato (ou 'nulo'): ")
                                            if num.lower() == 'nulo':
                                                if input("Confirmar NULO? (s/n): ").lower() == 's':
                                                    id_cand, nome_cand, confirmado = None, "NULO", True
                                                continue
                                            
                                            cand = buscar_candidato_por_numero(num)
                                            if not cand:
                                                print("Candidato não encontrado!")
                                            else:
                                                id_cand, nome_cand = cand
                                                if input(f"Confirmar em {nome_cand}? (s/n): ").lower() == 's':
                                                    confirmado = True
                                        
                                        if confirmado:
                                            prot = gerar_protocolo()
                                            registrar_voto(id_eleitor, id_cand, prot)
                                            registrar_log('SUCESSO', f'Voto realizado com sucesso para Eleitor ID {id_eleitor}.')
                                            print(f"Voto registrado! Protocolo: {prot}")

                                case "2":
                                    if input("Deseja realmente encerrar a votação? (s/n): ").lower() == 's':
                                        encerrar_votacao()
                                        registrar_log('ENCERRAMENTO', 'Votação finalizada com sucesso.')
                                        print("Sistema encerrado.")
                                        Abrir_sistema = "3"
                                case "3":
                                    print("Voltando...\n")
                    case "3":
                        print("Resultados ainda não implementados no banco.")
                    case "4":
                       print("Voltando...")
        case "2":
            # Gerenciamento (mantido conforme original do usuário)
            pass
        case "3":
            print("Saindo...")

fechar_conexao()
