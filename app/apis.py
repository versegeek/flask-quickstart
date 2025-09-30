from app.models import Item

items = [
    Item(1, 'Item 1'),
    Item(2, 'Item 2')
]

def get_items():
    return [item.to_dict() for item in items]

def get_item(item_id):
    for item in items:
        if item.id == item_id:
            return item.to_dict()
    return None
