class OperaçãoNãoEncontrada(Exception):
    pass


class Soma:
    def executar(self, operandos):
        return operandos[0] + operandos[1]


class Subtração:
    def executar(self, operandos):
        return operandos[0] - operandos[1]


class Divisão:
    def executar(self, operandos):
        return operandos[0] / operandos[1]


class Multiplicação:
    def executar(self, operandos):
        return operandos[0] * operandos[1]


class Calculadora:

    def __init__(self):
        self.operacoes = {}
        self.adicionar_operaçoes('+', Soma())
        self.adicionar_operaçoes('-', Subtração())
        self.adicionar_operaçoes('/', Divisão())
        self.adicionar_operaçoes('*', Multiplicação())

    def adicionar_operaçoes(self, sinal, operaçao):
        self.operacoes[sinal] = operaçao

    def calcular(self):
        operandos = []
        operandos.append(float(input('digite um número:')))
        sinal = input('Digite um operador: ')
        operandos.append(float(input('digite um número:')))
        try:
            soma = self.operacoes[sinal]
            resultado = soma.executar(operandos)
        except KeyError as e:
            raise OperaçãoNãoEncontrada(
                f'Operação não encontrada: {sinal}') from e
        return resultado


calculadora = Calculadora()
while True:
    print(calculadora.calcular())
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break
