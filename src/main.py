from fastapi import FastAPI

from src.api.v1.shortened_links import router
from src.handlers.exception_handler import add_exception_handlers


def create_app() -> FastAPI:
    application = FastAPI()
    application.include_router(router=router)
    add_exception_handlers(app=application)
    return application


app = create_app()
