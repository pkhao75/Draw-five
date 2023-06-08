# Draw Five

import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['\u2663', '\u2666', '\u2665', '\u2660']
rflush = ['10\u2660', 'J\u2660', 'Q\u2660', 'K\u2660', 'A\u2660']
betvalue = {1:10, 2:25, 3:50, 4:100, 5:250, 6:500}
actcheck1 = ['b','x', 'f', 'h']
actcheck2 = ['r', 'c', 'f', 'h']
actcheck3 = ['c', 'f', 'h']
line = '=' * 60

#Function to Print card picture
def print_cards(hand):
	line_set = ['┌───────┐' * 5, '', '│       │' * 5, '', '│       │' * 5, '', '└───────┘' * 5]
	for card in hand:
		if len(card[:-1]) == 1: 
			temp = ' '
		else:
			temp = ''
		line_set[3] += '│   {}   │'.format(card[-1])
		line_set[1] += '│{}{}     │'.format(card[:-1], temp)
		line_set[5] += '│     {}{}│'.format(temp, card[:-1])
	for line in line_set:
		print(line)


# Player Class

class Player:
	def __init__(self, inname, inno, inmoney = 3000):
		self.name = inname
		self.money = inmoney
		self.playernum = inno
		self.bet = 0
		self.bettot = 0
		self.hand = []
		self.lose = False
		self.fold = False

	def __repr__(self):
		return self.name

	def show_info(self):
		print('Money: $' + str(self.money))
		print('My Bet: $' + str(self.bettot))

	def show_hand(self):
		print_cards(self.hand)
		input('Enter any key to proceed and hide cards:')
		print('\n' * 100)

	def sort_hand(self):
		self.hand.sort(key = lambda c: (cards.index(c[:-1]), suits.index(c[-1])))


class DrawFive:

	#Show Bet Pool
	def show_pool(self):
		print('Current Round Bet: {}'.format(betvalue[self.bet_size]))
		print('Bet Pool: {}'.format(self.pool))

	#making Deck every new round
	def deck_shuffle(self):
		self.deck = []
		for suit in suits:
			for card in cards:
				self.deck.append(card+suit) 
		random.shuffle(self.deck)

	#Deal new cards
	def card_dealt(self):
		self.deck_shuffle()
		#print(self.deck)
		for i in range(5):
			for player in self.player:
				if player.lose == False and len(player.hand) <= 5:
					player.hand.append(self.deck.pop(0))
		for player in self.player: player.sort_hand()


	#Draw cards
	#def card_draw(self):

	#Bet
	def play_bet(self, player):
		player.bet = betvalue[self.bet_size]
		player.bettot += betvalue[self.bet_size]
		print('{} Bet Money'.format(player))
		print(player.bet)
		self.pool += betvalue[self.bet_size]
		player.money -= betvalue[self.bet_size]

	#Raise
	def play_raise(self, player):
		self.bet_size += 1
		player.bet = betvalue[self.bet_size]
		player.bettot += betvalue[self.bet_size]
		print('{} Raise Bet Money'.format(player))
		print(player.bet)
		self.pool += betvalue[self.bet_size]
		player.money -= betvalue[self.bet_size]

	#Call
	def play_call(self, player):
		player.bet = betvalue[self.bet_size]
		player.bettot += betvalue[self.bet_size]
		print('{} Call Bet'.format(player))
		print(player.bet)
		self.pool += betvalue[self.bet_size]
		player.money -= betvalue[self.bet_size]


	#Define which action to do
	def action(self, act):
		pass
	#Check for losing player(money less than 20)
	def check_out(self, player):
		if player.lose == False:
			if player.money < 20:
				player.lose = True
		print('Player {}, {}'.format(player, player.lose))

	#Check for winner(All other 3 players lose)
	def check_win(self):
		count = 0
		for player in self.player:
			if player.lose == True:
				count += 1
		if count == 3:
			self.game_over = True
			print("Game Over")
			for player in self.player:
				if player.lose == False:
					print('{} is the winner!'.format(player))


	#Round One
	def round_one(self):
		check = 0
		fold = 0
		self.bet_size = 1
		proceed = False
		while check+fold < 4:
			for player in self.player:
				if proceed == False:
					action = 0
					if player.fold == False:
						while(True):	
							print(line)
							print('\n\n{}\'s turn'.format(player))
							print(line)
							player.show_info()
							self.show_pool()
							#print('Hand:')
							#print(player.hand)
							print(line)
							if check == 0 and self.bet_size < 6:
								while action not in actcheck1:
									action = input('Select action(b = bet, x = check, f = fold, h = hand):')
									if action not in actcheck1: print('Wrong command, try again')
							elif check > 0 and self.bet_size < 6:
								while action not in actcheck2:
									action = input('Select action(r = raise, c = call, f = fold, h = hand):')
									if action not in actcheck2: print('Wrong command, try again')
							else:
								while action not in actcheck3:
									action = input('Select action(c = call, f = fold, h = hand):')
									if action not in actcheck2: print('Wrong command, try again')	
							if action == 'h': 
								player.show_hand()
								action = 0
							else: break

						#print(action)
						if action == 'b':
							self.play_bet(player)
							check = 1
						elif action == 'r':
							self.play_raise(player)
							check = 1
						elif action == 'c':
							self.play_call(player)
							check += 1
						elif action == 'x':
							print('Check')
							check += 1
						else:
							print('Fold')
							if check == 0: check = 1
							fold += 1
							player.fold = True
				if check+fold == 4:
					proceed = True
					

	#Main gameplay code
	def game_play(self):
			self.game_num += 1
			self.pool = 0
			print('Game {}: '.format(self.game_num))
			for player in self.player:
				player.fold == False
			self.card_dealt()
			self.round_one()



			for player in self.player:
				self.check_out(player)
			self.check_win()


						

	def __init__(self):
		print(line)
		print('Welcome to Five-Card Draw!')
		print_cards(rflush)
		print(line)
		print('Please enter each players name:')
		self.p1 = Player(input('Enter player1 name: '), 1)
		self.p2 = Player(input('Enter player2 name: '), 2)
		self.p3 = Player(input('Enter player3 name: '), 3)
		self.p4 = Player(input('Enter player4 name: '), 4)
		self.game_over = False
		self.game_num = 0
		self.bet_size = 1
		self.player = []
		self.player.append(self.p1)
		self.player.append(self.p2)
		self.player.append(self.p3)
		self.player.append(self.p4)
		print(self.player)
		#while(self.game_over == False):
		self.game_play()

DrawFive()