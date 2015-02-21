import math

class Box_on_incline(object):
	def __init__(self,**kwargs):
		self.angle=None
		self.width=None
		self.height=None
		
		self.m=None
		self.Fg=None
		self.Fd=None
		
		self.ktr=None
		self.Ftr=None

		self.add_data(**kwargs)

	def add_data(self,**kwargs):
		self.angle=kwargs['angle'] if 'angle' in kwargs else self.angle
		self.width=kwargs['width'] if 'width' in kwargs else self.width
		self.height=kwargs['height'] if 'height' in kwargs else self.height

		self.m=kwargs['m'] if 'm' in kwargs else self.m
		self.Fg=kwargs['Fg'] if 'Fg' in kwargs else self.Fg
		self.Fd=kwargs['Fd'] if 'Fd' in kwargs else self.Fd

		self.ktr=kwargs['ktr'] if 'ktr' in kwargs else self.ktr
		self.Ftr=kwargs['Ftr'] if 'Ftr' in kwargs else self.Ftr


	def delete_data(self,args):
		pass
	def calculate(self,args):
		pass
