from fastapi import FastAPI
from src.routers import catalog, shop, admin, cart
from src.backend.db import Base, engine
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount('/static', StaticFiles(directory="src/static"), name='static')

app.include_router(admin.router)
app.include_router(catalog.router)
app.include_router(shop.router)
app.include_router(cart.router)

@app.get('/')
async def start():
    return FileResponse('src/static/index.html')

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}