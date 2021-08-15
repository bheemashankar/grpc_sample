import grpc
import logging

from compiles import recommendations_pb2, recommendations_pb2_grpc
from compiles.recommendations_pb2 import BookCategory

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        client = recommendations_pb2_grpc.RecommendationsStub(channel)
        response = client.Recommend(recommendations_pb2.RecommendationsRequest(
            user_id=1,
            category=BookCategory.MYSTERY,
            max_results=3
        ))    
    print(response)


if __name__ == '__main__':
    logging.basicConfig()
    run()
