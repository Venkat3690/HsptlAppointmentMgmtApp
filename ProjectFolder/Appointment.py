class Appointment:
    def __init__(self,patient,doctor,date,time):
        self.patient=patient
        self.doctor=doctor
        self.date=date
        self.time=time
    def __str__(self):
        return (f'Appointment: {self.date} at {self.time}\nPatient: {self.patient}\nDoctor: Dr. {self.doctor}')