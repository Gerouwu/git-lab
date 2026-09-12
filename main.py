from fastapi import FastAPI

app = FastAPI( )

@app.get("/health")
def health():
    return {"status":  "ok"}

@app.get("/version")
def version():
    return {"version": "1.1.0"}

@app.get("/author")
def author():
    return {"Author": "Geronimo"}

@app.get("/demo")
def demo():
    return {"Demo": True}
