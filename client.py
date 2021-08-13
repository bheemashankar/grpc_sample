import grpc
import logging

from compiles import hello_pb2_grpc, hello_pb2

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    val = input("Enter any word: ")
    if isinstance(val, str):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = hello_pb2_grpc.GreeterStub(channel)
            response = stub.SayHello(hello_pb2.HelloRequest(name=val))    
        print("Greeter client received: " + response.message)
    else:
        print("Send only string.")

if __name__ == '__main__':
    logging.basicConfig()
    run()
