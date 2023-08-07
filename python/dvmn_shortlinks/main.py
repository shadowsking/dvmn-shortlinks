import argparse
import os

from dotenv import load_dotenv

import short_links

if __name__ == "__main__":
    load_dotenv()

    btl_token = os.environ["BTL_TOKEN"]

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u",
        "--url",
        help="Accepts the original or short URL",
    )
    args = parser.parse_args()
    url = args.url or input("Please enter a link: ")
    if short_links.is_bitlink(url, btl_token):
        print(
            "Your link was clicked: {} time(s)".format(
                short_links.count_clicks(url, btl_token)
            )
        )
    else:
        print("Bitlink: {}".format(short_links.shorten_link(url, btl_token)))
