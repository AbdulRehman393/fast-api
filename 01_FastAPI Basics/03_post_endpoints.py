from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ---------------------------
# Pydantic Model: Nested Review
# ---------------------------
class Review(BaseModel):
    num_stars: int
    text: str
    public: bool = False   # default value

# ---------------------------
# Pydantic Model: Movie Review
# (Contains a nested Review object)
# ---------------------------
class MovieReview(BaseModel):
    movie: str
    review: Review

# ---------------------------
# DB Model (Simulated)
# This is what the database would return
# ---------------------------
class DBReview(MovieReview):
    id: int     # database-generated ID


# ---------------------------
# POST Endpoint
# ---------------------------
@app.post("/reviews", response_model=DBReview)
def create_review(review: MovieReview):
    # Simulate saving to database (fake persistence)
    db_review = DBReview(
        id=1,           # fake DB id
        movie=review.movie,
        review=review.review
    )

    return db_review