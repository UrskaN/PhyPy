import unittest
import sys
import os
import math
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../')
#uncomment the folowing line  once file is created
#from box_on_incline import Box_on_incline as Incline

#Box_on_incline(**kwargs):  -->  (angle,height,width)  ,(mass,Fg,Fd,Fs) , (Ftr,ktr)
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
	def test_incline_add_data(self):
    		#We try to add data to object
		incline.add(m=1,angle=30)
	        self.assertEqual(1,incline.m)
		self.assertEqual(30,incline.angle)
	def test_incline_overrides_old_data_with_new(self):
		incline.add(angle=25)
		self.assertEqual(25,incline.angle)
	def test_incline.add_returns_error_on_wrong_angle(self):
	         self.assertRaises(ValueError,incline.add,angle=110)
	def test_incline.add_returns_error_on_to_big_ktr(self):
		self.assertRaises(ValueError,incline.add,ktr=1.2)
	def test_incline.add_returns_error_on_negative_ktr(self):
		self.assertRaises(ValueError,incline.add,ktr=-0.2)
	def test_incline.delete_deletes_all_data_when_called_without_args(self):
		incline.data()
		self.assertEqual(None,incline.m)
		self.assertEqual(None,incline.angle)
		#TODO check that all of variables are none
	def test_incline.calculate_returns_error_for_opossing_arguments(self):
		incline.add(m=1,angle=30,height=10,width=1)#angle should be around 84
		self.assertRaises(ValueError,incline.calculate)
		#TODO check for other cases
	def test_incline.calculate_returns_right_value_for_forces(self):
		incline.delete()
		incline.add(m=1,angle=30)
		incline.calculate()
		self.assertEqual(9.81,incline.fg)
		self.assertEqual(9.81/2,fd)
		self.assertEqual(9.81*math.sqrt(3)/2,incline.fs)
		





if __name__== '__main__':
    unittest.main()
