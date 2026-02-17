contatos = []

def adicionar_contato(contatos, nome_contato, numero_telefone, endereco_email):
    contato = {"nome":nome_contato,"telefone":numero_telefone, "email":endereco_email,"favorito": False}

    contatos.append(contato)
    print(f"Contato adicionado com sucesso!")

def ler_campo_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor == "":
            print("Este campo não pode ficar em branco!")
            continue
        return valor


def ver_contatos(contatos):
        print("Lista de contatos")
        for i, contato in enumerate(contatos, start=1):
            status = "Favorito ★" if contato["favorito"] else " "
            print(f"\nContato {i} [{status}]:")
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")

def editar_contato(contatos, opcao, novo_nome, novo_numero, novo_email):
    opcao_ajustada = opcao - 1

    contatos[opcao_ajustada]["nome"] = novo_nome
    contatos[opcao_ajustada]["telefone"] = novo_numero
    contatos[opcao_ajustada]["email"] = novo_email
    print("Contato atualizado com sucesso!")

def ler_opcao_contato(contatos,mensagem):
    while True:
        opcao = input(mensagem)

        if not opcao.isdigit():
            print("Digite apenas números!")
            continue

        opcao = int(opcao)

        if opcao == 0:
            return None

        if not 1 <= opcao <= len(contatos):
            print("Contato não existe!")
            continue

        return opcao  # retorna somente quando for válido

def marcar_favorito(contatos, opcao):
        opcao_ajustada = int(opcao) - 1
        contatos[opcao_ajustada]["favorito"] = True
        print(f"contato {opcao} marcado como favorito!")
        return
def ver_favoritos(contatos):
    print("\n---Contato Favoritos---")

    encontrou = False
    for i, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            print(f"\nContato {i} ")
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Email: {contato['email']}")
            encontrou = True

    if not encontrou:
        print("Nenhum contato favorito foi encontrado.")
def remover_contato(contatos, opcao):
    opcao_ajustada = int(opcao) - 1
    contatos.pop(opcao_ajustada)
    print(f"contato {opcao} removido com Sucesso!")

while True:
        print("\n---Agenda de Contatos---")
        print("1. Adicionar contato")
        print("2. ver contato")
        print("3. Editar contato")
        print("4. Marcar contato como favorito")
        print("5. Ver contatos Favoritos")
        print("6. remover contato")
        print("7. Sair")

        escolha = input("Digite a sua escolha: ")
        # validar se é número
        if not escolha.isdigit():
            print("Digite apenas números!")
            continue

        escolha = int(escolha)

        # validar intervalo
        if not 1 <= escolha <= 7:
            print("Digite uma opção válida (1 a 7)!")
            continue

        if escolha == 1:
            nome_contato = ler_campo_obrigatorio("Digite o nome: ")
            numero_telefone = ler_campo_obrigatorio("Digite o telefone: ")
            endereco_email = ler_campo_obrigatorio("Digite o email: ")
            adicionar_contato(contatos, nome_contato, numero_telefone, endereco_email)
        elif escolha == 2:
            if len(contatos) == 0:
                print("Nenhum contato para existente.")
                continue
            ver_contatos(contatos)
        elif escolha == 3:
            if len(contatos) == 0:
                print("Nenhum contato para editar.")
                continue
            ver_contatos(contatos)
            opcao = ler_opcao_contato(contatos,"Digite qual contato deseja editar (ou digite 0 para sair): ")

            if opcao is None:
                continue

            novo_nome = ler_campo_obrigatorio("Digite o nome: ")
            novo_numero = ler_campo_obrigatorio("Digite o telefone: ")
            novo_email = ler_campo_obrigatorio("Digite o email: ")
            editar_contato(contatos, opcao, novo_nome, novo_numero, novo_email)
        elif escolha == 4:
            if len(contatos) == 0:
                print("Nenhum contato existente.")
                continue
            ver_contatos(contatos)
            opcao = ler_opcao_contato(contatos,"Digite qual contato deseja marcar como favorito (ou digite 0 para voltar): ")
            if opcao is None:
                continue
            marcar_favorito(contatos, opcao)
        elif escolha == 5:
            ver_favoritos(contatos)
        elif escolha == 6:
            if len(contatos) == 0:
                print("Nenhum contato para existente.")
                continue

            ver_contatos(contatos)
            opcao = ler_opcao_contato(contatos,"Digite qual contato deseja remover (ou digite 0 para voltar): ")

            if opcao is None:
                continue
            remover_contato(contatos, opcao)
        elif escolha == 7:
            print("Saindo... Até mais")
            break


