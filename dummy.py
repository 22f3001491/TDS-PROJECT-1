# dummy_eval_server.py
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/notify")
async def notify(request: Request):
    data = await request.json()
    print("✅ Notification received:", data)
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
