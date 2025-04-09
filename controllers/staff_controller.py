from flask import Blueprint, request, jsonify
from models import Staff
from extensions import db
from repositories.staff_repository import StaffRepository
from services.staff_service import StaffService

staff_controller = Blueprint('staff', __name__, url_prefix='/api/staff')

# Initialize service
staff_repository = StaffRepository()
staff_service = StaffService(staff_repository)


@staff_controller.route('/', methods=['GET'])
def get_all_staff():
    staff_list = staff_service.list_staff()
    return jsonify([
        {
            'id': s.Id,
            'name': s.Name,
            'role': s.Role,
            'department': s.Speciality
        } for s in staff_list
    ])


@staff_controller.route('/<staff_id>', methods=['GET'])
def get_staff(staff_id):
    staff = staff_service.get_staff(staff_id)
    if not staff:
        return jsonify({'error': 'Staff not found'}), 404

    return jsonify({
        'id': staff.Id,
        'name': staff.Name,
        'role': staff.Role,
        'department': staff.Speciality
    })


@staff_controller.route('/', methods=['POST'])
def create_staff():
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'error': 'Name is required'}), 400

    staff = Staff(
        Name=data.get('name'),
        Role=data.get('role'),
        Speciality=data.get('department')
    )
    created = staff_service.create_staff(staff)
    return jsonify({
        'id': created.Id,
        'name': created.Name,
        'role': created.Role,
        'department': created.Speciality
    }), 201


@staff_controller.route('/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    staff = staff_service.get_staff(staff_id)
    if not staff:
        return jsonify({'error': 'Staff not found'}), 404

    data = request.get_json()
    staff.Name = data.get('name', staff.Name)
    staff.Role = data.get('role', staff.Role)
    staff.Speciality = data.get('department', staff.Speciality)
    updated = staff_service.edit_staff(staff)

    return jsonify({
        'id': updated.Id,
        'name': updated.Name,
        'role': updated.Role,
        'department': updated.Speciality
    })


@staff_controller.route('/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    staff = staff_service.get_staff(staff_id)
    if not staff:
        return jsonify({'error': 'Staff not found'}), 404

    staff_service.remove_staff(staff_id)
    return jsonify({'result': True})


@staff_controller.route('/uuid/<staff_uuid>', methods=['GET'])
def get_staff_by_uuid(staff_uuid):
    staff = staff_service.get_staff_by_uuid(staff_uuid)
    if not staff:
        return jsonify({'error': 'Staff not found'}), 404

    return jsonify({
        'id': staff.Id,
        'staff_id': staff.StaffId,
        'name': staff.Name,
        'role': staff.Role,
        'department': staff.Speciality
    })
