from fastapi import FastAPI, Depends
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from src.api.v1.shortened_links import router
from src.config import dev_domain


def create_app() -> FastAPI:
    application = FastAPI()
    application.add_middleware(
        middleware_class=TrustedHostMiddleware, allowed_hosts=["localhost", "0.0.0.0", dev_domain]
    )
    application.include_router(router=router)
    # add_exception_handlers(app=application)
    return application


app = create_app()
