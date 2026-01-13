from fastapi import FastAPI

app = FastAPI(title="AutoBlog SaaS")

@app.get("/health")
def health():
    return {"status": "ok"}
