import tkinter as tk
from tkinter import ttk
import Kanji
import os
import sys

kanji = tk.Tk()
kanji.title("Kanji PDF generator")
kanji.state('normal')


colonnes = ["Kanji", "Kun'yomi", "On'yomi", "Traduction","Number"]


levels = ["N1","N2","N3","N4","N5"]

levels_vars = {level: tk.IntVar() for level in levels}

# Create Checkbuttons for each level
for idx, level in enumerate(levels):
    check_button = tk.Checkbutton(kanji, text=level, variable=levels_vars[level])
    check_button.grid(row=0, column=idx, padx=10, pady=5)

def keep_numbers_with_comprehension(input_string):
    return ''.join([char for char in input_string if char.isdigit()])

# Function to show selected levels
def create_PDF():
    selected_levels = [level for level in levels if levels_vars[level].get() == 1]
    number =""
    for i in selected_levels:
        number += i
    number=keep_numbers_with_comprehension(number)
   # print("To send:",number)
    Kanji.niveauSelect(number)
    # Allow to change levels without restarting everything
    kanji.quit()
    python = sys.executable
    os.execv(python, ['python'] + sys.argv)

# Button to print selected levels
submit_button = tk.Button(kanji, text="Create PDF", command=create_PDF)
submit_button.grid(row=1, columnspan=len(levels), padx=10, pady=10)


def run():
    kanji.mainloop()

if __name__ == "__main__":
    run()