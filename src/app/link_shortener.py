import random
import string

from src.config import dev_domain


def prepare_shortened_link() -> str:
    generated = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    shortened_url = dev_domain + generated
    return shortened_url
