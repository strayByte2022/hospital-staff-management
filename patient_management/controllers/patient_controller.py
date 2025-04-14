from flask import jsonify, request
from patient_management.services.interfaces.patient_service_interface import IPatientService
from patient_management.services.interfaces.medical_history_service_interface import IMedicalHistoryService
from shared.utils import toDateTime
class PatientController:
    def __init__(self, patient_service: IPatientService, medical_history_service: IMedicalHistoryService):
        self.patient_service = patient_service
        self.medical_history_service = medical_history_service
        
    def get_all_patients(self):
        patients = self.patient_service.get_all()
        return jsonify([p.to_dict() for p in patients]), 200
    
    def get_patient(self, patient_uuid):
        patient = self.patient_service.get_by_patient_uuid(patient_uuid)
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        return jsonify(patient.to_dict()), 200
    
    def create_patient(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing data'}), 400
        try:
            name = data.get('name')
            age = int(data.get('age'))
            gender = data.get('gender')
            contact = data.get('contact')
            address = data.get('address')            
            
            patient = self.patient_service.add(name,age,gender,contact,address)
            
            return jsonify(patient.to_dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
    def update_patient(self, patient_uuid):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing data'}), 400
        try:
            name = data.get('name')
            age = int(data.get('age'))
            gender = data.get('gender')
            contact = data.get('contact')
            address = data.get('address')  
            
            patient = self.patient_service.update(patient_uuid, name, age, gender, contact, address)
            
            return jsonify(patient.to_dict()), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
    def delete_patient(self, patient_uuid):
        try:
            self.patient_service.delete(patient_uuid)
            return jsonify({'message': 'Patient deleted successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
    def get_medical_history(self, patient_uuid):
        medical_history = self.medical_history_service.get_by_patient_id(patient_uuid)
        return jsonify([m.to_dict() for m in medical_history]), 200
    
    def create_medical_history(self, patient_uuid):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing data'}), 400
        try:
            medical_history = self.medical_history_service.add(patient_uuid)
            return jsonify(medical_history.to_dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    def add_diagnosis(self, patient_uuid, history_id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing data'}), 400
        try:
            diagnosis = data.get('diagnosis')
            self.medical_history_service.add_diagnosis(patient_uuid, history_id, diagnosis)
            return jsonify({'message': 'Diagnosis added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
    def add_allergy(self, patient_uuid, history_id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing data'}), 400
        try:
            allergy = data.get('allergy')
            self.medical_history_service.add_allergy(patient_uuid, history_id, allergy)
            return jsonify({'message': 'Allergy added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
    def add_test_results(self, patient_uuid, history_id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing data'}), 400
        try:
            result = data.get('result')
            date = toDateTime(data.get('date'))
            self.medical_history_service.add_test_results(patient_uuid, history_id, date, result)
            return jsonify({'message': 'Test results added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
    def add_prescription(self, patient_uuid, history_id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing data'}), 400
        try:
            medication = data.get('medication')
            dosage = data.get('dosage')
            self.medical_history_service.add_prescription(patient_uuid, history_id, medication, dosage)
            return jsonify({'message': 'Prescription added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        
    
        