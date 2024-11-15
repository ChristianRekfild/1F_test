from datetime import datetime

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


@app.get("/TestMessage/")
async def get_test_message(message: str):
    print(f'time: {datetime.now()}')
    print(message)
    return {"message": f"{message}"}


# origins = [
#     "*",
#     f"http://localhost:{settings.app_port}",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)