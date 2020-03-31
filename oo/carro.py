"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

Motor
Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

Atributo de dado velocidade
Método acelerar, que deverá incremetar a velocidade de uma unidade
Método frear que deverá decrementar a velocidade em duas unidades
A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
Método girar_a_direita
Método girar_a_esquerda

Exemplo
    # >>> testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor = Motor()
    >>> motor.velocidade
    1
    >>> motor = Motor()
    >>> motor.velocidade
    2
    >>> motor = Motor()
    >>> motor.velocidade
    3
    >>> motor = Motor()
    >>> motor.frear
    1
    >>> motor = Motor()
    >>> motor.frear
    0
    # >>> testando direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    ‘Norte’
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    ‘Sul’
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    ‘Oeste’
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    ‘Norte’
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    ‘Oeste’
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    ‘Sul’
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    ‘Leste’
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    ‘Norte’
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>>carro.calcular_direcao()
    ‘Norte’
    >>>carro.girar_a_direita()
    >>>carro.calcular_direcao()
    ‘Leste’
    >>>carro.girar_a_esquerda()
    >>>carro.calcular_direcao()
    ‘Norte’
    >>>carro.girar_a_esquerda()
    >>>carro.calcular_direcao()
    ‘Oeste’

"""

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)

    # direcao:


class Direcao():
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }

    def __init__(self):
        self.direcao = 'Norte'

    def girar_a_direita(self):
        self.direcao = self.rotacao_a_direita_dct[self.direcao]

    #        if self.direcao == 'Norte':
    #            self.direcao = 'Leste'
    #        elif self.direcao == 'Leste':
    #            self.direcao = 'Sul'
    #        elif self.direcao == 'Sul':
    #            self.direcao = 'Oeste'
    #        elif self.direcao == 'Oeste':
    #            self.direcao = 'Norte'

    def girar_a_esquerda(self):
        self.direcao = self.rotacao_a_esquerda_dct[self.direcao]


#        if self.direcao == 'Norte':
#            self.direcao = 'Oeste'
#        elif self.direcao == 'Oeste':
#            self.direcao = 'Sul'
#        elif self.direcao == 'Sul':
#            self.direcao = 'Leste'
#        elif self.direcao == 'Leste':
#            self.direcao = 'Norte'

if __name__ == '__main__':
    direcao = Direcao()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
