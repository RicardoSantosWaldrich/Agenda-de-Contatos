"""
1.Adicionar um contato(Nome, telefone, email, favorito)
2.ver a lista de contatos
3.Editar lista de contatos
4.opção de marcar contato como favorito
5.ver so os contatos favoritos
6.selecionar um contato para apagar
"""

def adicionar_contato(agendas, nome, telefone, email):
    agenda = {"Nome": nome, "Telefone": telefone, "Email": email, "Favorito": False}
    agendas.append(agenda)
    print(f"Contato da pessoa {nome} foi adicionada com sucesso!!")
    return

def ver_agenda(agendas):
    print("\nLista de Contato")
    for indece, agenda in enumerate(agendas, start=1):
        status = "★" if agenda["Favorito"] else ""
        nome = agenda["Nome"]
        telefone = agenda["Telefone"]
        email = agenda["Email"]
        print(f"{indece}. [{status}] Nome:{nome} | Telefone:{telefone} | Email:{email}")
    return

def editar_agenda(agendas, indice_agenda, novo_nome_agenda, novo_telefone, novo_email):
    indice_agenda_ajustado = int(indice_agenda) - 1
    if indice_agenda_ajustado >= 0 and indice_agenda_ajustado < len(agendas):
        agendas[indice_agenda_ajustado]["Nome"] = novo_nome_agenda
        agendas[indice_agenda_ajustado]["Telefone"] = novo_telefone
        agendas[indice_agenda_ajustado]["Email"] = novo_email
        print(f"Nome atulizado para {novo_nome_agenda}")
        print(f"Telefone atulizado para {novo_telefone}")
        print(f"Email atulizado para {novo_email}")
    else:
        print("indice invalido")
    return

def marcar_favorita(agendas, indice_agenda):
    indice_agenda_ajustado = int(indice_agenda) - 1
    agendas[indice_agenda_ajustado]["Favorito"] = True
    print(f"Contato {indice_agenda} marcado como favorito")
    return

def ver_favoritas(agendas):
    for agenda in agendas:
        if agenda["Favorito"] == True:
            status = "★"
            nome = agenda["Nome"]
            telefone = agenda["Telefone"]
            email = agenda["Email"]
            print(f"[{status}] Nome:{nome} | Telefone:{telefone} | Email:{email}")
    return

def deletar_contato(agendas, indice_agenda):
    indice_agenda_ajustado = int(indice_agenda) - 1
    if indice_agenda_ajustado >= 0 and indice_agenda_ajustado < len(agendas):
        contato_removido = agendas.pop(indice_agenda_ajustado)
        print(f"Contato {contato_removido['Nome']} excluido com sucesso")
    else:
        print("Indice invalido")
    return


agendas = []

while True:
    print("\nAgenda de Contatos")
    print("1. Adicione um Contato a sua Agenda de Contatos")
    print("2. Veja sua Lista de Contatos")
    print("3. Atualize Dados da sua lista de Contatos")
    print("4. Marque um Contato como favorito")
    print("5. Veja seus Contatos Favoritos")
    print("6. Apague Contatos")
    print("7. Sair")

    escolha = input("Digite Sua Escolha:")

    if escolha == "1":

        # Pedi cada informação separadamente
        nome = input("Digite o Nome do Contato: ")
        telefone = input("Digite o Telefone do Contato: ")
        email = input("Digite o Email do Contato: ")

        # Chamei a função com as variaveis
        adicionar_contato(agendas, nome, telefone, email)

    elif escolha == "2":
        ver_agenda(agendas)
    elif escolha == "3":
        ver_agenda(agendas)
        indice_agenda = input("Digite o numero do contato que deseja atualizar:")
        novo_nome_agenda = input("Digite o novo nome:")
        novo_telefone = input("Digite o novo telefone:")
        novo_email = input("Digite o novo Email:")
        editar_agenda(agendas, indice_agenda, novo_nome_agenda, novo_telefone, novo_email)
    elif escolha == "4":
        ver_agenda(agendas)
        indice_agenda = input("Digete o numero do contato que deseja Favoritar:")
        marcar_favorita(agendas, indice_agenda)
    elif escolha == "5":
        ver_favoritas(agendas)
    elif escolha == "6":
        ver_agenda(agendas)
        indice_agenda = input("Escolha o contato que deseja deletar:")
        deletar_contato(agendas, indice_agenda)

    elif escolha == "7":
        print("Saindo da agenda...")
        break





