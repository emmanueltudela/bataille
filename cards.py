import stack
import random

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "A"]
symbols = ["♥", "♦", "♣", "♠"]

values = {}
for i in range(len(cards)):
	card = cards[i]
	values[card] = i

deck = stack.create(52)
for symbol in symbols:
	for card in cards:
		stack.push(deck, (card, symbol))

def get_value(card):
	card_number = card[0]
	card_symbol = card[1]
	card_value = values[card_number]
	return card_value

def get_shuffled_deck():
	"""
	get_shuffled_deck() => Shuffle global deck var and returns it
	deck => A stack of all classic cards

	Shuffle ->
		- repeat (repeats) times :
			. cut a "slice" of cards between 0 and before last card
			. create three stacks (deck_slices)
				one before the beggining of the slice
				a second one which is the slice
				a third one which is after the sliced part
			. push slices in (deck_shuffled) which is now empty
				first (at the bottom) the slice part (deck_slice[1])
				then two other parts of the game (deck_slice[2])
				and (deck_slice[0])
		- return deck_shuffled
	"""
	deck_shuffled = deck[:]
	deck_slices = [stack.create(52) for i in range(3)]
	repeats = 10000
	for i in range(repeats):
		# 0 <= slice_start < last card
		# The slice shouldn't finish at the end of the deck
		# - because the slice will be added at the end of the deck
		# - afterward, if the slice is at the end that would be nonsense
		deck_size = deck_shuffled[0]
		slice_start = random.randint(0, (deck_size - 1) - 1)
		slice_end = random.randint(slice_start, (deck_size - 1) - 1)
		for j in range(0, slice_start):
			deck_slice = deck_slices[0]
			stack.push(deck_slice, stack.pop(deck_shuffled))
		for j in range(slice_start, slice_end):
			deck_slice = deck_slices[1]
			stack.push(deck_slice, stack.pop(deck_shuffled))
		for j in range(slice_end, deck_size):
			deck_slice = deck_slices[2]
			stack.push(deck_slice, stack.pop(deck_shuffled))
		# Putting slices back in the deck
		# + Put the middle slice at the bottom
		while not stack.is_empty(deck_slices[1]):
			stack.push(deck_shuffled, stack.pop(deck_slices[1]))
		while not stack.is_empty(deck_slices[2]):
			stack.push(deck_shuffled, stack.pop(deck_slices[2]))
		while not stack.is_empty(deck_slices[0]):
			stack.push(deck_shuffled, stack.pop(deck_slices[0]))
	return deck_shuffled