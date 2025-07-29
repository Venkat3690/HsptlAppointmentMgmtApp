import streamlit as st
import Appointment as ap
import Patient as pt
import Doctor as dc
import Hospital as hspt

# Create the hospital object once
if 'hospital' not in st.session_state:
    st.session_state.hospital = hspt.Hospital("Cyno High Speciality Hostital")

hospital = st.session_state.hospital

st.title("Hospital Appointment Management System")

st.sidebar.header("Navigation")
options = st.sidebar.radio("Select an action", [
    "Add Patient", "Add Doctor", "View Patients", "View Doctors",
    "Schedule Appointment", "View Appointments"
])

# Add a new patient
if options == "Add Patient":
    st.subheader("➕ Add New Patient")
    pid = st.text_input("Patient ID")
    pname = st.text_input("Name")
    page = st.number_input("Age", min_value=0, max_value=120)
    pgender = st.selectbox("Gender", ["Male", "Female", "Other"])
    pcontact = st.text_input("Contact Number")
    if st.button("Add Patient"):
        if pid and pname and pcontact:
            new_patient = pt.Patient(pid, pname, page, pgender, pcontact)
            hospital.add_patient(new_patient)
            st.success("Patient added successfully!")
        else:
            st.error("Please fill all required fields.")

# Add a new doctor
elif options == "Add Doctor":
    st.subheader("➕ Add New Doctor")
    did = st.text_input("Doctor ID")
    dname = st.text_input("Name")
    specialization = st.text_input("Specialization")
    if st.button("Add Doctor"):
        if did and dname and specialization:
            new_doctor = dc.Doctor(did, dname, specialization)
            hospital.add_doctor(new_doctor)
            st.success("Doctor added successfully!")
        else:
            st.error("Please fill all required fields.")

# View all patients
elif options == "View Patients":
    st.subheader("📋 List of Patients")
    patients = hospital.display_patients()
    if patients:
        for p in patients:
            st.write(f"**ID:** {p.patient_id}, **Name:** {p.name}, **Age:** {p.age}, **Gender:** {p.gender}, **Contact:** {p.contact}")
    else:
        st.info("No patients added yet.")

# View all doctors
elif options == "View Doctors":
    st.subheader("📋 List of Doctors")
    doctors = hospital.display_doctors()
    if doctors:
        for d in doctors:
            st.write(f"**ID:** {d.doctor_id}, **Name:** {d.name}, **Specialization:** {d.specialization}")
    else:
        st.info("No doctors added yet.")

# Schedule an appointment
elif options == "Schedule Appointment":
    st.subheader("📅 Schedule Appointment")
    patient_id = st.text_input("Patient ID")
    doctor_id = st.text_input("Doctor ID")
    date = st.date_input("Date")
    time = st.time_input("Time")
    if st.button("Schedule"):
        if patient_id and doctor_id:
            hospital.schedule_appointment(patient_id, doctor_id, str(date), str(time))
            st.success("Appointment scheduled successfully!")
        else:
            st.error("Please enter both Patient ID and Doctor ID.")

# View all appointments
elif options == "View Appointments":
    st.subheader("📅 All Appointments")
    appointments = hospital.view_appointments()
    if appointments:
        for appt in appointments:
            st.write(f"**Patient:** {appt.patient.name}, **Doctor:** {appt.doctor.name}, **Date:** {appt.date}, **Time:** {appt.time}")
    else:
        st.info("No appointments scheduled yet.")
