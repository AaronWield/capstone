
from flask import Blueprint, jsonify, request, url_for
from soccer_api.helpers import token_required
from soccer_api.models import Favorite, favorite_schema, favorites_schema, db


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/favorites', methods = ['POST'])
@token_required
def create_favorite(current_user_token):
    team = request.json['team']
    player = request.json['player']
    match = request.json['match']
    explanation = request.json['explanation']
    comments = request.json['comments']
    user_token = current_user_token.token

    favorite = Favorite(team, player, match, explanation, comments, user_token=user_token)

    db.session.add(favorite)
    db.session.commit()

    response = favorite_schema.dump(favorite)
    return jsonify(response)

@api.route('/favorites', methods = ['GET'])
@token_required
def get_favorites(current_user_token):
    owner = current_user_token.token
    favorites = Favorite.query.filter_by(user_token = owner).all()
    response = favorites_schema.dump(favorites)
    return jsonify(response)

@api.route('/favorites/<id>', methods = ['GET'])
@token_required
def get_favorite(current_user_token, id):
    favorite = Favorite.query.get(id)
    if favorite:
        response = favorite_schema.dump(favorite)
        return jsonify(response)
    else:
        return jsonify({'message':"That does not exist."})


@api.route('/favorites/<id>', methods = ['POST'])
@token_required
def update_favorite(current_user_token, id):
    favorite = Favorite.query.get(id)
    if favorite:
        favorite.team = request.json['team']
        favorite.player = request.json['player']
        favorite.match = request.json['match']
        favorite.explanation = request.json['explanation']
        favorite.comments = request.json['comments']
        favorite.user_token = current_user_token.token

        db.session.commit()

        response = favorite_schema.dump(favorite)
        return jsonify(response)
    else:
        jsonify({'message': 'That does not exist.'})

@api.route('/favorites/<id>', methods = ['DELETE'])
@token_required
def delete_favorite(current_user_token, id):
    favorite = Favorite.query.get(id)
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        response = favorite_schema.dump(favorite)
        return jsonify(response)
    else:
        return jsonify({'message':"That does not exist."})