from fastapi import FastAPI

app = FastAPI(
    title="AI Finance OS",
    version="0.1.0-alpha"
)

@app.get("/")
def root():
    return {
        "project": "AI Finance OS",
        "status": "Running",
        "version": "0.1.0-alpha",
        "message": "Welcome to AI Finance OS 🚀"
    }