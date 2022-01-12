import tkinter as tk

class Application(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.show_window()

	def show_window(self):
		"""
		show_window(self) => Show every components that should be in the window (Tkinter)
		"""
		self.grid()

		self.label_player_1 = tk.Label(self, text="Player 1 - 0")
		self.label_player_1.grid(
			row = 1,
			column = 1,
		)
		self.label_player_1.config(
			font = ("Monospace", 15),
		)

		self.card_1 = tk.Label(self, text="Empty")
		self.card_1.grid(
			row = 2,
			column = 1,
			padx = 10
		)
		self.card_1.config(
			width = 10,
			height = 8,
			borderwidth = 3,
			relief = "raised",
			font = ("Monospace", 30),
			bg = "white"
		)

		self.label_deck_1_remaining = tk.Label(self, text="26")
		self.label_deck_1_remaining.grid(
			row = 2,
			column = 1,
			sticky="se",
			padx = 10
		)
		self.label_deck_1_remaining.config(
			width = 5,
			borderwidth = 3,
			relief = "raised",
			font = ("Monospace", 10),
			bg = "black",
			fg="white"
		)

		self.label_vs = tk.Label(self, text="VS")
		self.label_vs.grid(
			row = 2,
			column = 2,
		)
		self.label_vs.config(
			font = ("Monospace", 20, "underline"),
		)

		self.label_player_2 = tk.Label(self, text="Player 2 - 0")
		self.label_player_2.grid(
			row = 1,
			column = 3,
		)
		self.label_player_2.config(
			font = ("Monospace", 15),
		)

		self.card_2 = tk.Label(self, text="Empty")
		self.card_2.grid(
			row = 2,
			column = 3,
			padx = 10
		)
		self.card_2.config(
			width = 10,
			height = 8,
			borderwidth = 3,
			relief = "raised",
			font = ("Monospace", 30),
			bg = "white"
		)

		self.label_deck_2_remaining = tk.Label(self, text="26")
		self.label_deck_2_remaining.grid(
			row = 2,
			column = 3,
			sticky="se",
			padx = 10
		)
		self.label_deck_2_remaining.config(
			width = 5,
			borderwidth = 3,
			relief = "raised",
			font = ("Monospace", 10),
			bg = "black",
			fg="white"
		)

		self.set_card_1(("A", "♥"))
		self.set_card_2(("A", "♣"))

	def get_symbol_color(self, card):
		"""
		symbol_color(self, card) => Returns the associated color for a card symbol :
			-> ♥ == "red"
		card => Tuple representing a card like : (2, ♥)
		"""
		card_symbol = card[1]
		if card_symbol == "♥":
			return "red"
		elif card_symbol == "♦":
			return "red"
		elif card_symbol == "♣":
			return "black"
		else:
			return "black"

	def set_card_1(self, card):
		"""
		set_card_1(self, card) => Update card_1 with the wanted card and change color
			depending on the symbol of the card
		card => Tuple representing a card like : (2, ♥)
		"""
		card_value = card[0]
		card_symbol = card[1]
		self.card_1.config(text = card_value + card_symbol)
		self.card_1.config(fg = self.get_symbol_color(card))

	def set_card_2(self, card):
		card_value = card[0]
		card_symbol = card[1]
		self.card_2.config(text = card_value + card_symbol)
		self.card_2.config(fg = self.get_symbol_color(card))

if __name__=="__main__":
	app = Application()
	app.title = "Bataille"
	app.mainloop()