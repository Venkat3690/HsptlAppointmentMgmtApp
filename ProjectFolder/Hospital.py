import Appointment as ap
import Patient as pt 
import Doctor as dc

class Hospital:
    def __init__(self,name):
        self.name=name
        self.patient=[]
        self.doctor=[]
        self.appointments=[]
    