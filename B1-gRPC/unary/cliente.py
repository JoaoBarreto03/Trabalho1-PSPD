import grpc
import unary_pb2
import unary_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = unary_pb2_grpc.GreeterStub(channel)

response = stub.SayHello(unary_pb2.HelloRequest(name='João'))
print(response.message)
