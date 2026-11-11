class Livro: #Isso é uma classe
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def resumo(self): 
        print("--------------------------------") #Isso é um atributo
        print(f"Título do livro: {self.titulo}") #Isso é um atributo
        print(f"Autor(a): {self.autor}") #Isso é um atributo
        print(f"Qtd. páginas: {self.paginas}") #Isso é um atributo

livro1 = Livro("Dom Casmurro", "Machado de Assis", 208) #Isso é uma intância
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96) #Isso é uma intância

livro1.resumo()
livro2.resumo()
print("\nLista original")

livro1.paginas = 362

livro1.resumo()
livro2.resumo()
print("\nLista atualizada")