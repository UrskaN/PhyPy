import math

class Box_on_incline(object):
	def __init__(self,**kwargs):
		self.angle=None
		self.width=None
		self.height=None
		
		self.m=None
		self.Fg=None
		self.Fd=None
		
		self.kf=None
		self.Ff=None

		self.given_data=set()
		self.add_data(**kwargs)

	def add_data(self,**kwargs):
		self.given_data.update(kwargs.keys())
		if 'angle' in kwargs:
			if 0 <= kwargs['angle'] <= 90 :
				self.angle=kwargs['angle']
			else:
				raise ValueError('Angle should be between 0 an 90 degrees')
		self.width=kwargs['width'] if 'width' in kwargs else self.width
		self.height=kwargs['height'] if 'height' in kwargs else self.height

		self.m=kwargs['m'] if 'm' in kwargs else self.m
		self.Fg=kwargs['Fg'] if 'Fg' in kwargs else self.Fg
		self.Fd=kwargs['Fd'] if 'Fd' in kwargs else self.Fd
		
		if 'kf' in kwargs:
			if 0 <= kwargs['kf'] <= 1:
				self.kf=kwargs['kf']
			else:
				raise ValueError('Coefficient (kf) should be between 0 and 1')
		self.Ff=kwargs['Ff'] if 'Ff' in kwargs else self.Ff


	def delete_data(self,*args):
		pass
	def calculate(self,*args):
		pass
	
	def check_data(self,*args):
		pass
