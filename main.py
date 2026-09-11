from fastapi import FastAPI

app = FastAPI( )

@app.get("/health")
def health():
    return {"status":  "ok"}

@app.get("/author")
def author():
    return {"Author": "Juan"}