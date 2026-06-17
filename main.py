from fastapi import FastAPI, Request
from app.routes.user_route import router
from app.exceptions.handlers import BusinessException, business_exception_handler

app = FastAPI()

app.include_router(router=router)

app.add_exception_handler(
    BusinessException,
    business_exception_handler
)