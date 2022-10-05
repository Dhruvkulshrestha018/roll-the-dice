#import tkinter amd ramdom modules
from tkinter import *
import random

#create a window
window = Tk()

# Setting background colour of the window
window.configure(bg="blue")

# Setting geometry of the window
window.geometry("530x350")

# Setting title of the window
window.title("Rolling The Dice Game")

# Preventing maximizing of the window
window.resizable(0, 0)

# Creating function to roll the dices
def roll_dices():
	# These values indicate dots on the dices.
	# For eg: \u2680 corresponds to 1 dot,
	# \u2681 corresponds to 2 dots etc.
	dice_dots = ['\u2680', '\u2681','\u2682', '\u2683','\u2684', '\u2685']
	# Generating random dots on the dices
	label.configure(
		text=f'{random.choice(dice_dots)}{random.choice(dice_dots)}')
	label.pack()


# Adding button to roll the dices
roll_button = Button(window, text="Roll!",
					width=10, height=2,
					font=20, bg="aqua",
					bd=2, command=roll_dices)
# Setting the position of the button
roll_button.pack(padx=12, pady=18)

# Adding Label
label = Label(window, font=("times", 250),
			bg="black", fg="yellow")

window.mainloop()

