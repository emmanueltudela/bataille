import my_queue
import stack
import cards
import random
import window

playing = True

player_1_score = 0
player_2_score = 0

cards_exchanges_limit = 10000

while playing:
	# print("New game (p1 : " + str(player_1_score) + " vs p2 : " + str(player_2_score) + ")")

	# Base deck (With every cards)
	deck = cards.get_shuffled_deck()

	deck_1 = que.create(52)
	deck_2 = que.create(52)

	# Distribute the cards => 1 / 2 for the two players
	for i in range(52):
		if i % 2 == 0:
			que.enqueue(deck_1, stack.pop(deck))
		else:
			que.enqueue(deck_2, stack.pop(deck))

	deck1_length = deck_1[0]
	deck2_length = deck_2[0]

	cards_exchanges = 0
	while deck1_length != 0 and deck2_length != 0 and cards_exchanges < cards_exchanges_limit:
		# print("--------------------------")
		# input()

		played_cards = que.create(52)

		# Storing two cards to compare them =>
		# 		. card_1
		# 		. card_2
		# Adding two cards to played_cards
		card_1 = que.dequeue(deck_1)
		card_2 = que.dequeue(deck_2)
		que.enqueue(played_cards, card_1)
		que.enqueue(played_cards, card_2)

		# Will store the winner of this turn
		winner = []

		p1_cards_left = deck_1[0]
		p2_cards_left = deck_2[0]

		# print("P1(" + str(p1_cards_left) + ") : (" + card_1[0] + " - " + card_1[1] + ") vs P2(" + str(p2_cards_left) + ") : (" + card_2[0] + " - " + card_2[1] + ")")
		# input()

		card1_value = cards.get_value(card_1)
		card2_value = cards.get_value(card_2)

		if card1_value < card2_value:
			winner = deck_2
			# print("Player 2 : WIN")
		elif card1_value > card2_value:
			winner = deck_1
			# print("Player 1 : WIN")
		else:
			# print("===== BATTLE =====")
			# input()

			battle = True
			while battle:
				# Be sure that no deck is empty
				if not que.is_empty(deck_1) and not que.is_empty(deck_2):
					# According to the battle game (Base rules)
					# When a battle is declared two cards must be played with their value hidden
					que.enqueue(played_cards, que.dequeue(deck_1))
					que.enqueue(played_cards, que.dequeue(deck_2))

					# Because we are dequeueuing another time we need to verify another time
					if not que.is_empty(deck_1) and not que.is_empty(deck_2):
						# Storing two cards to compare them =>
						# 		. card_1
						# 		. card_2
						# Adding two cards to played_cards
						card_1 = que.dequeue(deck_1)
						card_2 = que.dequeue(deck_2)
						que.enqueue(played_cards, card_1)
						que.enqueue(played_cards, card_2)

						# print("-- TWO CARDS IN GAME --\n")
						# print("P1 (" + str(p1_cards_left) + ") : (" + card_1[0] + " - " + card_1[1] + ") vs P2 (" + str(p2_cards_left) + ") : (" + card_2[0] + " - " + card_2[1] + ")")
						# input()

						card1_value = cards.get_value(card_1)
						card2_value = cards.get_value(card_2)

						if card1_value < card2_value:
							winner = deck_2
							battle = False
							# print("Player 2 : WIN")
						elif card1_value > card2_value:
							winner = deck_1
							battle = False
							# print("Player 1 : WIN")
						# else battle continue
					else:
						battle = False
						if que.is_empty(deck_1):
							winner = deck_2
							# print("Player 1 : No cards left...")
						else:
							winner = deck_1
							# print("Player 2 : No cards left...")
				else:
						battle = False
						if que.is_empty(deck_1):
							winner = deck_2
							# print("Player 1 : No cards left...")
						else:
							winner = deck_1
							# print("Player 2 : No cards left...")

			# input()
			# print("===== BATTLE ENDS =====")

		# input()
		# print("Cards won :")

		# Putting every played cards in the winner's deck
		while not que.is_empty(played_cards):
			card = que.dequeue(played_cards)

			# print(" . " + card[0] + " - " + card[1])

			que.enqueue(winner, card)

		# input()

		# Update decks lengths
		deck1_length = deck_1[0]
		deck2_length = deck_2[0]
		cards_exchanges += 1

	# print("-_-_-_- GAME ENDS -_-_-_-")
	# input()

	# The winner is the player with cards remaining in his deck
	deck1_length = deck_1[0]
	deck2_length = deck_2[0]

	# if game exchanges exceeded limit => Player with bigger deck win
	# else player with empty deck loses
	if cards_exchanges >= cards_exchanges_limit:
		print("Game limit exceeded ( > " + str(cards_exchanges_limit) + " echanges )")
		if deck1_length > deck2_length:
			print("Player 1 : WIN")
			player_1_score += 1
		else:
			print("Player 2 : WIN")
			player_2_score += 1
	elif deck1_length == 0:
		print("Player 2 : WIN")
		player_2_score += 1
	else:
		print("Player 1 : WIN")
		player_1_score += 1

	# input()
	choice = input("Continue playing ? (y/n) : ")
	if choice == 'n':
		playing = False