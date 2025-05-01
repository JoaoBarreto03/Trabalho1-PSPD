import grpc
from concurrent import futures
import time
import server_stream_pb2
import server_stream_pb2_grpc

class NewsService(server_stream_pb2_grpc.NewsServiceServicer):
    def StreamHeadlines(self, request, context):
        headlines = [
            f"{request.category} notícia 1",
            f"{request.category} notícia 2",
            f"{request.category} notícia 3"
        ]
        for headline in headlines:
            yield server_stream_pb2.NewsHeadline(headline=headline)
            time.sleep(1)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
server_stream_pb2_grpc.add_NewsServiceServicer_to_server(NewsService(), server)
server.add_insecure_port('[::]:50052')
server.start()
server.wait_for_termination()
