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



class box_on_incline__init_and_add_test(unittest.TestCase):
	def setUp(self):
		self.incline=Box_on_incline()
		self.attr=self.incline.attr

	def test_incline_add_data(self):
		data=self.generate_data()
		self.incline.add_data(**data)
		for param in data:
			self.assertEqual(data[param],self.incline.data[param])
		self.assertEqual(set(self.attr),self.incline.given_data)
				
	def test_incline_overrides_old_data_with_new(self):
		self.incline.add_data(angle=40)
		self.incline.add_data(angle=25)
		self.assertEqual(25,self.incline.data['angle'])


	def test_incline_str_shows_values_right(self):
		data=self.generate_data()
		del data['m']
		del data['angle']
		self.incline.add_data(**data)
		
		correct='Box on incline:\n\tGiven data:\n'
		for param in data:
			correct+='\t\t{0}={1}\n'.format(param,data[param])
		correct+='\tCalculated data:\n'
		correct+='\tData not possible to btain:\n'
		correct+='\t\tm=None\n'
		correct+='\t\tangle=None\n'
		self.assertEqual(self.incline.__str__(),correct)


	def test_incline_rep_shows_values_right(self):
		data=self.generate_data()
		self.incline.add_data(**data)
		correct='Box_on_incline(**{0})'.format(data)
		self.assertEqual(self.incline.__repr__(),correct)

		
	def test_incline_add_returns_error_on_wrong_angle(self):
		self.assertRaises(ValueError,self.incline.add_data,angle=110)
		self.assertRaises(ValueError,self.incline.add_data,angle=-0.5)
		self.assertRaises(ValueError,self.incline.add_data,angle=370)

		
	def test_incline_add_returns_error_on_wrong_kf(self):
		self.assertRaises(ValueError,self.incline.add_data,kf=1.2)
		self.assertRaises(ValueError,self.incline.add_data,kf=-0.2)	

	def generate_data(self):
		#probably should make it a random generator
		data=dict()
		values=[i for i in range(len(self.attr))]
		for i in range(len(self.attr)):
			param=self.attr[i]
			if param == 'kf':
				data[param]=0.5
			else:
				data[param]=values[i]
		return data
		
if __name__== '__main__':
    unittest.main()
