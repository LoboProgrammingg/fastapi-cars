from fastapi import FastAPI

from .routers import router as car_router


app = FastAPI(
    title='Fast Car API',
    description='LoboProgrammingg modern Car API',
    version='0.1.0',
)


app.include_router(car_router)


@app.get('/')
def read_root():
    return {'status': 'ok'}
