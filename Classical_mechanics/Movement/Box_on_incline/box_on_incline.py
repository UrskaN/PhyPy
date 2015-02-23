import math

class Box_on_incline(object):
        def __init__(self,**kwargs):
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
                string+='\tData not possible to calculate:\n'
                string+=''.join('\t\t{0}={1}\n'.format(param,self.data[param]) for param in self.data if self.data[param] == None)               
                return string

        def add_data(self,**kwargs):
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


        def delete_data(self,*args):
                if args:
                        for param in args:
                                del self.data[param]
                        self.__init__(**self.data)
                else:
                        self.__init__()
        def calculate(self,*args):
                pass


