inicio = ""
while inicio != "3":
    inicio=input("1:Votação\n2:gerenciamento\n3:sair\n")
    match inicio:
        case "1":
            Votação=""
            while Votação!="4":
                Votação=input("1:Auditoria\n2:Abrir sistema de votação\n3:Resultados\n4:Voltar\n")
                match Votação:
                    case "1":
                        Auditoria=""
                        while Auditoria!="3":
                            Auditoria=input("1:Protocolos de votação\n2:Logs de ocorrência\n3:Voltar\n")
                            match Auditoria:
                                case "1":
                                    pass
                                case "2":
                                    pass
                                case "3":
                                    print("Voltando\n")
                                case _:
                                    print("Opção inválida\n")
                    case "2":
                        Abrir_sistema=""
                        while Abrir_sistema!="3":
                            Abrir_sistema=input("1:Votar\n2:Encerrar sistema de votação\n3:Voltar\n")      
                            match Abrir_sistema:
                                case "1":
                                    Votar=""
                                    while Votar!="1":
                                        Votar=input("1:Cancelar voto\n2:Confirmar voto\n")
                                        match Votar:
                                            case "1":
                                                print("Voto cancelado\n")
                                            case "2":
                                                print("Voto confirmado\n")
                                                Votar="1"
                                                Abrir_sistema="3"
                                            case _:
                                                print("Opção inválida\n")
                                case "2":
                                    Encerrar="1"
                                    while Encerrar=="1":
                                        Encerrar=input("1:Não encerrar\n2:Encerrar\n3:Voltar\n")
                                        match Encerrar:
                                            case "1" :
                                                print("Sistema de votação não encerrado\n")
                                            case "2":
                                                print("Encerrando sistema de votação\n")
                                                Abrir_sistema="3"  
                                            case "3":
                                                print("Voltando\n")       
                                            case _:
                                                print("Opção inválida\n")                  
                                case "3":
                                    print("Voltando\n")
                                case _:
                                    print("Opção inválida\n")                    
                    case "3":
                        Resultados=""
                        while Resultados!="5":
                            Resultados=input("1:Boletim de urna\n2:Estatística de comparecimento\n3:Validação de integridade\n4:Votos por partido\n5:Voltar\n")
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
                                    print("Voltando\n")
                                case _:
                                    print("Opção inválida\n")
                    case "4":
                       print("Voltando")
                    case _:
                        print("Opção inválida\n")
        case "2":
            Gerenciamento=""
            while Gerenciamento!="3":
                Gerenciamento=input("1:Eleitores\n2:Candidatos\n3:Voltar\n")
                match Gerenciamento:
                    case "1":
                        Eleitores=""
                        while Eleitores!="6":
                            Eleitores=input("1:Remoção de eleitores\n2:Buscar eleitores\n3:Listagen de eleitores\n4:Editar dados de eleitores\n5:Cadastrar eleitores\n6:Voltar\n")
                            match Eleitores:
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
                                    print("Voltando\n")
                                case _:
                                    print("Opção inválida\n")
                    case "2":
                        Candidatos=""
                        while Candidatos!="6":
                            Candidatos=input("1:Buscar candidato\n2:Cadastro de candidatos\n3:Editar dados de candidatos\n4:Remover candidato\n5:Listar candidatos\n6:Voltar\n")
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
                                    print("Voltando")
                                case _:
                                    print("Opção inválida\n")
                    case "3":
                        print("Voltando\n")
                    case _:
                        print("Opção inválida\n")
        case "3":
            print("Saindo")
        case _:
            print("Opção inválida\n")
        case 3:
            print("Saindo")
        case _:
            print("Opção inválida\n")
