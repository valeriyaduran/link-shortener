from pydantic import BaseModel, field_validator
from starlette.status import HTTP_400_BAD_REQUEST

from src.handlers.exception_handler import EmptyOriginLinkException


class Link(BaseModel):
    origin_link: str

    @field_validator("origin_link")
    def link_must_not_be_empty(cls, origin_link: str) -> str:
        if not origin_link:
            raise EmptyOriginLinkException(message="Link must not be empty", status_code=HTTP_400_BAD_REQUEST)
        return origin_link
