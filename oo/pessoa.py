class Pessoa:
    def __init__(self, *filhos, nome=None, idade=0):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    walter = Pessoa(nome='Walter Franco', idade=54)
    mozart = Pessoa(walter, nome='Mozart', idade=90)
    print (mozart.nome)
    print (mozart.idade)
    for filho in mozart.filhos:
        print(filho.nome)
        print(filho.idade)

#    p = Pessoa('Patrícia')
#    print(Pessoa.cumprimentar(p))
#    print (id(p))
#    print(p.cumprimentar())
#    print (p.nome)
#    p.nome='Walter Franco'
#    print (p.nome)
#    print (p.idade)
