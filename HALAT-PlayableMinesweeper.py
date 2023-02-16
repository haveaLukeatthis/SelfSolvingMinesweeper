# -*- coding: utf-8 -*-

import random
from tkinter import *

# user configurable
NUMBER_OF_BOMBS = 400
NUMBER_OF_ROWS = 38
NUMBER_OF_COLUMNS = 56
START_ROW = 12
START_COLUMN = 10

# lists
buttons = []
bombIndexes = []
flagIndexes = []
clickedIndexes = []
recursiveChecksList = []

nRevealedTiles = 0


def main():
	# tk setup
	root = Tk()
	my_str = StringVar()
	l1 = Label(root, textvariable=my_str)
	l1.grid(row=0, column=0, columnspan=10)

	# lists
	fill_buttons_list(root)
	initialize_lists()

	# place start tile
	start_index = ((START_ROW - 1) * NUMBER_OF_COLUMNS) + START_COLUMN - 1
	buttons[start_index].config(text="S")

	place_bombs(start_index)

	root.mainloop()


def fill_buttons_list(root: Tk):
	button_index = 0
	# Loop which creates all the tiles
	for row in range(NUMBER_OF_ROWS):
		for column in range(NUMBER_OF_COLUMNS):
			buttons.append(Button(root, width=2, height=1, font='Terminal'))
			buttons[button_index].bind('<Double-Button-1>',
				lambda event, x=column, y=row, index=button_index: my_fun(event, x, y, index))
			buttons[button_index].bind('<Button-1>',
				lambda event, x=column, y=row, index=button_index: chord_click(event, x, y, index))
			buttons[button_index].bind('<Button-3>',
				lambda event, x=column, y=row, index=button_index: flag_click(index))
			buttons[button_index].grid(row=row + 1, column=column)
			button_index += 1


def initialize_lists():
	global flagIndexes
	global clickedIndexes
	global recursiveChecksList
	flagIndexes = [0] * len(buttons)
	clickedIndexes = [0] * len(buttons)
	recursiveChecksList = [0] * len(buttons)


def place_bombs(start_index):
	global bombIndexes
	numbered_tile_list = list(range(0, len(buttons)))
	for i in [-1, 0, 1]:
		numbered_tile_list.remove(start_index + NUMBER_OF_COLUMNS + i)
		numbered_tile_list.remove(start_index + i)
		numbered_tile_list.remove(start_index - NUMBER_OF_COLUMNS + i)
	bombIndexes = random.sample(numbered_tile_list, NUMBER_OF_BOMBS)


def flag_click(index):
	button_box = buttons[index]
	if clickedIndexes[index] != 0:
		return
	if flagIndexes[index] == 0:
		button_box.config(text="🚩")
		button_box.config(fg="red")
		flagIndexes[index] = 1
	elif flagIndexes[index] == 1:
		button_box.config(text="")
		flagIndexes[index] = 0


def chord_click(event, x, y, index):
	button_box = buttons[index]
	if clickedIndexes[index] != 1 and button_box.cget('text') == "B":
		return

	# Check number of nearby flagged cells
	nearby_flag_count = count_nearby_flags(index, x, y)

	# print("Nearby flag count is " + str(nearby_flag_count) + " and nearby bomb count is " + button_box.cget('text'))

	# Check if all nearby bombs have been flagged
	if nearby_flag_count == int(button_box.cget('text')):
		# print("match")
		# reveal all non-flagged nearby tiles
		reveal_tiles(event, index, x, y)


def reveal_tiles(event, index, x, y):
	if x != 0 and flagIndexes[index - 1] == 0:
		my_fun(event, x - 1, y, index - 1)
	if x != NUMBER_OF_COLUMNS - 1 and flagIndexes[index + 1] == 0:
		my_fun(event, x + 1, y, index + 1)
	if y != 0 and flagIndexes[index - NUMBER_OF_COLUMNS] == 0:
		my_fun(event, x, y - 1, index - NUMBER_OF_COLUMNS)
	if y != NUMBER_OF_ROWS - 1 and flagIndexes[index + NUMBER_OF_COLUMNS] == 0:
		my_fun(event, x, y + 1, index + NUMBER_OF_COLUMNS)
	if x != 0 and y != 0 and flagIndexes[index - 1 - NUMBER_OF_COLUMNS] == 0:
		my_fun(event, x - 1, y - 1, index - 1 - NUMBER_OF_COLUMNS)
	if x != NUMBER_OF_COLUMNS - 1 and y != 0 and flagIndexes[index + 1 - NUMBER_OF_COLUMNS] == 0:
		my_fun(event, x + 1, y - 1, index + 1 - NUMBER_OF_COLUMNS)
	if x != 0 and y != NUMBER_OF_ROWS - 1 and flagIndexes[index - 1 + NUMBER_OF_COLUMNS] == 0:
		my_fun(event, x - 1, y + 1, index - 1 + NUMBER_OF_COLUMNS)
	if x != NUMBER_OF_COLUMNS - 1 and y != NUMBER_OF_ROWS - 1 and flagIndexes[
		index + 1 + NUMBER_OF_COLUMNS] == 0:
		my_fun(event, x + 1, y + 1, index + 1 + NUMBER_OF_COLUMNS)


def count_nearby_flags(index, x, y):
	nearby_flag_count = 0
	# Check cell to the left
	if x != 0 and flagIndexes[index - 1] == 1:
		nearby_flag_count += 1
	# Check cell to the right
	if x != NUMBER_OF_COLUMNS - 1 and flagIndexes[index + 1] == 1:
		nearby_flag_count += 1
	# Check cell above
	if y != 0 and flagIndexes[index - NUMBER_OF_COLUMNS] == 1:
		nearby_flag_count += 1
	# Check cell below
	if y != NUMBER_OF_ROWS - 1 and flagIndexes[index + NUMBER_OF_COLUMNS] == 1:
		nearby_flag_count += 1
	# Check cell up & left
	if x != 0 and y != 0 and flagIndexes[index - 1 - NUMBER_OF_COLUMNS] == 1:
		nearby_flag_count += 1
	# Check cell up & right
	if x != NUMBER_OF_COLUMNS - 1 and y != 0 and flagIndexes[index + 1 - NUMBER_OF_COLUMNS] == 1:
		nearby_flag_count += 1
	# Check cell down & left
	if x != 0 and y != NUMBER_OF_ROWS - 1 and flagIndexes[index - 1 + NUMBER_OF_COLUMNS] == 1:
		nearby_flag_count += 1
	# Check cell down & right
	if x != NUMBER_OF_COLUMNS - 1 and y != NUMBER_OF_ROWS - 1 and flagIndexes[index + 1 + NUMBER_OF_COLUMNS] == 1:
		nearby_flag_count += 1
	return nearby_flag_count


def show_all_bombs():
	for button in range(len(buttons)):
		button_box = buttons[button]
		if is_bomb(button) and flagIndexes[button] == 0:
			button_box.config(text="💣")
			button_box.config(fg="black")


def is_bomb(index):
	return TRUE if bombIndexes.count(index) > 0 else FALSE


def my_fun(event, x, y, index):
	if clickedIndexes[index] != 0:
		return

	# my_str.set("button row is " + str(x) + " button col is " + str(y) + " index is " + str(index))
	button_box = buttons[index]

	nearby_bomb_count = count_nearby_bombs(index, x, y)
	if nearby_bomb_count == 0 and not is_bomb(index):
		recursiveChecksList[index] = 1
		if x != 0 and recursiveChecksList[index - 1] == 0:
			my_fun(event, x - 1, y, index - 1)
		if x != NUMBER_OF_COLUMNS - 1 and recursiveChecksList[index + 1] == 0:
			my_fun(event, x + 1, y, index + 1)
		if y != 0 and recursiveChecksList[index - NUMBER_OF_COLUMNS] == 0:
			my_fun(event, x, y - 1, index - NUMBER_OF_COLUMNS)
		if y != NUMBER_OF_ROWS - 1 and recursiveChecksList[index + NUMBER_OF_COLUMNS] == 0:
			my_fun(event, x, y + 1, index + NUMBER_OF_COLUMNS)
		if x != 0 and y != 0 and recursiveChecksList[index - 1 - NUMBER_OF_COLUMNS] == 0:
			my_fun(event, x - 1, y - 1, index - 1 - NUMBER_OF_COLUMNS)
		if x != NUMBER_OF_COLUMNS - 1 and y != 0 and recursiveChecksList[index + 1 - NUMBER_OF_COLUMNS] == 0:
			my_fun(event, x + 1, y - 1, index + 1 - NUMBER_OF_COLUMNS)
		if x != 0 and y != NUMBER_OF_ROWS - 1 and recursiveChecksList[index - 1 + NUMBER_OF_COLUMNS] == 0:
			my_fun(event, x - 1, y + 1, index - 1 + NUMBER_OF_COLUMNS)
		if x != NUMBER_OF_COLUMNS - 1 and y != NUMBER_OF_ROWS - 1 and recursiveChecksList[index + 1 + NUMBER_OF_COLUMNS] == 0:
			my_fun(event, x + 1, y + 1, index + 1 + NUMBER_OF_COLUMNS)

	set_font_color(button_box, nearby_bomb_count)

	# Update cell number
	# Check for bomb in current cell
	if is_bomb(index):
		button_box.config(text="💣")
		button_box.config(fg="black")
		print("You Lose")
		show_all_bombs()
	else:
		button_box.config(text=str(nearby_bomb_count))
		button_box.config(relief="flat")
		button_box.config(bg="#e9e9e9")

	global nRevealedTiles
	nRevealedTiles += 1

	# Check to see if you've won
	if nRevealedTiles == (NUMBER_OF_ROWS * NUMBER_OF_COLUMNS) - NUMBER_OF_BOMBS:
		print("You Win")

	clickedIndexes[index] = 1


def count_nearby_bombs(index, x, y):
	nearby_bomb_count = 0
	# Check cell to the left
	if x != 0 and is_bomb(index - 1):
		nearby_bomb_count += 1
	# Check cell to the right
	if x != NUMBER_OF_COLUMNS - 1 and is_bomb(index + 1):
		nearby_bomb_count += 1
	# Check cell above
	if y != 0 and is_bomb(index - NUMBER_OF_COLUMNS):
		nearby_bomb_count += 1
	# Check cell below
	if y != NUMBER_OF_ROWS - 1 and is_bomb(index + NUMBER_OF_COLUMNS):
		nearby_bomb_count += 1
	# Check cell up & left
	if x != 0 and y != 0 and is_bomb(index - 1 - NUMBER_OF_COLUMNS):
		nearby_bomb_count += 1
	# Check cell up & right
	if x != NUMBER_OF_COLUMNS - 1 and y != 0 and is_bomb(index + 1 - NUMBER_OF_COLUMNS):
		nearby_bomb_count += 1
	# Check cell down & left
	if x != 0 and y != NUMBER_OF_ROWS - 1 and is_bomb(index - 1 + NUMBER_OF_COLUMNS):
		nearby_bomb_count += 1
	# Check cell down & right
	if x != NUMBER_OF_COLUMNS - 1 and y != NUMBER_OF_ROWS - 1 and is_bomb(index + 1 + NUMBER_OF_COLUMNS):
		nearby_bomb_count += 1
	return nearby_bomb_count


def set_font_color(button_box, nearby_bomb_count):
	# Set the font colour based on number of bombs nearby
	if nearby_bomb_count == 0:
		button_box.config(fg="#e9e9e9")
	elif nearby_bomb_count == 1:
		button_box.config(fg="blue")
	elif nearby_bomb_count == 2:
		button_box.config(fg="green")
	elif nearby_bomb_count == 3:
		button_box.config(fg="red")
	elif nearby_bomb_count == 4:
		button_box.config(fg="#9900ff")
	elif nearby_bomb_count == 5:
		button_box.config(fg="#660000")
	elif nearby_bomb_count == 6:
		button_box.config(fg="#4a86e8")
	elif nearby_bomb_count == 7:
		button_box.config(fg="black")
	elif nearby_bomb_count == 8:
		button_box.config(fg="#d9d9d9")


if __name__ == '__main__':
	main()
