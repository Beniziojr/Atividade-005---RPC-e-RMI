import grpc
from concurrent import futures
import time

import calculadora_pb2
import calculadora_pb2_grpc

import math

class CalculadoraServicer(calculadora_pb2_grpc.CalculadoraServicer):

    def raiz_quad(self, request, context):
        return calculadora_pb2.Num(value = (math.sqrt(request.value)))

    def multi(self,request, context):
        return calculadora_pb2.Num(value = (request.value1 * request.value2))

    def soma(self,request, context):
        return calculadora_pb2.Num(value = (request.value1 + request.value2))
        

    def sub(self,request, context):
        return calculadora_pb2.Num(value = (request.value1 - request.value2))
        

    def div(self,request, context):
        return calculadora_pb2.Num(value = (request.value1 / request.value2))
        

    def exp(self,request, context):
        return calculadora_pb2.Num(value = (request.value1 ** request.value2))
        

    def resto(self,request, context):
        return calculadora_pb2.Num(value = (request.value1 % request.value2))
        


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


calculadora_pb2_grpc.add_CalculadoraServicer_to_server(
        CalculadoraServicer(), server)


print('Ligando servidor...')
print('Servidor Ligado. Ouvindo na porta 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)