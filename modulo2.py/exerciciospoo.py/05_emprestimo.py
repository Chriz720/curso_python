class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

    def emprestar(self):
        if self.emprestado:
            return False

        self.emprestado = True
        return True

    def devolver(self):
        if not self.emprestado:
            return False

        self.emprestado = False
        return True


livro = Livro("Dom Casmurro")

for operacao in (livro.emprestar, livro.emprestar, livro.devolver, livro.devolver):
    retorno = operacao()
    print(f"Retorno: {retorno}; emprestado: {livro.emprestado}")
