# This is the file where I'll write the code

import numpy as np

class Particle():
	def __init__(self,r=np.zeros(3),m=0,q=0,v=np.zeros(3)):
		self.r = r
		self.v = v
		self.a = np.zeros(3)
		self.m = m
		self.q = q
		if np.all(self.v==0):
			self.isFixed = True
		else:
			self.isFixed = False

class Cloud():
	def __init__(self,c=np.zeros(3),q=0,rad=1):
		self.center = c
		self.q = q
		self.radius = rad

class Shell():
	def __init__(self,c=np.zeros(3),r=0):
		self.center = c
		self.radius = r

class Atom():
	def __init__(self,r=np.zeros(3),m=0,q=0):
		self.core = Particle(r,m,q)
		self.electrons = Cloud(r,q)

	def move(dr):
		self.core.r += dr
		self.electrons.center += dr

class Plate():
	def __init__(self,A=1,dim=[10,100,0],n=100):
		self.A = A
		self.dim = dim
		self.atoms = 

#	def resize(self,dim):		


class Universe():
	G = 1
	K = 1
	def __init__(self):
		self.projectiles = []
		self.plate = Plate();
		self.wrapper = Wrapper(100)