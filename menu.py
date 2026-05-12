import sql_insert
from sql_insert import inserir_eleitor, verificao_mesarrio, registrar_voto, verificao_votacao, listar_candidatos,  encerrar_votacao, votacao_esta_aberta, registrar_log, exibir_logs, exibir_protocolos, listar_eleitores, buscar_eleitor, verificar_titulo_eleitor, fechar_conexao, abrir_votacao, encerrar_votacao, votacao_esta_aberta
import random
import criptografia
import mysql.connector
import os
import datetime

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
                                    exibir_protocolos()
                                case "2":
                                    exibir_logs()
                                case "3":
                                    print("Voltando...\n")
                                case _:
                                    print("Opção inválida\n")
                    case "2":
                        Abrir_sistema=""
                        while Abrir_sistema!="3":
                            if votacao_esta_aberta() == False:
                                cpf_mesario = input("Digite o CPF do mesário: ")
                                chave_mesario = input("Digite a chave de acesso do mesário: ")

                                if verificao_mesarrio(cpf_mesario, chave_mesario):
                                    abrir_votacao()
                                    print("\n✅ Votação aberta com sucesso!\n")
                                    registrar_log("ABERTURA: Votação aberta com sucesso.")
                                else:
                                    print("\n❌ ERRO: Credenciais do mesário inválidas.\n")

                                    registrar_log("ABERTURA: Tentativa de abertura de votação com credenciais inválidas.")
                            else:
                                print("A votação já está aberta!")
                            print(f"\n------------------------------Sistema de Votação--------------------------------")
                            print("\n1-Votar\n2-Encerrar sistema de votação\n3-Voltar\n")
                            Abrir_sistema=input("Escolha a opção desejada:")      
                            match Abrir_sistema:
                                case "1":
                                    if votacao_esta_aberta() == False:
                                        print("\n❌ ERRO: A votação está FECHADA. Não é possível votar.\n")
                                        break
                                    cpf = input("Digite o CPF do eleitor: ")
                                    chave = input("Digite a chave de acesso do eleitor: ")

                                    if not verificao_votacao(cpf, chave):
                                        print("\n❌ ERRO: Credenciais do eleitor inválidas ou voto já registrado.\n")
                                        registrar_log(f"VOTO: Tentativa de voto com credenciais inválidas ou voto já registrado para CPF {cpf}.")
                                        break
                                    listar_candidatos()
                                    while votacao_esta_aberta():
                                        print(f"\n----------------------------Votação---------------------------------------------")
                                        print("\n1-Cancelar voto\n2-Confirmar voto\n")
                                        Votar=input("Escolha a opção desejada:")
                                        match Votar:
                                            case "1":
                                                print("Voto cancelado\n")
                                                break
                                            case "2":
                                                print("Voto confirmado\n")
                                                Votar="1"
                                                Abrir_sistema="3"
                                            case _:
                                                print("Opção inválida\n")
                                
                                case "2":
                                    if votacao_esta_aberta():
                                        cpf_mesario = input("Digite o CPF do mesário: ")
                                        chave_mesario = input("Digite a chave de acesso do mesário: ")

                                        if verificao_mesarrio(cpf_mesario, chave_mesario):
                                            encerrar_votacao()
                                            print("\n✅ Votação encerrada com sucesso!\n")
                                            registrar_log("ENCERRAMENTO: Votação encerrada com sucesso.")
                                        else:
                                            print("\n❌ ERRO: Credenciais do mesário inválidas.\n")
                                            registrar_log("ENCERRAMENTO: Tentativa de encerramento de votação com credenciais inválidas.")
                                        break
                                    Encerrar=""
                                    while Encerrar!="3":
                                        print(f"\n----------------------------Encerrar Votação------------------------------------")
                                        print("\n1-Não encerrar\n2-Encerrar\n3-Voltar\n")
                                        Encerrar=input("Escolha a opção desejada:")
                                        match Encerrar:
                                            case "1" :
                                                print("Ainda não implementado")
                                            case "2":
                                                print("Encerrando sistema de votação...\n")
                                                Abrir_sistema="3"
                                            case "3":
                                                print("Voltando...\n")      
                                            case _:
                                                print("Opção inválida\n")                  
                                case "3":
                                    print("Voltando...\n")
                                case _:
                                    print("Opção inválida\n")                    
                    case "3":
                        Resultados=""
                        while Resultados!="5":
                            print(f"\n----------------------------Resultados------------------------------------------")
                            print("\n1-Boletim de urna\n2-Estatística de comparecimento\n3-Validação de integridade\n4-Votos por partido\n5-Voltar\n")
                            Resultados=input("Escolha a opção desejada:")
                            match Resultados:
                                case "1":
                                    pass
                                case "2":
                                    pass
                                case "3":
                                    pass
                                case "4":
                                    pass
                                case "5":
                                    print("Voltando...\n")
                                case _:
                                    print("Opção inválida\n")
                    case "4":
                       print("Voltando...")
                    case _:
                        print("Opção inválida\n")
        case "2":
            Gerenciamento=""
            while Gerenciamento!="3":
                print(f"\n----------------------------Gerenciamento---------------------------------------")
                print("\n1-Eleitores\n2-Candidatos\n3-Voltar\n")
                Gerenciamento=input("Escolha a opção desejada:")
                match Gerenciamento:
                    case "1":
                        Eleitores=""
                        while Eleitores!="6":
                            print(f"\n----------------------------Eleitores-------------------------------------------")
                            print("\n1-Remoção de eleitores\n2-Buscar eleitores\n3-Listagen de eleitores\n4-Editar dados de eleitores\n5-Cadastrar eleitores\n6-Voltar\n")
                            Eleitores=input("Escolha a opção desejada:")
                            match Eleitores:
                                case "1":
                                    sql_insert.excluir_eleitor(input("Digite o CPF ou o Título de eleitor: "))
                                case "2":
                                    valor = input("Digite o nome ou CPF do eleitor para busca: ")
                                    buscar_eleitor(valor)
                                case "3":
                                    listar_eleitores()
                                case "4":
                                    print("Edição ainda não implementada\n")
                                case "5":
                                    nome = input("Digite o nome do eleitor: ")
                                    if nome.find(" ")==-1:
                                        print("\nNome inválido!")
                                    
                                    else:        
                                        cpf_digitado = input("Digite o CPF apenas números: ")
                                        cpf_limpo = ""
                                        for char in cpf_digitado:
                                            if char.isdigit():
                                                cpf_limpo = cpf_limpo + char
                            
                                        status_cpf = verificacaoCPF(cpf_limpo)
                                        
                                        if status_cpf == True:
                                            print(f"O CPF {cpf_digitado} é VÁLIDO e disponível para cadastro.")
                                            titulo=int(input("Título: "))
                                            if not validacaoTitulo(titulo):
                                                print(f"ERRO: O Título de Eleitor {titulo} é INVÁLIDO.")
                                            elif verificar_titulo_eleitor(titulo):
                                                print(f"ERRO: O Título de Eleitor {titulo} já está cadastrado.")
                                            else:
                                                mesario = input("Mesário (s/n): ").lower() == "s"
                                                chave = nome[0].upper()+nome[1].upper()+nome[nome.find(" ")+1].upper()+str(random.randint(1000,9999))
                                                inserir_eleitor(nome, cpf_limpo, titulo, mesario, chave)
        
                                        elif status_cpf == "CADASTRADO":
                                            print(f"ERRO: O CPF {cpf_digitado} já está cadastrado no sistema.")
                                        else:
                                            print(f"ERRO: O CPF {cpf_digitado} é INVÁLIDO.")

                                case "6":
                                    print("Voltando...\n")
                                case _:
                                    print("Opção inválida\n")
                    case "2":
                        Candidatos=""
                        while Candidatos!="6":
                            print(f"\n----------------------------Candidatos------------------------------------------")
                            print("\n1-Buscar candidato\n2-Cadastro de candidatos\n3-Editar dados de candidatos\n4-Remover candidato\n5-Listar candidatos\n6-Voltar\n")
                            Candidatos=input("Escolha a opção desejada:")
                            match Candidatos:
                                case "1":
                                    pass
                                case "2":
                                    pass
                                case "3":
                                    pass
                                case "4":
                                    pass
                                case "5":
                                    pass
                                case "6":
                                    print("Voltando...")
                                case _:
                                    print("Opção inválida\n")
                    case "3":
                        print("Voltando...\n")
                    case _:
                        print("Opção inválida\n")
        case "3":
            print("Saindo...")
        case _:
            print("Opção inválida\n")

fechar_conexao()
