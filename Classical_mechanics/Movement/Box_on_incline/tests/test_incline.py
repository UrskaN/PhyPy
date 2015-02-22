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



class box_on_incline_test(unittest.TestCase):
        def setUp(self):
                self.incline=Box_on_incline()
                self.attr=self.incline.attr
        def test_incline_add_data(self):
    		#We try to add data to object
                self.incline.add_data(m=1,angle=30)
                self.assertEqual(1,self.incline.data['m'])
                self.assertEqual(30,self.incline.data['angle'])
        def test_incline_overrides_old_data_with_new(self):
                self.incline.add_data(angle=25)
                self.assertEqual(25,self.incline.data['angle'])
        def test_incline_add_returns_error_on_wrong_angle(self):
        	self.assertRaises(ValueError,self.incline.add_data,angle=110)
        def test_incline_add_returns_error_on_to_big_kf(self):
                self.assertRaises(ValueError,self.incline.add_data,kf=1.2)
        def test_incline_add_returns_error_on_negative_kf(self):
                self.assertRaises(ValueError,self.incline.add_data,kf=-0.2)
        def test_incline_delete_deletes_all_data_when_called_without_args(self):
                self.incline.add_data(m=1,angle=4,height=4,Fg=9.81,width=4,kf=0,Ff=3)
                self.incline.delete_data()
                for param in self.attr:
	                self.assertEqual(None,self.incline.data[param])

        def test_incline_calculate_returns_error_for_opossing_arguments(self):
                self.incline.add_data(m=1,angle=30,height=10,width=1)#angle should be around 84
                self.assertRaises(ValueError,self.incline.calculate)
		#TODO check for other cases
        def test_incline_calculate_returns_right_value_for_forces(self):
                self.incline.delete_data()
                self.incline.add_data(m=1,angle=30)
                self.incline.calculate()
                self.assertEqual(9.81,self.incline.data['Fg'])
                self.assertEqual(9.81/2,self.incline.data['Fd'])
                self.assertEqual(9.81*math.sqrt(3)/2,self.incline.data['Fs'])






if __name__== '__main__':
    unittest.main()
