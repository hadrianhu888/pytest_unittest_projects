#car.py class 

import sys 
class car():   
    def __init__(self,name):        
        self.name = name 
        return self        
    def factory(self,make):
        self.make = make
        return make 
    def model_year(self,year): 
        self.year = year
        return year
    def turnOn(self,status):
        self.status = status
        return status
    def speed(self,velocity): 
        self.velocity = velocity
        return velocity
    def powermode(self,vehicle_power_mode):
        self.vehicle_power_mode = vehicle_power_mode
        return vehicle_power_mode
    
