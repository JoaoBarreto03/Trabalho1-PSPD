import grpc
from concurrent import futures
import proto_chat_pb2
import proto_chat_pb2_grpc

class ChatService(proto_chat_pb2_grpc.ChatServiceServicer):
    def Chat(self, request_iterator, context):
        for message in request_iterator:
            yield proto_chat_pb2.ChatMessage(user="Servidor", text=f"Recebido: {message.text}")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
proto_chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
server.add_insecure_port('[::]:50054')
server.start()
server.wait_for_termination()
