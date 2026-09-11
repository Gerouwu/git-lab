from fastapi import FastAPI

app = FastAPI( )

@app.get("/health")
def health():
    return {"status":  "ok"}
@app.get("/version")
def version():
    return {"Version": "1.0.0"}
@app.get("/author")
def author():
    return {"Author": "Juan"}