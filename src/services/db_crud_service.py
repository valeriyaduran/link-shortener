from src.config import session_maker
from src.models.link import Link


async def insert_links_data_into_links_db(links_data: dict) -> None:
    with session_maker() as session:
        session.add(
            Link(origin_link=links_data["origin_link"],
                 shortened_link=links_data["shortened_link"])
        )
        session.commit()


# async def get_links_data_from_links_db(key: dict):
#     with session_maker() as session:
#         session.query(Link).where(key=key)