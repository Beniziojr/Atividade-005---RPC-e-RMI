import grpc

import calculadora_pb2
import calculadora_pb2_grpc

canal = grpc.insecure_channel('localhost:50051')

stub = calculadora_pb2_grpc.CalculadoraStub(canal)

def operacoes(stub, operacao):
    if operacao == 0 :
        print('\nDigite o valor a ter a raiz calculada.')
        valor = int(input())
        resposta = stub.raiz_quad(calculadora_pb2.Num(value = valor))
        print('Resposta = ', resposta.value)

    elif operacao == 1 :
        print('\nDigite o primeiro valor.')
        valor1 = int(input())
        print('\nDigite o segundo valor.')
        valor2 = int(input())
        resposta = stub.soma(calculadora_pb2.doisNums(value1=valor1, value2=valor2))
        print('Resposta = ', resposta.value)

    elif operacao == 2 :
        print('\nDigite o primeiro valor.')
        valor1 = int(input())
        print('\nDigite o segundo valor.')
        valor2 = int(input())
        resposta = stub.sub(calculadora_pb2.doisNums(value1=valor1, value2=valor2))
        print('Resposta = ', resposta.value)

    elif operacao == 3 :
        print('\nDigite o primeiro valor.')
        valor1 = int(input())
        print('\nDigite o segundo valor.')
        valor2 = int(input())
        resposta = stub.multi(calculadora_pb2.doisNums(value1=valor1, value2=valor2))
        print('Resposta = ', resposta.value)

    elif operacao == 4 :
        print('\nDigite o primeiro valor.')
        valor1 = int(input())
        print('\nDigite o segundo valor.')
        valor2 = int(input())
        resposta = stub.div(calculadora_pb2.doisNums(value1=valor1, value2=valor2))
        print('Resposta = ', resposta.value)

    elif operacao == 5 :
        print('\nDigite o primeiro valor.')
        valor1 = int(input())
        print('\nDigite o segundo valor.')
        valor2 = int(input())
        resposta = stub.exp(calculadora_pb2.doisNums(value1=valor1, value2=valor2))
        print('Resposta = ', resposta.value)

    elif operacao == 6 :
        print('\nDigite o primeiro valor.')
        valor1 = int(input())
        print('\nDigite o segundo valor.')
        valor2 = int(input())
        resposta = stub.resto(calculadora_pb2.doisNums(value1=valor1, value2=valor2))
        print('Resposta = ', resposta.value)
    
    elif operacao == 7:
        print('\nFechando Calculadora.\n')
        exit()

    else :
        print ('\nOp????o Inv??lida!!!!\n')

while True:
    print('\nDigite: \n' 
        '0 para Raiz Quadrada \n'
        '1 para Soma \n'
        '2 para Subtra????o \n'
        '3 para Multiplica????o \n'
        '4 para Divis??o \n'
        '5 para Exponensia????o \n'
        '6 para Resto da Divis??o \n'
        '7 para Sair da Calculadora \n'
        )
    respostap = input()
    operacao = int(respostap)

    try:
        calculadora_ativa = operacoes(stub, operacao)
            
    except: 
        exit()

