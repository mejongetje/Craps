import random
import craps_classes as cc
import text as tx

registry = {
					1: tx.func1,
					2: tx.func2,
					3: tx.func3,
					4: tx.func4,
					5: tx.func5,
					6: tx.func6,
					7: tx.func7,
					8: tx.func8,
					9: tx.func9,
					10: tx.func10,
					11: tx.func11,
					12: tx.func12,
					13: tx.func13,
					14: tx.func14,
					15: tx.func15,
					16: tx.func16
		}

class MyGame:
	def __init__(self, game=0, pot=0, point_roll=0):
		self.game = game
		self.pot = pot
		self.point_roll = point_roll
		
	def next_round(self):
		self.game += 1
		return self.game

	def bet_depo(self, shooter, other):
		self.pot += 10
		shooter.balance -= 5
		other.balance -= 5

	def settle_bet(self, shooter, other, win=True):
		if win == True:
			shooter.balance += self.pot
		else:
			other.balance += self.pot 
		self.pot = 0
		
	def double_offer(self, shooter, other):
		registry[1](shooter)
		double = input('Type y if you accept, else n: ')
		if double == 'y':
			registry[2](other)
			self.bet_depo(shooter, other)
			registry[3](self.pot)
		else:
			pass
		
	def play(self):

		d1 = cc.Die()
		d2 = cc.Die()
		print('=====================================================')
		print('          Welcome to STREET CRAPS 2000')
		print('=====================================================\n')

		cp1 = cc.Player('Frankie Five Stars')
		cp2 = cc.Player('Uncle Lou')
		cp3 = cc.Player('Billy the Hat')
		cp4 = cc.Player('Alice Capone')

		cp = random.choice([cp1,cp2,cp3,cp4])

		print('So you have the balls to take on four of the greatest')
		print('street craps hustlers in  New York City? Notorious men')
		print('with names like Frankie Five Stars, Uncle Lou, Billy the Hat')
		print('and Ace Capone? You got some nerve son...\n')

		hpname = input("What was your name again? ")

		hp = cc.Player(hpname)
		print(f'Welcome {hp}\n')

		while True:
	#print(f'Game: {game}')
	
			rolls = 0
			game = self.next_round()
			print(f'\nGame: {game}')
			print('----------\n')
			print(f'{hp.name} has ${hp.balance:.2f}')
			print(f'{cp.name} has ${cp.balance:.2f}\n')
	
			print('===========================================')
	
			print('---------- SHOOTER\'s BET ----------')
			# Who is the shooter?
			if game == 1:
				shooter = hp.positioning(cp)

			registry[4](shooter)
			other = hp if shooter == cp else cp
			
			registry[5](shooter)
			self.bet_depo(shooter, other)

			if shooter == hp:
				registry[6]()
				shooter_bet = int(input('Type 1 for Pass or 2 for Don t Pass: '))
				if shooter_bet == 1:
					registry[7](hp)
				else:
					registry[8](hp)
			else:
				shooter_bet = random.randint(1,2)
				if shooter_bet == 1:
					registry[7](cp)
				else:
					registry[8](cp)
			
			print('============================================')
			print('-------------- COMING OUT ---------------\n')
			print(f'Time to roll some dice {shooter}!')
			t_conf = input('Type y to continue or n to stop: ')
			if t_conf == 'y':
				t1 = d1.throw_die()
				t2 = d2.throw_die()
				print('\n')
				print(f'dice 1: {t1}, dice 2: {t2}\n')
				print('===========================================')
				print('===========================================')
				print(f'       The Point is: {t1 + t2}')
				print('===========================================')
				print('===========================================\n')
			else:
				print('no score')
	
			point = t1 + t2
			if point == 7 or point == 11:
				if shooter_bet == 1:
					registry[9](shooter)
					self.settle_bet(shooter, other, win=True)
				else:
					registry[10](shooter)	
					self.settle_bet(shooter, other, win=False)
			elif point == 2 or point == 3 or point == 12:
				if shooter_bet == 1:
					registry[10](shooter)
					self.settle_bet(shooter, other, win=False)
				else:
					registry[9](shooter)	
					self.settle_bet(shooter, other, win=True)		
			else:
				print('--------- DOUBLE THE BETS ------------')
				if shooter == hp:
					double = input('Type y if you want to double the bets, else n: ')
					if double == 'y':
						registry[11](cp)
						self.bet_depo(shooter, other)
						registry[12](self.pot)
					else:
						pass
				if shooter == cp and shooter_bet == 1:
					if point == 6 or point == 8:
						self.double_offer(shooter, other)
					else:
						pass
				if shooter == cp and shooter_bet == 2:
					if point == 4 or point == 10:
						self.double_offer(shooter, other)
					else:
						pass
						
				print('=============================================')
				print('------------ MAKING THE POINT -------------\n')
				registry[13](point,shooter)
				while True:
					registry[14](rolls)
					rolls += 1
					conf = input('Roll the dice! ')
					if conf == "y":
						t3 = d1.throw_die()
						t4 = d2.throw_die()
						roll = t3 + t4
						registry[15](t3, t4, roll)
						if roll == 7:
							if shooter_bet == 1:
								registry[10](shooter)
								self.settle_bet(shooter, other, win=False)
								shooter = hp if shooter == cp else cp
							else:
								registry[9](shooter)
								self.settle_bet(shooter, other, win=True)	
								print('\n')
							registry[16](rolls)
							break
						elif roll == point:
							if shooter_bet == 1:
								registry[9](shooter)
								self.settle_bet(shooter, other, win=True)
							else:
								registry[10](shooter)
								self.settle_bet(shooter, other, win=False)
								shooter = hp if shooter == cp else cp
								print('\n')
							registry[16](rolls)
							break
						else:
							pass
					
					print('\n')
