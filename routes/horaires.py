from flask import Blueprint, request, jsonify
from models import db, Horaire

horaires_bp = Blueprint('horaires', __name__)

@horaires_bp.route('/', methods=['GET'])
def get_horaires():
    horaires = Horaire.query.all()
    return jsonify([horaire.serialize() for horaire in horaires])

@horaires_bp.route('/', methods=['POST'])
def add_horaire():
    data = request.json
    horaire = Horaire(bus_id=data['bus_id'], trajet_id=data['trajet_id'], departure_time=data['departure_time'], arrival_time=data['arrival_time'])
    db.session.add(horaire)
    db.session.commit()
    return jsonify(horaire.serialize()), 201

@horaires_bp.route('/<int:id>', methods=['PUT'])
def update_horaire(id):
    data = request.json
    horaire = Horaire.query.get_or_404(id)
    horaire.bus_id = data['bus_id']
    horaire.trajet_id = data['trajet_id']
    horaire.departure_time = data['departure_time']
    horaire.arrival_time = data['arrival_time']
    db.session.commit()
    return jsonify(horaire.serialize())

@horaires_bp.route('/<int:id>', methods=['DELETE'])
def delete_horaire(id):
    horaire = Horaire.query.get_or_404(id)
    db.session.delete(horaire)
    db.session.commit()
    return jsonify({'message': 'Horaire deleted successfully'})
