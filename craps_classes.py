import random

class Die:
	def __init__(self, eyes=6):
		self.eyes = eyes
		
	def throw_die(self):
		result = random.randint(1,self.eyes)
		return result
		
class Player:
	
	players = []
	
	def __init__(self, name, position=0, balance=50):
		self.name = name
		self.balance = balance
		self.position = position
		__class__.players.append(self)
		
	def __repr__(self):
		return self.name
		
	def positioning(self, other):
		x = random.randint(1,2)
		self.position = 1 if x == 1 else 2
		other.position = 1 if x == 2 else 2
		if self.position == 1:
			shooter = self
		else:
			shooter = other
		return shooter
				
	
		

