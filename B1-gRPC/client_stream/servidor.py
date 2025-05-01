import grpc
from concurrent import futures
import client_stream_pb2
import client_stream_pb2_grpc

class FileUploader(client_stream_pb2_grpc.FileUploaderServicer):
    def UploadFile(self, request_iterator, context):
        full_content = ""
        for chunk in request_iterator:
            full_content += chunk.content
        return client_stream_pb2.UploadStatus(message=f"Arquivo recebido: {len(full_content)} caracteres.")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
client_stream_pb2_grpc.add_FileUploaderServicer_to_server(FileUploader(), server)
server.add_insecure_port('[::]:50053')
server.start()
server.wait_for_termination()
