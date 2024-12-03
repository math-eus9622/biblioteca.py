class Biblioteca:
    @staticmethod
    def gerenciar_livros():
        livros = Livro.listar_livros()
        for livro in livros:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Ano: {livro[2]}, Autor: {livro[3]}")

    @staticmethod
    def gerenciar_autores():
        autores = Autor.listar_autores()
        for autor in autores:
            print(f"ID: {autor[0]}, Nome: {autor[1]}")
