import grpc
import logging
from concurrent import futures
from compiles import hello_pb2, hello_pb2_grpc


class Greeter(hello_pb2_grpc.GreeterServicer):

  def SayHello(self, request, context):
    return hello_pb2.HelloResponse(message='Hello, %s!' % request.name)

  def SayHelloAgain(self, request, context):
    return hello_pb2.HelloResponse(message='Hello again, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
