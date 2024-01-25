import json
from fastapi import Request, Response, APIRouter

from src.app.link_shortener import prepare_shortened_link
from src.schemas.link import Link
from src.services.db_crud_service import insert_links_data_into_links_db

router = APIRouter()


@router.post("/create_shortened_link")
async def get_link(link: Link, request: Request) -> Response:
    shortened_link = prepare_shortened_link()
    await insert_links_data_into_links_db(links_data={"shortened_link": shortened_link,
                                                      "origin_link": link.origin_link})
    return Response(status_code=200, content=json.dumps(shortened_link))


# @router.delete("/delete_shortened_link")
# async def delete_link(link: Link, request: Request) -> Response:
#     shortened_link = prepare_shortened_link()
#     return Response(status_code=200, content=json.dumps(shortened_link))