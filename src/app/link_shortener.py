import random
import string

from src.config import dev_domain


def get_generated_value() -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(10))


def prepare_shortened_link() -> str:
    generated = get_generated_value()
    shortened_url = dev_domain + generated
    return shortened_url


def get_shortened_link_id(shortened_link: str) -> str:
    link_id = shortened_link.split("/")[-1]
    return link_id
