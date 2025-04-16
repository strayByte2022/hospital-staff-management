from flask import jsonify, request
from staff_management.services.interfaces.staff_service_interface import IStaffService
from staff_management.services.interfaces.schedule_service_interface import IScheduleService
from shared.utils import toDateTime

class StaffController:
    def __init__(self, staff_service: IStaffService, schedule_service: IScheduleService):
        self.staff_service = staff_service
        self.schedule_service = schedule_service

    def get_all_staff(self):
        staff_list = self.staff_service.list_staff()
        return jsonify([s.to_dict() for s in staff_list])


    def get_staff(self,staff_id):
        staff = self.staff_service.get_staff(staff_id)
        if not staff:
            return jsonify({'error': 'Staff not found'}), 404

        return jsonify(staff.to_dict())


    def create_staff(self):
        data = request.get_json()
        if not data or not data.get('name') or not data.get('role') or not data.get('department') or not data.get('contact'):
            return jsonify({'error': 'Missing fields'}), 400
        
        try:
            created = self.staff_service.register_staff(**data)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
        return jsonify(created.to_dict()), 201


    def update_staff(self,staff_id):
        staff = self.staff_service.get_staff(staff_id)
        if not staff:
            return jsonify({'error': 'Staff not found'}), 404

        data = request.get_json()
        fields = {k: v if v else staff.to_dict().get(k) for k, v in data.items() }

        
        try:
            updated = self.staff_service.update_staff(staff_id, **fields)
            if not updated:
                return jsonify({'error': 'Failed to update staff'}), 400
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
        
        return jsonify(updated.to_dict()), 200


    def delete_staff(self,staff_id):
        staff = self.staff_service.get_staff(staff_id)
        if not staff:
            return jsonify({'error': 'Staff not found'}), 404

        self.staff_service.remove_staff(staff_id)
        return jsonify("success"), 200

    def create_shift(self,staff_id):
        staff = self.staff_service.get_staff(staff_id)
        if not staff:
            return jsonify({'error': 'Staff not found'}), 404
        
        data = request.get_json()
        if not data or not all(k in data for k in ('shift_start', 'shift_end')):
            return jsonify({'error': 'Shift start and end times are required'}), 400

        try:
            shift_start = toDateTime(data.get('shift_start'))
            shift_end = toDateTime(data.get('shift_end'))
            created = self.schedule_service.add_shift(staff_id, shift_start, shift_end)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        return jsonify(created.to_dict()), 201
        
    def get_shifts_within_time(self,staff_id):
        staff = self.staff_service.get_staff(staff_id)
        if not staff:
            return jsonify({'error': 'Staff not found'}), 404
        
        try:
            start_time = request.args.get('start_time')
            end_time = request.args.get('end_time')
            
            shifts = self.schedule_service.get_schedule(staff_id, toDateTime(start_time), toDateTime(end_time))
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
        return jsonify([s.to_dict() for s in shifts])

    def get_staff_availability(self,staff_id):
        staff = self.staff_service.get_staff(staff_id)
        if not staff:
            return jsonify({'error': 'Staff not found'}), 404
        
        try:
            start_time = request.args.get('start_time')
            end_time = request.args.get('end_time')
            
            if not start_time or not end_time:
                return jsonify({'error': 'Start and end times are required'}), 400
            
            availability = self.schedule_service.get_staff_availability(staff_id, toDateTime(start_time), toDateTime(end_time))
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
        return jsonify([{
            'start_time': a[0],
            'end_time': a[1]
        } for a in availability])
        
    def get_staff_work_hours(self,staff_id):
        staff = self.staff_service.get_staff(staff_id)
        if not staff:
            return jsonify({'error': 'Staff not found'}), 404
        
        try:
            start_time = request.args.get('start_time')
            end_time = request.args.get('end_time')
            
            if not start_time or not end_time:
                return jsonify({'error': 'Start and end times are required'}), 400
            
            work_hours = self.schedule_service.get_staff_work_hours(staff_id, toDateTime(start_time), toDateTime(end_time))
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
        return jsonify({
            'work_hours': work_hours
        })
        
    def delete_shift(self,staff_id, shift_id):
        staff = self.staff_service.get_staff(staff_id)
        if not staff:
            return jsonify({'error': 'Staff not found'}), 404
        
        try:
            self.schedule_service.remove_shift(staff_id, shift_id)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        
        return jsonify({'result': True})