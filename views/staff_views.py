from flask import Blueprint, jsonify, request, make_response
from models import Staff
from app import db

staff_bp = Blueprint('staff_api', __name__, url_prefix='/staff')  # Changed blueprint name

@staff_bp.route('/', methods=['GET'])
def get_staff_list():
    staff = Staff.query.all()
    return jsonify([s.to_dict() for s in staff])  # Use to_dict() and jsonify

@staff_bp.route('/<int:staff_id>', methods=['GET'])
def get_staff_detail(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    return jsonify(staff.to_dict())

@staff_bp.route('/', methods=['POST'])
def create_staff():
    if not request.json:
        return make_response(jsonify({'error': 'Missing JSON'}), 400)  # Bad Request

    name = request.json.get('name')
    role = request.json.get('role')
    department = request.json.get('department')

    if not name:
        return make_response(jsonify({'error': 'Name is required'}), 400)

    new_staff = Staff(name=name, role=role, department=department)
    db.session.add(new_staff)
    db.session.commit()
    return jsonify(new_staff.to_dict()), 201  # Created

@staff_bp.route('/<int:staff_id>', methods=['PUT'])  # Or PATCH
def update_staff(staff_id):
    staff = Staff.query.get_or_404(staff_id)

    if not request.json:
        return make_response(jsonify({'error': 'Missing JSON'}), 400)

    staff.name = request.json.get('name', staff.name)  # Use current value if not provided
    staff.role = request.json.get('role', staff.role)
    staff.department = request.json.get('department', staff.department)

    db.session.commit()
    return jsonify(staff.to_dict())

@staff_bp.route('/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    db.session.delete(staff)
    db.session.commit()
    return jsonify({'result': True})  # Or a 204 No Content