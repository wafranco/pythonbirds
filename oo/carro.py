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

"""
class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1
        return self.velocidade

    def frear(self):
        self.velocidade = 0 if self.velocidade - 2 < 0 else self.velocidade - 2


if __name__ == '__main__':
    motor = Motor(velocidade=0)
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
    def __init__(self):
        self.direcao = 'Norte'

    def girar_a_direita(self):
        if self.direcao == 'Norte':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Norte'

    def girar_a_esquerda(self):
        if self.direcao == 'Norte':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Norte'

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
