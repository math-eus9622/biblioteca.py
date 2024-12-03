import tkinter as tk
from tkinter import messagebox

class Livro:
    def __init__(self, titulo, autor, ano, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn

class BancoDeDados:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        return [f"{livro.titulo} de {livro.autor} ({livro.ano}) - ISBN: {livro.isbn}" for livro in self.livros]

# Função para adicionar o livro
def adicionar_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    ano = entry_ano.get()
    isbn = entry_isbn.get()

    if titulo and autor and ano and isbn:
        livro = Livro(titulo, autor, ano, isbn)  # Passando o ISBN ao criar o livro
        db.adicionar_livro(livro)
        messagebox.showinfo("Sucesso", f"Livro '{titulo}' adicionado!")
        listar_livros()
    else:
        messagebox.showwarning("Entrada Inválida", "Preencha todos os campos.")

# Função para listar os livros na interface
def listar_livros():
    lista_livros.delete(0, tk.END)
    for livro in db.listar_livros():
        lista_livros.insert(tk.END, livro)

# Criando a interface
root = tk.Tk()
root.title("Sistema de Gerenciamento de Livros")

# Criando o Banco de Dados
db = BancoDeDados()

# Labels e campos de entrada
tk.Label(root, text="Título").grid(row=0, column=0)
entry_titulo = tk.Entry(root)
entry_titulo.grid(row=0, column=1)

tk.Label(root, text="Autor").grid(row=1, column=0)
entry_autor = tk.Entry(root)
entry_autor.grid(row=1, column=1)

tk.Label(root, text="Ano").grid(row=2, column=0)
entry_ano = tk.Entry(root)
entry_ano.grid(row=2, column=1)

tk.Label(root, text="ISBN").grid(row=3, column=0)
entry_isbn = tk.Entry(root)
entry_isbn.grid(row=3, column=1)

# Botão para adicionar livro
botao_adicionar = tk.Button(root, text="Adicionar Livro", command=adicionar_livro)
botao_adicionar.grid(row=4, column=0, columnspan=2)

# Lista de livros
lista_livros = tk.Listbox(root, width=50, height=10)
lista_livros.grid(row=5, column=0, columnspan=2)

# Exibir a lista inicial de livros (vazia no começo)
listar_livros()

# Rodar a interface
root.mainloop()
