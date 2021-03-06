# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculadora_pb2 as calculadora__pb2


class CalculadoraStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.soma = channel.unary_unary(
                '/Calculadora/soma',
                request_serializer=calculadora__pb2.doisNums.SerializeToString,
                response_deserializer=calculadora__pb2.Num.FromString,
                )
        self.sub = channel.unary_unary(
                '/Calculadora/sub',
                request_serializer=calculadora__pb2.doisNums.SerializeToString,
                response_deserializer=calculadora__pb2.Num.FromString,
                )
        self.multi = channel.unary_unary(
                '/Calculadora/multi',
                request_serializer=calculadora__pb2.doisNums.SerializeToString,
                response_deserializer=calculadora__pb2.Num.FromString,
                )
        self.div = channel.unary_unary(
                '/Calculadora/div',
                request_serializer=calculadora__pb2.doisNums.SerializeToString,
                response_deserializer=calculadora__pb2.Num.FromString,
                )
        self.raiz_quad = channel.unary_unary(
                '/Calculadora/raiz_quad',
                request_serializer=calculadora__pb2.Num.SerializeToString,
                response_deserializer=calculadora__pb2.Num.FromString,
                )
        self.exp = channel.unary_unary(
                '/Calculadora/exp',
                request_serializer=calculadora__pb2.doisNums.SerializeToString,
                response_deserializer=calculadora__pb2.Num.FromString,
                )
        self.resto = channel.unary_unary(
                '/Calculadora/resto',
                request_serializer=calculadora__pb2.doisNums.SerializeToString,
                response_deserializer=calculadora__pb2.Num.FromString,
                )


class CalculadoraServicer(object):
    """Missing associated documentation comment in .proto file."""

    def soma(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sub(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def multi(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def div(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def raiz_quad(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def exp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def resto(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculadoraServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'soma': grpc.unary_unary_rpc_method_handler(
                    servicer.soma,
                    request_deserializer=calculadora__pb2.doisNums.FromString,
                    response_serializer=calculadora__pb2.Num.SerializeToString,
            ),
            'sub': grpc.unary_unary_rpc_method_handler(
                    servicer.sub,
                    request_deserializer=calculadora__pb2.doisNums.FromString,
                    response_serializer=calculadora__pb2.Num.SerializeToString,
            ),
            'multi': grpc.unary_unary_rpc_method_handler(
                    servicer.multi,
                    request_deserializer=calculadora__pb2.doisNums.FromString,
                    response_serializer=calculadora__pb2.Num.SerializeToString,
            ),
            'div': grpc.unary_unary_rpc_method_handler(
                    servicer.div,
                    request_deserializer=calculadora__pb2.doisNums.FromString,
                    response_serializer=calculadora__pb2.Num.SerializeToString,
            ),
            'raiz_quad': grpc.unary_unary_rpc_method_handler(
                    servicer.raiz_quad,
                    request_deserializer=calculadora__pb2.Num.FromString,
                    response_serializer=calculadora__pb2.Num.SerializeToString,
            ),
            'exp': grpc.unary_unary_rpc_method_handler(
                    servicer.exp,
                    request_deserializer=calculadora__pb2.doisNums.FromString,
                    response_serializer=calculadora__pb2.Num.SerializeToString,
            ),
            'resto': grpc.unary_unary_rpc_method_handler(
                    servicer.resto,
                    request_deserializer=calculadora__pb2.doisNums.FromString,
                    response_serializer=calculadora__pb2.Num.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Calculadora', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Calculadora(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def soma(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculadora/soma',
            calculadora__pb2.doisNums.SerializeToString,
            calculadora__pb2.Num.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sub(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculadora/sub',
            calculadora__pb2.doisNums.SerializeToString,
            calculadora__pb2.Num.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def multi(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculadora/multi',
            calculadora__pb2.doisNums.SerializeToString,
            calculadora__pb2.Num.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def div(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculadora/div',
            calculadora__pb2.doisNums.SerializeToString,
            calculadora__pb2.Num.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def raiz_quad(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculadora/raiz_quad',
            calculadora__pb2.Num.SerializeToString,
            calculadora__pb2.Num.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def exp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculadora/exp',
            calculadora__pb2.doisNums.SerializeToString,
            calculadora__pb2.Num.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def resto(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculadora/resto',
            calculadora__pb2.doisNums.SerializeToString,
            calculadora__pb2.Num.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
