from routes import bp
from ..apis import get_items, get_item


@bp.route('/items', methods=['GET'])
def items():
    return jsonify(get_items())

@bp.route('/items/<int:item_id>', methods=['GET'])
def item(item_id):
    item = get_item(item_id)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

