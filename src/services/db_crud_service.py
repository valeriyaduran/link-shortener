from src.config import session_maker
from src.models.link import Link


async def get_link_from_links_db(link: str) -> str | None:
    with session_maker() as session:
        link_obj = session.query(Link).filter(Link.origin_link == link).all()
        if link_obj:
            return link_obj[0].shortened_link


async def insert_links_data_into_links_db(links_data: dict) -> None:
    with session_maker() as session:
        session.add(
            Link(origin_link=links_data["origin_link"],
                 shortened_link=links_data["shortened_link"],
                 link_id=links_data["link_id"])
        )
        session.commit()


async def delete_link_from_links_db(link_id: str) -> None:
    with session_maker() as session:
        link_obj = session.query(Link).filter(Link.link_id == link_id).all()
        if link_obj:
            session.delete(link_obj[0])
        session.commit()
