lista = []

while True:
    print("\nMenu de opções:")
    print("1. Cadastrar contatos")
    print("2. Remover contato")
    print("3. Buscar contato por nome")
    print("4. Listar aniversariantes do mês")
    print("5. Exibir todos os contatos")
    print("6. Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        num_contatos = int(input('Quantos contatos você deseja cadastrar? '))
        for i in range(num_contatos):
            print(f'\nDigite os dados do contato {i+1}:')
            nome = input('Digite o nome: ')
            data = input('Digite a data (exemplo: 23/02/2005): ')
            endereco = input('Digite o endereço: ')
            telefone = input('Digite o telefone: ')
            
            contato = [nome, data, endereco, telefone]
            lista.append(contato)
        print("\nContatos cadastrados com sucesso!")

    elif opcao == 2:
        removercontato = input('Digite a posição do contato a ser removido: ')
        removercontato = int(removercontato)
        lista.pop(removercontato)
        print(lista)

    elif opcao == 3:
        nome = input('Digite o nome desejado: ')
        for i in lista:
            if i[0] == nome:
                print(i)

    elif opcao == 4:
        aniversario = input('Digite o mês para imprimir os aniversariantes (exemplo: se for fevereiro, escrever 02): ')
        for i in lista:
            if i[1][3:5] == aniversario:
                print(i)

    elif opcao == 5:
        if lista:
            print("\nLista de contatos:")
            for contato in lista:
                print(contato)

    elif opcao == 6:
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
