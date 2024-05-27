from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models import storage, Place, Amenity

@app_views.route('/places/<place_id>/amenities', methods=['GET'])
def get_place_amenities(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    
    amenities = []
    for amenity_id in place.amenity_ids:
        amenity = storage.get(Amenity, amenity_id)
        if amenity:
            amenities.append(amenity.to_dict())
    return jsonify(amenities)

@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'])
def delete_place_amenity(place_id, amenity_id):
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if not place or not amenity:
        abort(404)
    
    if amenity_id not in place.amenity_ids:
        abort(404)
    
    place.amenity_ids.remove(amenity_id)
    storage.save()
    return jsonify({}), 200

@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'])
def link_amenity_to_place(place_id, amenity_id):
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if not place or not amenity:
        abort(404)
    
    if amenity_id in place.amenity_ids:
        return jsonify(amenity.to_dict()), 200
    
    place.amenity_ids.append(amenity_id)
    storage.save()
    return jsonify(amenity.to_dict()), 201
