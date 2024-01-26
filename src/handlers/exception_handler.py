from fastapi import Request, Response, FastAPI


class BaseCustomException(Exception):
    def __init__(self, message: str, status_code: int) -> None:
        self.message = message
        self.status_code = status_code


class EmptyOriginLinkException(BaseCustomException):
    pass


def empty_origin_link_exception_handler(app: FastAPI):
    @app.exception_handler(EmptyOriginLinkException)
    async def exception_handler(request: Request, exc: EmptyOriginLinkException) -> Response:
        return Response(status_code=exc.status_code, content=exc.message)


def add_exception_handlers(app: FastAPI) -> None:
    empty_origin_link_exception_handler(app=app)
