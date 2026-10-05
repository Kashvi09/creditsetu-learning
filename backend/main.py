from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "CreditSetu backend is running!"}

@app.get("/borrowers")
def get_borrowers():
    return [
        {"id": 1, "name": "Priya", "credit_score": 642},
        {"id": 2, "name": "Anita", "credit_score": 718}
    ]

@app.get("/borrowers/{borrower_id}")
def get_borrower(borrower_id: int):
    return {
        "id": borrower_id,
        "name": "Priya",
        "credit_score": 642
    }