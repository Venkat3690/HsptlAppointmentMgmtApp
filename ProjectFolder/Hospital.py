import streamlit as st
import Appointment as ap
import Patient as pt 
import Doctor as dc

class Hospital:
    def __init__(self,name):
        self.name=name
        self.patients=[]
        self.doctors=[]
        self.appointments=[]
    #Patient Management
    #Adding a patient details
    def add_patient(self,patient):
        self.patient.append(patient)
    #displaying the patient details
    def display_patients(self):
        st.subheader("\n--- Patients ---")
        for patient in self.patients:
            st.write(patient)
    #removing the patient details
    def remove_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                return True
        return False
    #Doctor Management
    #Adding a doctor details
    def add_doctors(self,doctor):
        self.doctors.append(doctor)
    #displaying the doctor details
    def display_doctor(self):
        st.subheader("\n--- Doctors ---")
        for doctor in self.doctors:
            st.write(doctor)
    #removing the patient details
    def remove_doctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                self.doctors.remove(doctor)
                return True
        return False
    #Appointment MAnagement
    def schedule_appointment(self, patient_id, doctor_id, date, time):
        patient = next((p for p in self.patients if p.patient_id == patient_id),None)
        doctor = next((d for d in self.doctors if d.doctor_id == doctor_id), None)
        if not patient or not doctor:
            st.error("Invalid patient or doctor ID!")
            return False
        appointment = ap.Appointment(patient, doctor, date, time)
        self.appointments.append(appointment)
        st.write(f"\nAppointment scheduled:\n{appointment}")
        return True
    def view_appointments(self):
        st.subheader("\n--- Appointments ---")
        for appointment in self.appointments:
            st.write(appointment)
            st.write("------------------")