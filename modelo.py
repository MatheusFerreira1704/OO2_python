class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def likes(self):
        return self._like
    
    def dar_likes(self):
        self._like += 1
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
        
    # metodo especial para representar o objeto em string  
    def __str__(self):
        return f'Nome: {self._nome} Ano: {self.ano} Likes: {self._like}'
    
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self):
        return f'Nome: {self._nome} Ano: {self.ano} Duração: {self.duracao} Likes: {self._like}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
    def __str__(self):
        return f'Nome: {self._nome} Ano: {self.ano} Temporada: {self.temporadas} Likes: {self._like}'
    
class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas
     
    def tamanho(self):
        return len(self.programas)
    



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist.programas:
    print(programa)


