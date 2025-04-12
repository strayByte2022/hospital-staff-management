from flask import Blueprint, request, jsonify
from extensions import db
from repositories.staff_repository import StaffRepository
from repositories.schedule_repository import ScheduleRepository
from services.staff_service import StaffService
from services.schedule_service import ScheduleService
from models import Staff, Shift
import datetime

staff_controller = Blueprint('staff', __name__, url_prefix='/api/staff')

staff_repository = StaffRepository()
staff_service = StaffService(staff_repository)

schedule_repository = ScheduleRepository()
schedule_service = ScheduleService(schedule_repository, staff_service)


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
    if not data or not data.get('name') or not data.get('role') or not data.get('department') or not data.get('contact'):
        return jsonify({'error': 'Missing fields'}), 400

    name = data.get('name')
    role = data.get('role')
    department = data.get('department')
    contact = data.get('contact')
    
    try:
        created = staff_service.register_staff(name, role, department, contact)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
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
    name = data.get('name', staff.Name)
    role = data.get('role', staff.Role)
    speciality = data.get('department', staff.Speciality)
    contact = data.get('contact', staff.Contact)
    
    try:
        updated = staff_service.edit_staff(staff_id, name, role, speciality, contact)
        if not updated:
            return jsonify({'error': 'Failed to update staff'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    
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
    return jsonify("success"), 200

@staff_controller.route('/<int:staff_id>/shifts/', methods=['POST'])
def create_shift(staff_id):
    staff = staff_service.get_staff(staff_id)
    if not staff:
        return jsonify({'error': 'Staff not found'}), 404
    
    data = request.get_json()
    if not data or not all(k in data for k in ('shift_start', 'shift_end')):
        return jsonify({'error': 'Shift start and end times are required'}), 400

    try:
        shift_start = datetime.strptime(data.get('shift_start'), '%Y-%m-%dT%H:%M:%S')
        shift_end = datetime.strptime(data.get('shift_end'), '%Y-%m-%dT%H:%M:%S')
        created = schedule_service.add_shift(staff_id, shift_start, shift_end)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({
        'id': created.Id,
        'shift_start': created.ShiftStart,
        'shift_end': created.ShiftEnd
    }), 201
    
@staff_controller.route('/<int:staff_id>/shifts', methods=['GET'])
def get_shifts_within_time(staff_id):
    staff = staff_service.get_staff(staff_id)
    if not staff:
        return jsonify({'error': 'Staff not found'}), 404
    
    try:
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        
        if not start_time or not end_time:
            return jsonify({'error': 'Start and end times are required'}), 400
        
        shifts = schedule_service.get_shifts(staff_id, start_time, end_time)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    return jsonify([{
        'shift_start': s.ShiftStart,
        'shift_end': s.ShiftEnd
    } for s in shifts])

@staff_controller.route('/<int:staff_id>/shifts/availability', methods=['GET'])
def get_staff_availability(staff_id):
    staff = staff_service.get_staff(staff_id)
    if not staff:
        return jsonify({'error': 'Staff not found'}), 404
    
    try:
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        
        if not start_time or not end_time:
            return jsonify({'error': 'Start and end times are required'}), 400
        
        availability = schedule_service.get_staff_availability(staff_id, start_time, end_time)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    return jsonify([{
        'start_time': a[0],
        'end_time': a[1]
    } for a in availability])
    
@staff_controller.route('/<int:staff_id>/shifts/work_hours', methods=['GET'])
def get_staff_work_hours(staff_id):
    staff = staff_service.get_staff(staff_id)
    if not staff:
        return jsonify({'error': 'Staff not found'}), 404
    
    try:
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        
        if not start_time or not end_time:
            return jsonify({'error': 'Start and end times are required'}), 400
        
        work_hours = schedule_service.get_staff_work_hours(staff_id, start_time, end_time)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    return jsonify({
        'work_hours': work_hours
    })
    
@staff_controller.route('/<int:staff_id>/shifts/<int:shift_id>', methods=['DELETE'])
def delete_shift(staff_id, shift_id):
    staff = staff_service.get_staff(staff_id)
    if not staff:
        return jsonify({'error': 'Staff not found'}), 404
    
    try:
        schedule_service.remove_shift(staff_id, shift_id)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    return jsonify({'result': True})