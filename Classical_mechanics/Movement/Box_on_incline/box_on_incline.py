import math

class Box_on_incline(object):
        def __init__(self,**kwargs):
                self.attr=['angle','width','height','m','Fg','Fs','Fd','kf','Ff']
                 # attributes of the incline in order: angle,width,height, mass,Fg(gravity force),Fs(statical force), Fd (dynamical force),kf(friction coefficient), Ff(friction force)
                self.data=dict()
                for param in self.attr:
                        self.data[param]=None
                self.given_data=set() #set of data given by user
                self.add_data(**kwargs)

        def add_data(self,**kwargs):
                self.given_data.update(kwargs.keys())
                for i in range(len(self.attr)):
                        param=self.attr[i]
                        if param in kwargs:
                                if i==0 and not (0 <= kwargs['angle'] <= 90) :# atribute is angle
                                        raise ValueError('Angle should be between 0 an 90 degrees')
                                elif i==7 and not (0 <= kwargs[param] <= 1):
                                        raise ValueError('Coefficient (kf) should be between 0 and 1')
                                else:
                                        self.data[param]=kwargs[param]

        def delete_data(self,*args):
                self.__init__()
        def calculate(self,*args):
                pass


