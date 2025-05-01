import grpc
import proto_chat_pb2
import proto_chat_pb2_grpc

def generate_messages():
    textos = ["Oi", "Tudo bem?", "Até mais!"]
    for txt in textos:
        yield proto_chat_pb2.ChatMessage(user="João", text=txt)

channel = grpc.insecure_channel('localhost:50054')
stub = proto_chat_pb2_grpc.ChatServiceStub(channel)

responses = stub.Chat(generate_messages())
for res in responses:
    print(f"{res.user}: {res.text}")
