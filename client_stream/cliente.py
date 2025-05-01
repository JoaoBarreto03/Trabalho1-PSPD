import grpc
import client_stream_pb2
import client_stream_pb2_grpc

def generate_chunks():
    try:
        with open("exemplo.txt", "r") as f:
            for line in f:
                yield client_stream_pb2.FileChunk(content=line.strip())
    except FileNotFoundError:
        print("Arquivo 'exemplo.txt' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")


channel = grpc.insecure_channel('localhost:50053')
stub = client_stream_pb2_grpc.FileUploaderStub(channel)

response = stub.UploadFile(generate_chunks())
print(response.message)
