class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=0):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 32

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    walter = Pessoa(nome='Walter Franco', idade=54)
    mozart = Pessoa(walter, nome='Mozart', idade=90)
    print(Pessoa.cumprimentar(mozart))
    print (mozart.nome)
    print (mozart.idade)
    for filho in mozart.filhos:
        print(filho.nome)
        print(filho.idade)
    mozart.sobrenome='Franco'
    del mozart.sobrenome
    mozart.olhos=1
    #del mozart.olhos
    print(mozart.__dict__)
    print(walter.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(mozart.olhos)
    print(walter.olhos)
    print(id(Pessoa.olhos), id(mozart.olhos), id(walter.olhos))
    print(Pessoa.metodo_estatico(), mozart.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), mozart.nome_e_atributos_de_classe())


#    p = Pessoa('Patrícia')
#    print(Pessoa.cumprimentar(p))
#    print (id(p))
#    print(p.cumprimentar())
#    print (p.nome)
#    p.nome='Walter Franco'
#    print (p.nome)
#    print (p.idade)
