import math

class Box_on_incline(object):
        """Box_on_incline(kwags) - object with methods for solving physics problem of a box on incline

        Kwargs:
                m  (> 0) - Mass of a box                [kg]
                Fg (> 0) - Gravity force on the box     [N]
                Fd (>= 0) - Dynamical force on the box (parallel to incline)    [N]
                Fs (>= 0) - Statical force on the box (perpendicular to incline)        [N]
                
                angle (> 0= && <= 90) - Angle of the incline    [degrees]
                height (> 0) - Height of the incline [m]
                width  (> 0) - Width of the incline  [m]
                length (> 0) - Length of the incline [m]

                kf (> 0 && <1 ) -Coefficient of friction [No unit]
                Ff (>= 0) - Friction force on the box(opposite to dynamical force) [N]

        Example:
                Box_on_incline(m=1, Fg=9.81 , Fd=0 , Fs=9.81 , angle=0, height=0, width=10, length= 10, kf=0.5 , Ff=4.905)
       
                To see currently saved data use print(object_name) where object_name is name of the variable in which Box_on_incline has been initialized, or use  method check_data
        
        """
        def __init__(self,**kwargs):
                """Initializes Box_on_incline. For kwargs see help(Box_on_incline)"""
                self.attr = ['angle','width','height','m','Fg','Fs','Fd','kf','Ff']
                 # attributes of the incline in order: angle,width,height, mass,Fg(gravity force),Fs(statical force), Fd (dynamical force),kf(friction coefficient), Ff(friction force)
                self.data = {param: None for param in self.attr}#initialazing data
                self.given_data = set() #set of data given by user
                self.add_data(**kwargs)

        def __repr__(self):
                return 'Box_on_incline(**{0})'.format(self.data)
        
        def __str__(self):
                string='Box on incline:\n\tGiven data:\n'
                string+=''.join('\t\t{0}={1}\n'.format(param,self.data[param]) for param in self.given_data)
                string+='\tCalculated data:\n'
                string+=''.join('\t\t{0}={1}\n'.format(param,self.data[param]) for param in self.data if (param not in self.given_data and self.data[param] != None ))
                string+='\tData not calculated:\n'
                string+=''.join('\t\t{0}={1}\n'.format(param,self.data[param]) for param in self.data if self.data[param] == None)               
                return string

        def add_data(self,**kwargs):
                """Adds data to Box_on_incline object. For kwargs see help(Box_on_incline)"""
                self.given_data.update([x for x in kwargs.keys()  if kwargs[x]!=None ])
                for i in range(len(self.attr)):
                        param=self.attr[i]
                        if param in kwargs and kwargs[param]!=None:
                                if i==0 and not (0 <= kwargs['angle'] <= 90) :# atribute is angle
                                        raise ValueError('Angle should be between 0 an 90 degrees')
                                elif i==7 and not (0 <= kwargs[param] <= 1):
                                        raise ValueError('Coefficient (kf) should be between 0 and 1')
                                else:
                                        self.data[param]=kwargs[param]
                print('Added data to object. See current data by using print(object_name) or  using check_data method')


        def delete_data(self,*args):
                """ Deletes data from Box_on_incline object.
                
                if no args: deletes all data
                otherwise deletes data given in args
                args: 'm','Fg','Fd','Fs','angle','height','length','width','kf','Ff'
                """
                if args:
                        for param in args:
                                del self.data[param]
                        self.__init__(**self.data)
                else:
                        self.__init__()
                print('Deleted data. See current data by using print(object_name) or  using check_data method')

        def calculate(self,*args):
                """ Calculates data from data given by user
                
                if no args: calculates all possible data
                otherwise calculates data given in args if possible
                args: 'm','Fg','Fd','Fs','angle','height','length','width','kf','Ff'

                """
                pass

        def check_data(self):
                """Prints current data"""
                print(self.__str__())

