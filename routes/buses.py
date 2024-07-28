from flask import Blueprint, request, jsonify
from models import db, Bus

buses_bp = Blueprint('buses', __name__)

@buses_bp.route('/', methods=['GET'])
def get_buses():
    buses = Bus.query.all()
    return jsonify([bus.serialize() for bus in buses])

@buses_bp.route('/', methods=['POST'])
def add_bus():
    data = request.json
    bus = Bus(name=data['name'], capacity=data['capacity'])
    db.session.add(bus)
    db.session.commit()
    return jsonify(bus.serialize()), 201

@buses_bp.route('/<int:id>', methods=['PUT'])
def update_bus(id):
    data = request.json
    bus = Bus.query.get_or_404(id)
    bus.name = data['name']
    bus.capacity = data['capacity']
    db.session.commit()
    return jsonify(bus.serialize())

@buses_bp.route('/<int:id>', methods=['DELETE'])
def delete_bus(id):
    bus = Bus.query.get_or_404(id)
    db.session.delete(bus)
    db.session.commit()
    return jsonify({'message': 'Bus deleted successfully'})
