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



class box_on_incline_delete_test(unittest.TestCase):
        def setUp(self):
                self.incline=Box_on_incline()
                self.attr=self.incline.attr
       
        def test_incline_delete_deletes_all_data_when_called_without_args(self):
                #first we generate data
                self.generate_data()
                #now we delete it:
                self.incline.delete_data()
                for param in self.attr:
	                self.assertEqual(None,self.incline.data[param])
                self.assertEqual(set(),self.incline.given_data)

        def test_incline_delete_deletes_only_param_which_we_call(self):
                self.generate_data()
                self.incline.delete_data('m','angle')
                self.assertEqual(None,self.incline.data['m'])
                self.assertEqual(None,self.incline.data['angle'])
                attr=list(self.attr)
                attr.remove('m')
                attr.remove('angle')
                self.assertEqual(set(attr),self.incline.given_data)

        def generate_data(self):
                data=dict()
                values=[i for i in range(len(self.attr))]
                for i in range(len(self.attr)):
                        param=self.attr[i]
                        if param == 'kf':
                                data[param]=0.5
                        else:
                                data[param]=values[i]
                self.incline.add_data(**data)
                return data
                





if __name__== '__main__':
    unittest.main()
