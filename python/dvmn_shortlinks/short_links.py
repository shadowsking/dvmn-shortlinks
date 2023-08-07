import os
from urllib.parse import urlparse

import requests


def get_relative_url(short_url: str) -> str:
    parsed_url = urlparse(short_url)
    return "{netloc}{path}".format(netloc=parsed_url.netloc, path=parsed_url.path)


def shorten_link(long_url: str, btl_token: str) -> str:
    data = {
        "long_url": long_url,
    }
    response = requests.post(
        "https://api-ssl.bitly.com/v4/shorten".format(**os.environ),
        headers={"Authorization": "Bearer {}".format(btl_token)},
        json=data,
    )
    response.raise_for_status()
    return response.json().get("link")


def count_clicks(short_url: str, btl_token: str) -> str:
    bitlink = get_relative_url(short_url)
    response = requests.get(
        "https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary".format(
            bitlink=bitlink
        ),
        headers={
            "Authorization": "Bearer {}".format(btl_token),
        },
    )
    response.raise_for_status()
    return response.json().get("total_clicks")


def is_bitlink(short_url: str, btl_token: str) -> bool:
    bitlink = get_relative_url(short_url)
    response = requests.get(
        "https://api-ssl.bitly.com/v4/bitlinks/{bitlink}".format(bitlink=bitlink),
        headers={
            "Authorization": "Bearer {}".format(btl_token),
        },
    )
    return response.ok
