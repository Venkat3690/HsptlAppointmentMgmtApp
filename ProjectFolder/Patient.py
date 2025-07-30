class Patient:
    def __init__(self,patient_id,name,age,gender,contact):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.gender=gender
        self.contact=contact
    def __str__(self):
        return (f'ID: {self.patient_id}\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nContact: {self.contact}')
        
