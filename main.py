from datetime import datetime

from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/TestMessage/", dependencies=None)
async def get_test_message(message: str):
    print(f'time: {datetime.now()}')
    print(message)


    return {"message": f"{message}"}


@app.post("/TestRequest/", dependencies=None)
async def log_all_requests(request: Request):
    # Логируем запрос
    body = await request.body()
    print("=== Incoming Request ===")
    print(f"Method: {request.method}")
    print(f"URL: {request.url}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Body: {body.decode('utf-8') if body else None}")



@app.get("/")
async def root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)