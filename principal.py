import biblioteca

while True:
    print ('Bem - vindo a Biblioteca Virtual! ')
    print ('1 - Adicionar livro')
    print ('2 - Emprestar livro')
    print ('3 - Devolver livro')
    print ('4 - Mostrar todos os livros disoníveis')
    print ('5 - Adicionar informações sobre um livro')
    print ('6 - Mostrar status de um livro')
    print ('7 - Mudar status de um livro')
    print ('8 - Sair')

    L = int (input('Escolha uma opção: '))

    if L == 1 :
        livro = input ('Adicione o livro:')
        biblioteca.Biblioteca.adicionar(livro)
    elif L == 2:
        livro = input ('Adicione o livro: ')
        biblioteca.Biblioteca.emprestar(livro)
    elif L == 3:
        livro = input ('Adicione o livro: ')
        biblioteca.Biblioteca.devolver
    elif L == 4:
        biblioteca.Biblioteca.imprimir_biblioteca(biblioteca.livros_d)
    elif L == 5:
        info = input ('Adicione o título, autor, ano de publicação e status do livro: ')
        x = biblioteca.Livros(info)
    elif L == 6:
        livro = input ('Adicione um livro para ver o status: ')
        livro = biblioteca.Livros.status()
    elif L == 7:
        livro = input('Adicione um livro para mudar o status: ')
        s = input('Insira o novo status do livro: ')
        livro = biblioteca.Livros.mudar_status(s)
    else:
        break

