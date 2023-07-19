# Draw Five

import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['\u2663', '\u2666', '\u2665', '\u2660']
rflush = ['10\u2660', 'J\u2660', 'Q\u2660', 'K\u2660', 'A\u2660']
card_value = {i: c for c, i in enumerate(cards)}
betvalue = {1:10, 2:25, 3:50, 4:100, 5:250, 6:500}
actcheck1 = ['b','x', 'f', 'h']
actcheck2 = ['r', 'c', 'f', 'h']
actcheck3 = ['c', 'f', 'h']
line = '=' * 60
indx = list(range(5))
win_dict = {1: 'High Card', 5:'One Pair', 9:'Two Pair', 10: 'Three of a kind', 11: 'Straight', 12: 'Flush', 14: 'Full House', 15: 'Four of a Kind', 22: 'Straight Flush', 23: 'Royal Flush'}

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

#Solve Tie
def solve_draw(players, draw_point):
		draw = 0
		hand_nums = []
		#hand_suits = []
		draw_index = []
		winner_index = 0
		for player in players:
			draw_index.append(players.index(player))
			temp_num = []
			for card in player.hand:
				temp_num.append(card[:-1])
			hand_nums.append(temp_num)
		#High
		if draw_point == 1:
			for i in range(5):
				draw = 0
				for j in range(len(players)-1):
					hand_a = card_value[hand_nums[winner_index][4-i]]
					hand_b = card_value[hand_nums[j+1][4-i]]
					if hand_a < hand_b:
						winner_index = j+1
						draw_index[j] = 'x'
						draw = 0
					elif hand_a == hand_b:
						draw += 1 
					else:
						if i == 4:
							draw_index.remove(j+1)
				if draw == 0: 
					break
		#one_pair
		elif draw_point == 5:
			pair_card = []
			for hand in hand_nums:
				for card in hand:
					if hand.count(card) == 2:
						pair_card.append(card_value[card])
						hand.remove(card)
						hand.remove(card)
						break
			max_value = max(pair_card)
			if pair_card.count(max_value) == 1:
				winner_index = pair_card.index(max_value)
			else:
				for i in draw_index:
					if pair_card[i] != max_value: draw_index.remove(i)
				winner_index = draw_index[0]
				for i in range(3):
					draw = 0
					for j in range(len(draw_index)-1):
						hand_a = card_value[hand_nums[winner_index][2-i]]
						hand_b = card_value[hand_nums[draw_index[j+1]][2-i]]
						if hand_a < hand_b:
							winner_index = draw_index[j+1]
							draw_index[j] = 'x'
							draw = 0
						elif hand_a == hand_b:
							draw += 1 
						else:
							if i == 2:
								draw_index[j+1] = 'x'
					if draw == 0: 
						break
		#two_pair
		elif draw_point == 9:
			pair_high = []
			pair_low = []
			for hand in hand_nums:
				temp = []
				for card in hand:
					if hand.count(card) == 2:
						temp.append(card_value[card])
						hand.remove(card)
						hand.remove(card)
				pair_high.append(temp[1])
				pair_low.append(temp[0])
			print(pair_high)
			print(pair_low)
			print(hand_nums)
			max_value = max(pair_high)
			if pair_high.count(max_value) == 1:
				winner_index = pair_high.index(max_value)
			else:
				for i in draw_index:
					if pair_high[i] != max_value: 
						pair_low[i] = -1
				max_value = max(pair_low)
				if pair_low.count(max_value) == 1:
					winner_index = pair_low.index(max_value)
				else:
					for i in draw_index:
						if pair_low[i] != max_value: 
							draw_index.remove(i)	
					winner_index = draw_index[0]
					draw = 0
					for j in range(len(draw_index)-1):
						hand_a = card_value[hand_nums[winner_index][0]]
						hand_b = card_value[hand_nums[draw_index[j+1]][0]]
						if hand_a < hand_b:
							winner_index = draw_index[j+1]
							draw_index[j] = 'x'
							draw = 0
						elif hand_a == hand_b:
							draw += 1 
						else:
							draw_index[j+1] = 'x'
		#three_kind
		elif draw_point == 10:
			three_card = []
			for hand in hand_nums:
				for card in hand:
					if hand.count(card) == 3:
						three_card.append(card_value[card])
						hand.remove(card)
						hand.remove(card)
						hand.remove(card)
						break
			max_value = max(three_card)
			winner_index = three_card.index(max_value)
		#straight
		elif draw_point == 11:
			for j in range(len(draw_index)-1):
				hand_a = card_value[hand_nums[winner_index][4]]
				hand_b = card_value[hand_nums[draw_index[j+1]][4]]
				if hand_a < hand_b:
					winner_index = draw_index[j+1]
					draw_index[j] = 'x'
					draw = 0
				elif hand_a == hand_b:
					draw += 1 
				else:
					draw_index[j+1] = 'x'
		#flush
		elif draw_point == 12:
			for j in range(len(draw_index)-1):
				hand_a = card_value[hand_nums[winner_index][4]]
				hand_b = card_value[hand_nums[draw_index[j+1]][4]]
				if hand_a < hand_b:
					winner_index = draw_index[j+1]
					draw_index[j] = 'x'
					draw = 0
				elif hand_a == hand_b:
					draw += 1 
				else:
					draw_index[j+1] = 'x'
		#full_house
		elif draw_point == 14:
			three_card = []
			for hand in hand_nums:
				for card in hand:
					if hand.count(card) == 3:
						three_card.append(card_value[card])
						break
			max_value = max(three_card)
			winner_index = three_card.index(max_value)
		#Four_pair
		elif draw_point == 15:
			four_card = []
			for hand in hand_nums:
				for card in hand:
					if hand.count(card) == 4:
						four_card.append(card_value[card])
						break
			max_value = max(four_card)
			winner_index = four_card.index(max_value)
		#Straight_Flush
		elif draw_point == 22:
			for j in range(len(draw_index)-1):
				hand_a = card_value[hand_nums[winner_index][4]]
				hand_b = card_value[hand_nums[draw_index[j+1]][4]]
				if hand_a < hand_b:
					winner_index = draw_index[j+1]
					draw_index[j] = 'x'
					draw = 0
				elif hand_a == hand_b:
					draw += 1 
				else:
					draw_index[j+1] = 'x'
		#R Flush is draw
		if draw == 0: return winner_index, 0
		else:
			xcount = draw_index.count('x')
			if xcount > 1:
				xind = draw_index.index('x')
				if xind == 1: draw_index.remove(0)
			while xcount > 0:
				draw_index.remove('x')
				xcount -= 1 
			return draw_index, 1


# Player Class

class Player:
	def __init__(self, inname, inno, inmoney = 2000):
		self.name = inname
		self.money = inmoney
		self.playernum = inno
		self.bet = 0
		self.bettot = 0
		self.hand = []
		self.lose = False
		self.fold = False
		self.points = 0

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
		for i in range(5):
			for player in self.player:
				if player.lose == False and len(player.hand) < 5:
					player.hand.append(self.deck.pop(0))
		for player in self.player: player.sort_hand()


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


	#Check for losing player(money less than 20)
	def check_out(self, player):
		if player.lose == False:
			if player.money < 20:
				player.lose = True
		print('Player {}, {}'.format(player, player.lose))

	#Check for winner(All other 3 players lose)
	def check_game(self):
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
					return False
		return True

	#Calculate points from hand
	def cal_pts(self, hand):
		pts = 1
		nums = []
		suits = []
		for card in hand:
			nums.append(card[:-1])
			suits.append(card[-1])
		#Check for 2/3/4 kind
		for item in nums:
			if nums.count(item) == 2:
				pts += 2
			elif nums.count(item) == 4:
				pts += 14
				break	
			if nums.count(item) == 3: 
				pts += 3
		#Check Straight
		if pts == 1:
			count = 0
			for i in range(4):
				if card_value[nums[i+1]] - card_value[nums[i]] == 1: count += 1
			if card_value[nums[4]] - card_value[nums[0]] == 12: count +=1
			if count == 4: pts += 10
		#Check Flush
			if suits.count(suits[0]) == 5: pts += 11
		if pts == 22:
			if nums[0] == '10' and nums[4] == 'A': pts += 1
		return pts

	#Check for winner
	def check_win(self, checker):
		win_points = 0
		win_name = ''
		draw = 0
		draw_set = []
		for player in checker:
			player.points = self.cal_pts(player.hand) 
			if player.points > win_points: 
				win_points = player.points
				win_name = player
				draw = 0
				draw_set = []
			elif player.points == win_points:
				draw += 1
				draw_set.append(player)
		if draw > 0: 
			win_ind, win_cond = solve_draw(draw_set, win_points)

		print('\n' * 10 + line)
		print('This game winner is \"{}\" with {}, taking a total of ${}!!!'.format(win_name, win_dict[win_points], self.pool))
		win_name.money += self.pool

	#Round One
	def round_one(self):
		check = 0
		fold = 0
		for player in self.player:
			if player.lose == True:
				player.fold = True
			if player.fold == True:
				fold += 1
		self.bet_size = 1
		proceed = False
		while check+fold < 4 and fold < 3:
			for player in self.player:
				if proceed == False:
					action = 0
					if player.fold == False:
						while(True):	
							print('{}\'s turn'.format(player))
							print(line)
							player.show_info()
							self.show_pool()
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
							fold += 1
							player.fold = True
				if check+fold == 4 or fold == 3: 
					proceed = True
					if self.play: self.check = True
					if fold == 3: self.other_fold = True
		self.play = not self.play

					
	#Draw cards
	def card_draw(self):
		print('\n'*100)
		for player in self.player:
			if player.fold == False:
				a = 0
				print(line + '\nDraw Phase\n' + line)
				print('{}\'s turn'.format(player))
				print('Select cards to hold on to (minimum of 2) - All unselected cards will be discard and new cards will be dealt')
				print_cards(player.hand)
				while a < 2 or a > 5:
					keep = list(map(int,str(input('Please enter position of cards you wish to keep (card position is between 1-5) (eg., 1234, 542, 25): '))))
					a = len(keep)
					if a < 2: print('!!!!!!Must keep at least 2 cards!!!!!!')
					elif a > 5: print('!!!!!!You only have total of 5 cards!!!!!!')
					else:
						for i in keep:
							if i-1 not in indx:
								print('!!!!!!Must enter number between 1-5!!!!!!')
								a = 0
								break
				for i in indx:
					if i+1 not in keep:
						player.hand[i] = self.deck.pop(0)
				player.sort_hand()
				print('This is your new card\n' + line)
				player.show_hand()


	#Main gameplay code
	def game_play(self):
		#use play variable to indicate round 1 or 2 by flipping boolean status False = 1 True = 2
		while self.check_game():	
			self.play = False
			self.check = False
			self.other_fold = False
			self.game_num += 1
			self.pool = 0
			for player in self.player:
				player.fold = False
			self.card_dealt()
			print('\n\n' + line + '\n\nGame {}: '.format(self.game_num) + '\nRound One\n\n' + line)
			self.round_one()
			if self.other_fold: self.fold_win()
			else:
				self.card_draw()
				print('\n\n' + line + '\n\nGame {}: '.format(self.game_num) + '\nRound Two\n\n' + line)
				self.round_one()
			if self.other_fold: self.fold_win()
			else: 
				contender = []
				for player in self.player:
					if player.fold == False: contender.append(player)
				self.check_win(contender)
			print(line + '\nMoney Recap\n')
			for player in self.player:
				print('{}: ${}'.format(player, player.money))
			print(line)

			for player in self.player:
				self.check_out(player)

	#Win by all other players fold
	def fold_win(self):
		for player in self.player:
			if not player.fold:
				print(line + '\nEveryone fold except {}, {} win by default and took a total of ${}\n'.format(player, player, self.pool) + line)
				player.money += self.pool
						

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
		self.game_play()

DrawFive()