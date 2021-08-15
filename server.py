import sys
import grpc
import random
import logging
from signal import signal, SIGTERM, SIGINT, SIGKILL
from concurrent import futures
from recommendations import books_by_category
from compiles import recommendations_pb2, recommendations_pb2_grpc


class RecommendationsService(recommendations_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")
        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(books_for_category, num_results)
        return recommendations_pb2.RecommendationsResponse(recommendations=books_to_recommend)


# Server setup and starting
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(RecommendationsService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on localhost:50051 Use Ctrl-C to exit ")

    def handle_sigterm(*_):
        print("Received shutdown signal")
        all_rpcs_done_event = server.stop(30)
        all_rpcs_done_event.wait(30)
        print("Shut down gracefully")

    signal(SIGTERM, handle_sigterm)
    signal(SIGINT, handle_sigterm)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
