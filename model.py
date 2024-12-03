class Autor:
    def __init__(self, nome):
        self.nome = nome

    def adicionar_autor(self):
        conexao = Database.conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Autor (nome) VALUES (%s)", (self.nome,))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar_autores():
        conexao = Database.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Autor")
        autores = cursor.fetchall()
        conexao.close()
        return autores

class Livro:
    def __init__(self, titulo, ano_publicacao, autor_id):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.autor_id = autor_id

    def adicionar_livro(self):
        conexao = Database.conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Livro (titulo, ano_publicacao, autor_id) VALUES (%s, %s, %s)",
                       (self.titulo, self.ano_publicacao, self.autor_id))
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar_livros():
        conexao = Database.conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        SELECT Livro.id, Livro.titulo, Livro.ano_publicacao, Autor.nome
        FROM Livro
        JOIN Autor ON Livro.autor_id = Autor.id
        """)
        livros = cursor.fetchall()
        conexao.close()
        return livros
