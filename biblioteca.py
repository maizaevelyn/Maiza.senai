livros_d = []
livros_e = []

class Biblioteca:
    def adicionar (livro):
        livros_d.append(livro)

    def emprestar (livro):
        livros_d.remove(livro)
        livros_e.append(livro)
    
    def devolver (livro):
        livros_e.remove(livro)
        livros_d.append(livro)

    def imprimir_biblioteca (livros_d):
        print (livros_d)


class Livros:
    def __init__ (self,titulo,autor,ano,status):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status

    def status (self):
        print ('Livro: ',self.titulo,'Status: ',self.status)
    
    def mudar_status (self,novo):
        self.status = novo
        return self.status