import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../')
#uncomment the folowing line  once file is created
#from box_on_incline import Box_on_incline as Incline

#Box_on_incline(angle,m,k=0,g=9,81)
#arguments :  angle,coefficient,grafity accleration


class box_on_incline_test(unittest.TestCase):
    def test_incline_create_object_returns_error_message_if_no_arguments(self):
        #We try to create obejct without arguments (neded arguments are: angle, m)
        self.assertRaises(TypeError,Incline)
    def test_incline_create_object_returns_error_message_if_angle_not_given(self):
        #We try to create obejct without arguments (neded arguments are: angle, m)
        self.assertRaises(TypeError,Incline,m=5)

    def test_incline_create_object_returns_error_message_if_mass_not_given(self):
        #We try to create obejct without arguments (neded arguments are: angle, m)
        self.assertRaises(TypeError,Incline,2)

    def test_incline_create_object_returns_error_message_if_mass_not_number(self):
        #We try to create obejct without arguments (neded arguments are: angle, m)
        self.assertRaises(TypeError,Incline,m='mass')

    def test_incline_create_object_returns_error_message_if_angle_not_number(self):
        #We try to create obejct without arguments (neded arguments are: angle, m)
        self.assertRaises(TypeError,Incline,'angle')
        self.assertRaises(TypeError,Incline,None)








if __name__== '__main__':
    unittest.main()
