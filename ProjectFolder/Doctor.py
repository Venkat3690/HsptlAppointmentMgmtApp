class Doctor:
    def __init__(self,doctor_id,name,specialization):
        self.doctor_id=doctor_id
        self.name=name
        self.specialization=specialization
    def __str__(self):
        return (f'ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}')