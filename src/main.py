from fastapi import FastAPI
from routers import catalog, shop, admin, cart
from backend.db import Base, engine
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount('/static', StaticFiles(directory="static"), name='static')

app.include_router(admin.router)
app.include_router(catalog.router)
app.include_router(shop.router)
app.include_router(cart.router)

@app.get('/')
async def start():
    return FileResponse('static/index.html')