from fastapi import FastAPI

app = FastAPI(
    title="Hybrid Graph RAG API",
    description="Hybrid Vector + Knowledge Graph RAG API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "Hybrid Graph RAG",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
