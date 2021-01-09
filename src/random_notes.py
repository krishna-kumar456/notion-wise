import random
import os

from notion.client import NotionClient
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv('NOTION_TOKEN')
KL_URL = os.getenv('KL_URL')
CATALOG_DB_URL = os.getenv('CATALOG_DB_URL')


def get_content():
    """ Get random note links from Notion.

    Args:
        token:
            Notion session token.
        kl_url:
            Page url for Knowledge Lake.
        catalog_db_url:
            DB View url for Catalog Database.
    Returns:
        A dict of knowledge lake and Catalog notes
    """

    # Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
    client = NotionClient(token_v2=NOTION_TOKEN)

    # Replace this URL with the URL of the page you want to edit
    knowledge_lake = client.get_block(KL_URL)
    cv = client.get_collection_view(CATALOG_DB_URL)

    kl_dict = {}
    kh_dict = {}

    for child in knowledge_lake.children:
        if child.type == "page":
            kl_dict[child.title] = child.get_browseable_url()

    for row in cv.collection.get_rows():
        kh_dict[row.title] = row.Source

    kl_rand_title, kl_rand_source = random.choice(list(kl_dict.items()))
    kh_rand_title, kh_rand_source = random.choice(list(kh_dict.items()))

    payload = {
        'kl': {
            kl_rand_title : kl_rand_source
        },
        'kh': {
            kh_rand_title : kh_rand_source
        },

    }

    return payload