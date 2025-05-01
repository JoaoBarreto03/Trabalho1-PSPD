import grpc
import server_stream_pb2
import server_stream_pb2_grpc

channel = grpc.insecure_channel('localhost:50052')
stub = server_stream_pb2_grpc.NewsServiceStub(channel)

responses = stub.StreamHeadlines(server_stream_pb2.NewsRequest(category="Esportes"))
for res in responses:
    print(res.headline)
