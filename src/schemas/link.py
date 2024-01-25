from pydantic import BaseModel, field_validator

# from src.handlers.exception_handler import EmptyOriginLinkException


class Link(BaseModel):
    origin_link: str

    # @field_validator("origin_link, shortened_link")
    # def build_name_must_not_be_empty(cls, field_value: str) -> str:
    #     if not field_value:
    #         raise EmptyOriginLinkException(message="Link must not be empty", status_code=400)
    #     return field_value
