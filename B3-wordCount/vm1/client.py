import grpc
import word_count_pb2
import word_count_pb2_grpc

def contar_palavras(texto, ip_servidor):
    with grpc.insecure_channel(f"{ip_servidor}:50054") as channel:
        stub = proto_pb2_grpc.WordCountServiceStub(channel)
        request = proto_pb2.TextMessage(text=texto)
        response = stub.CountWords(request)
        return dict(response.counts)