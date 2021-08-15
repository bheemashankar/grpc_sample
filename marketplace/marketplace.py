import os
import grpc
from flask import Flask, jsonify
from google.protobuf.json_format import MessageToDict
from compiles.recommendations_pb2 import RecommendationsRequest, BookCategory
from compiles.recommendations_pb2_grpc import RecommendationsStub


app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
    f"{recommendations_host}:50051"
)
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/", methods=['GET'])
def home_page():
    recommendations_request = RecommendationsRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    recommendations_response = recommendations_client.Recommend(
        recommendations_request
    )
    serialize = MessageToDict(recommendations_response)
    return jsonify(serialize)
