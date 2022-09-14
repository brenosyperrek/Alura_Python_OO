class Programa:

    def __init__ (self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes +=1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def __str__(self) -> str:
        return f"Nome: {self.nome} - Ano: {self.ano} - Likes: {self.likes}"

class Filme(Programa):

    def __init__ (self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self) -> str:
        return f"Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} - Likes: {self.likes}"    

class Serie(Programa):

    def __init__ (self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas
        
    def __str__(self) -> str:
        return f"Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self.likes}"

class Playlist():  
    def __init__(self, nome, programas) -> None:
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme("vingadores, guerra infinita", 2018, 140)
strager_things = Serie("strager things", 2016, 4)
breaking_bad = Serie("BREAKING BAD", 2013, 6)
o_nome_da_rosa = Filme("O nome da rosa", 1998, 120)

vingadores.dar_like()
vingadores.dar_like()
strager_things.dar_like()
strager_things.dar_like()
strager_things.dar_like()
breaking_bad.dar_like()
o_nome_da_rosa.dar_like()
o_nome_da_rosa.dar_like()
o_nome_da_rosa.dar_like()
o_nome_da_rosa.dar_like()

playlist = Playlist("Programas para Assistir", [vingadores, strager_things, breaking_bad, o_nome_da_rosa])

print("Tamanho da playlist: {}".format(len(playlist)))

for programa in playlist:
    print(programa)
