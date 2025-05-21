import uvicorn
from fastapi import FastAPI

from backend.api.routes import router

app = FastAPI(title="Mudar depois" )

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)