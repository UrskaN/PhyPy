import unittest
import sys
import os
import math
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../')

from box_on_incline import Box_on_incline

#Box_on_incline(**kwargs):  -->  (angle,height,width)  ,(mass,Fg,Fd,Fs) , (Ff,kf)
#methods:
#-add_data(**kwargs)
#-delete_data(**args)
#-calculate(*args)  --> (we tell it what to calculate, default is everything posible)
#possible methods:
#-position(t)
#-animation
#draw  --> draws forces



class box_on_incline_calculate_test(unittest.TestCase):
        def setUp(self):
                self.incline=Box_on_incline()
                self.attr=self.incline.attr

        def test_incline_calculate_returns_error_for_opossing_arguments(self):
                #TODO check if there is enough cases
                wrong_data=[{'m':1,'Fg':50},{'angle':30,'height':10,'width':1},{'Ff':500,'Fg':1,'kf':1},{'Fs':20,'Fg':10,'angle':5},{'Fd':20,'Fg':10,'angle':5}]
                for data in wrong_data:
                        self.incline.add_data(**data)
                        self.assertRaises(ValueError,self.incline.calculate)
                        self.incline.delete_data()

	        
        def test_incline_calculate_returns_right_value_for_forces(self):
                #TODO create test
                pass




if __name__== '__main__':
    unittest.main()
