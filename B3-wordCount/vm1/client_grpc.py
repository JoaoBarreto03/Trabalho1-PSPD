import grpc
import word_count_pb2
import word_count_pb2_grpc

def contar_palavras(texto, ip_servidor):
    with grpc.insecure_channel(f"{ip_servidor}:50053") as channel:
        stub = word_count_pb2_grpc.WordCountServiceStub(channel)
        request = word_count_pb2.TextRequest(text=texto)
        response = stub.CountWords(request)
        return dict(response.word_counts)

def palavra_mais_frequente(texto, ip_servidor):
    with grpc.insecure_channel(f"{ip_servidor}:50054") as channel:
        stub = word_count_pb2_grpc.WordCountServiceStub(channel)
        request = word_count_pb2.TextRequest(text=texto)
        response = stub.MostFrequentWord(request)
        return response.word, response.count

