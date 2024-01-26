import json
from fastapi import Request, Response, APIRouter
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK

from src.app.link_shortener import prepare_shortened_link, get_shortened_link_id
from src.schemas.link import Link
from src.services.db_crud_service import insert_links_data_into_links_db, delete_link_from_links_db, \
    get_link_from_links_db

router = APIRouter()


@router.post("/shortened_link")
async def get_link(link: Link, request: Request) -> Response:
    shortened_link = await get_link_from_links_db(link=link.origin_link)
    if not shortened_link:
        shortened_link = prepare_shortened_link()
        link_id = get_shortened_link_id(shortened_link=shortened_link)
        await insert_links_data_into_links_db(links_data={"shortened_link": shortened_link,
                                                          "origin_link": link.origin_link,
                                                          "link_id": link_id})
    return Response(status_code=HTTP_200_OK, content=json.dumps(shortened_link))


@router.delete("/shortened_link/{link_id}")
async def delete_link(link_id: str, request: Request) -> Response:
    await delete_link_from_links_db(link_id=link_id)
    return Response(status_code=HTTP_204_NO_CONTENT)
