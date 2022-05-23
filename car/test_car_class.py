import car_class
import pytest as pt 
import sys
sys.path.append(".")
from car_class import car 
car1 = car("Ford")
def test_car_initialization(car1): 
    assert car1.__init__
    





