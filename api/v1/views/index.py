from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """
    Retrieves the number of each object by type
    """
    classes = ["User", "State", "City", "Amenity", "Place", "Review"]
    stats = {}
    for cls_name in classes:
        cls_count = storage.count(cls=cls_name)
        stats[cls_name] = cls_count
    return jsonify(stats)
