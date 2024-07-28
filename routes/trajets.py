from flask import Blueprint, request, jsonify
from models import db, Trajet

trajets_bp = Blueprint('trajets', __name__)

@trajets_bp.route('/', methods=['GET'])
def get_trajets():
    trajets = Trajet.query.all()
    return jsonify([trajet.serialize() for trajet in trajets])

@trajets_bp.route('/', methods=['POST'])
def add_trajet():
    data = request.json
    trajet = Trajet(start=data['start'], end=data['end'], distance=data['distance'])
    db.session.add(trajet)
    db.session.commit()
    return jsonify(trajet.serialize()), 201

@trajets_bp.route('/<int:id>', methods=['PUT'])
def update_trajet(id):
    data = request.json
    trajet = Trajet.query.get_or_404(id)
    trajet.start = data['start']
    trajet.end = data['end']
    trajet.distance = data['distance']
    db.session.commit()
    return jsonify(trajet.serialize())

@trajets_bp.route('/<int:id>', methods=['DELETE'])
def delete_trajet(id):
    trajet = Trajet.query.get_or_404(id)
    db.session.delete(trajet)
    db.session.commit()
    return jsonify({'message': 'Trajet deleted successfully'})
