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
                #TODO check if there is enough cases
                def assemble_answer(i):
                        string='Box on incline:\n\tGiven data:\n'
                        string+=''.join('\t\t{0}={1}\n'.format(param,in_data[i][param]) for param in in_data[i])
                        string+='\tCalculated data:\n'
                        string+=''.join('\t\t{0}={1}\n'.format(param,calculated_data[i][param]) for param in calculated_data[i] )
                        string+='\tData not calculated:\n'
                        string+=''.join('\t\t{0}=None\n'.format(param) for param in self.attr if (param not in in_data[i] and param not in calculated_data[i]))         
                        return string           

                in_data=[{},{'m':1,'angle':0,'kf':0.5},{'height':2,'width':2,'Fd':5,'Ff':5}]
                calculated_data=[{},{'Fg':9.81,'Fd':0,'Fs':9.81,'Ff':4.905},{'angle':45,'length':8**(1/2),'Fs':5,'Fg':10/2**(1/2),'m':10/9.81/2**(1/2),'kf':9.81*2**(1/2)/2}]
                for i in range(len(in_data)):
                        self.incline.delete_data()
                        self.incline.add_data(**in_data[i])
                        self.assertEqual(self.incline.calculate(),assemble_answer(i))




if __name__== '__main__':
    unittest.main()
