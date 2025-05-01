import grpc
from concurrent import futures
import unary_pb2
import unary_pb2_grpc

class Greeter(unary_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return unary_pb2.HelloReply(message=f"Olá, {request.name}!")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
unary_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
