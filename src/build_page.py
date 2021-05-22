import json
from datetime import datetime

with open('/Users/simons/Programming/notion-kindle-sync/data/kindle_highlights.json') as f:
  highlights_dict = json.load(f)
with open('/Users/simons/Programming/notion-kindle-sync/data/kindle_books.json') as f:
  books = json.load(f)




def create_page_dict(book_id, database_id):
    highlights = highlights_dict[book_id]
    sorted(highlights, key = lambda i: i['location'])

    children = []
    for highlight in highlights:
        children.append( {
        "object": "block",
        "has_children": False,
        "type": "paragraph",
        "paragraph": {
            "text": [
            {
                "type": "text",
                "text": {
                "content": "{}(Location {})\n".format(highlight['text'],highlight['location']),
                "link": None
                }
            }
            ]
        }
        })
    



    return {
            "database_id": database_id,
                "parent": { "database_id": database_id },
        "properties": {
        "Author": {
        "id": "Jpub",
        "type": "rich_text",
        "rich_text": [
            {
            "type": "text",
            "text": {
                "content": highlights[0]['author'],
                "link": None
            }
            }
        ]
        },
        "Last Synced": {
        "id": "K|:n",
        "type": "date",
        "date": {
            "start": datetime.today().strftime('%Y-%m-%d'),
            "end": None
        }
        },
        "Category": {
        "id": "b`b|",
        "type": "rich_text",
        "rich_text": [
            {
            "type": "text",
            "text": {
                "content": "Books",
                "link": None
            }
            }
        ]
        },
        "Highlights": {
        "id": "kbeJ",
        "type": "number",
        "number": len(highlights)
        },
        "Name": {
        "id": "title",
        "type": "title",
        "title": [
            {
            "type": "text",
            "text": {
                "content": books[book_id],
                "link": None
            }
            }
        ]
        }
    },
        "children": children
            }
    