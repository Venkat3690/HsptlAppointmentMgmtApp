class Appointment:
    def __init__(self,patient,doctor,date,time):
        self.patient=patient
        self.doctor=doctor
        self.date=date
        self.time=time
    def __str__(self):
        return (f'Appointment scheduled on {self.date} at {self.time} for {self.patient} assigned to {self.doctor}')