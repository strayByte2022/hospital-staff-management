from flask import Blueprint
from staff_management.controllers.staff_controller import StaffController
from staff_management.services.staff_service import StaffService
from staff_management.repositories.staff_repository import StaffRepository
from staff_management.repositories.schedule_repository import ScheduleRepository
from staff_management.services.schedule_service import ScheduleService

def init_staff_blueprint():
    staff_blueprint = Blueprint('staff', __name__, url_prefix='/api/staff')
    staff_repository = StaffRepository()
    schedule_repository = ScheduleRepository()
    staff_service = StaffService(staff_repository)
    schedule_service = ScheduleService(schedule_repository, staff_service)
    staff_controller = StaffController(staff_service, schedule_service)
    staff_blueprint.add_url_rule('/', view_func=staff_controller.get_all_staff, methods=['GET'])
    staff_blueprint.add_url_rule('/<uuid:staff_id>', view_func=staff_controller.get_staff, methods=['GET'])
    staff_blueprint.add_url_rule('/', view_func=staff_controller.create_staff, methods=['POST'])
    staff_blueprint.add_url_rule('/<uuid:staff_id>', view_func=staff_controller.update_staff, methods=['PUT'])
    staff_blueprint.add_url_rule('/<uuid:staff_id>', view_func=staff_controller.delete_staff, methods=['DELETE'])
    
    staff_blueprint.add_url_rule('/<uuid:staff_id>/shifts', view_func=staff_controller.get_shifts_within_time, methods=['GET'])
    staff_blueprint.add_url_rule('/<uuid:staff_id>/shifts', view_func=staff_controller.create_shift, methods=['POST'])
    staff_blueprint.add_url_rule('/<uuid:staff_id>/shifts', view_func=staff_controller.delete_shift, methods=['DELETE'])
    staff_blueprint.add_url_rule('/<uuid:staff_id>/shifts/availability', view_func=staff_controller.get_staff_availability, methods=['GET'])
    staff_blueprint.add_url_rule('/<uuid:staff_id>/shifts/workhours', view_func=staff_controller.get_staff_work_hours, methods=['GET'])
    
    return staff_blueprint

from patient_management.controllers.patient_controller import PatientController
from patient_management.services.patient_service import PatientService
from patient_management.repositories.patient_repository import PatientRepository
from patient_management.repositories.medical_history_repository import MedicalHistoryRepository
from patient_management.services.medical_history_service import MedicalHistoryService

def init_patient_blueprint():
    patient_blueprint = Blueprint('patient', __name__, url_prefix='/api/patients')
    patient_repository = PatientRepository()
    medical_history_repository = MedicalHistoryRepository()
    patient_service = PatientService(patient_repository)
    medical_history_service = MedicalHistoryService(medical_history_repository)
    patient_controller = PatientController(patient_service, medical_history_service)
    
    patient_blueprint.add_url_rule('/', view_func=patient_controller.get_all_patients, methods=['GET'])
    patient_blueprint.add_url_rule('/<uuid:patient_uuid>', view_func=patient_controller.get_patient, methods=['GET'])
    patient_blueprint.add_url_rule('/', view_func=patient_controller.create_patient, methods=['POST'])
    patient_blueprint.add_url_rule('/<uuid:patient_uuid>', view_func=patient_controller.update_patient, methods=['PUT'])
    patient_blueprint.add_url_rule('/<uuid:patient_uuid>', view_func=patient_controller.delete_patient, methods=['DELETE'])
    
    patient_blueprint.add_url_rule('/<uuid:patient_uuid>/medical_history', view_func=patient_controller.get_medical_history, methods=['GET'])
    patient_blueprint.add_url_rule('/<uuid:patient_uuid>/medical_history', view_func=patient_controller.create_medical_history, methods=['POST'])
    
    patient_blueprint.add_url_rule(
        '/<uuid:patient_uuid>/medical_history/diagnosis',
        defaults={'history_id': None},
        view_func=patient_controller.add_diagnosis,
        methods=['POST']
    )
    patient_blueprint.add_url_rule(
        '/<uuid:patient_uuid>/medical_history/<int:history_id>/diagnosis',
        view_func=patient_controller.add_diagnosis,
        methods=['POST']
    )
    
    patient_blueprint.add_url_rule(
        '/<uuid:patient_uuid>/medical_history/allergy',
        defaults={'history_id': None},
        view_func=patient_controller.add_allergy,
        methods=['POST']
    )
    patient_blueprint.add_url_rule(
        '/<uuid:patient_uuid>/medical_history/<int:history_id>/allergy',
        view_func=patient_controller.add_allergy,
        methods=['POST']
    )
    
    patient_blueprint.add_url_rule(
        '/<uuid:patient_uuid>/medical_history/test',
        defaults={'history_id': None},
        view_func=patient_controller.add_test_results,
        methods=['POST']
    )
    patient_blueprint.add_url_rule(
        '/<uuid:patient_uuid>/medical_history/<int:history_id>/test',
        view_func=patient_controller.add_test_results,
        methods=['POST']
    )
    
    patient_blueprint.add_url_rule(
        '/<uuid:patient_uuid>/medical_history/prescription',
        defaults={'history_id': None},
        view_func=patient_controller.add_prescription,
        methods=['POST']
    )
    patient_blueprint.add_url_rule(
        '/<uuid:patient_uuid>/medical_history/<int:history_id>/prescription',
        view_func=patient_controller.add_prescription,
        methods=['POST']
    )
    
    return patient_blueprint
