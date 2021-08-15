# recommendations.py
from compiles.recommendations_pb2 import (
    BookCategory,
    BookRecommendations
)

from compiles import recommendations_pb2_grpc


books_by_category = {
    BookCategory.MYSTERY: [
        BookRecommendations(id=1, title="The Maltese Falcon"),
        BookRecommendations(id=2, title="Murder on the Orient Express"),
        BookRecommendations(id=3, title="The Hound of the Baskervilles"),
    ],
    BookCategory.SCIENCE_FICTION: [
        BookRecommendations(id=4, title="The Hitchhiker's Guide to the Galaxy"),
        BookRecommendations(id=5, title="Ender's Game"),
        BookRecommendations(id=6, title="The Dune Chronicles"),
    ],

    BookCategory.SELF_HELP: [
        BookRecommendations(id=7, title="The 7 Habits of Highly Effective People"),
        BookRecommendations(id=8, title="How to Win Friends and Influence People"),
        BookRecommendations(id=9, title="Man's Search for Meaning"),
    ],

}