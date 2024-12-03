from controller import Biblioteca
from model import Autor, Livro


def menu_principal():
    while True:
        print("\n=== Biblioteca ===")
        print("1. Adicionar Autor")
        print("2. Listar Autores")
        print("3. Adicionar Livro")
        print("4. Listar Livros")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do autor: ")
            Autor(nome).adicionar_autor()
            print("Autor adicionado com sucesso!")

        elif opcao == "2":
            Biblioteca.gerenciar_autores()

        elif opcao == "3":
            titulo = input("Título do livro: ")
            ano = int(input("Ano de publicação: "))
            autor_id = int(input("ID do autor: "))
            Livro(titulo, ano, autor_id).adicionar_livro()
            print("Livro adicionado com sucesso!")

        elif opcao == "4":
            Biblioteca.gerenciar_livros()

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")
