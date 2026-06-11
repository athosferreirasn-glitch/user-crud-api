from fastapi import FastAPI, Request
from app.routes.user_route import router

app = FastAPI()

app.include_router(router=router)
