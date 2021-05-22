import yaml
from notion_client import Client

from build_page import create_page_dict

#from notion_client import Client

with open(r'/Users/simons/Programming/notion-kindle-sync/config.yaml') as file:
    config = yaml.full_load(file)

notion = Client(auth=config['notion_cred']['token'])

for book_id in config['books_to_sync']:
    page_dict = create_page_dict(book_id,config['notion_cred']['database_id'])
    notion.pages.create(**page_dict)

