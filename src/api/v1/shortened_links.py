import json
from fastapi import Request, Response, APIRouter

from src.app.link_shortener import prepare_shortened_link
from src.schemas.link import Link

router = APIRouter()


@router.post("/create_shortened_link")
async def get_link(link: Link, request: Request) -> Response:
    shortened_link = prepare_shortened_link()
    return Response(status_code=200, content=json.dumps(shortened_link))


# @router.delete("/delete_shortened_link")
# async def delete_link(link: Link, request: Request) -> Response:
#     shortened_link = prepare_shortened_link()
#     return Response(status_code=200, content=json.dumps(shortened_link))