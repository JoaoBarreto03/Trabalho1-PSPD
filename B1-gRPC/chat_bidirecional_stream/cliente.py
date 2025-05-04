import grpc
import proto_chat_pb2
import proto_chat_pb2_grpc

def generate_messages():
    textos = ["Oi", "Tudo bem?", "Até mais!"]
    for txt in textos:
        yield proto_chat_pb2.ChatMessage(user="João", text=txt)

def call_server(address):
    channel = grpc.insecure_channel(address)
    stub = proto_chat_pb2_grpc.ChatServiceStub(channel)
    responses = stub.Chat(generate_messages())
    for res in responses:
        print(f"{res.user}: {res.text}")

IP_VM2 = r"192.168.122.87:50054"
IP_VM3 = r"192.168.122.253:50054"


# IPs reais das suas VMs VM2 e VM3
call_server(IP_VM2)  # VM2
# call_server(IP_VM3)  # VM3
