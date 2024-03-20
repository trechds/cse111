import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry
import math

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window.
    frm_main = Frame(root)
    frm_main.master.title("Circle Area Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function to add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop.
    root.mainloop()

def populate_main_window(frm_main):
    # Create a label for radius.
    lbl_radius = Label(frm_main, text="Radius:")

    # Create a float entry box for the user to enter radius.
    ent_radius = FloatEntry(frm_main, width=10)

    # Create a label for displaying the result.
    lbl_result = Label(frm_main, text="Area:")

    # Function to calculate the area when radius is entered.
    def calculate(event):
        try:
            # Get the radius entered by the user.
            radius = ent_radius.get()

            # Calculate the area of the circle.
            area = math.pi * radius ** 2

            # Display the calculated area.
            lbl_result.config(text=f"{area:.2f}")
        except ValueError:
            # If invalid input, clear the result label.
            lbl_result.config(text="")

    # Function to clear all inputs and outputs.
    def clear():
        ent_radius.clear()
        lbl_result.config(text="")

    # Create the Calculate button.
    btn_calculate = Button(frm_main, text="Calculate")

    # Bind the calculate function to the radius entry box.
    ent_radius.bind("<KeyRelease>", calculate)

    # Layout the widgets in a grid.
    lbl_radius.grid(row=0, column=0, padx=3, pady=3)
    ent_radius.grid(row=0, column=1, padx=3, pady=3)
    lbl_result.grid(row=1, column=0, columnspan=2, padx=3, pady=3)
    btn_calculate.grid(row=2, column=0, columnspan=2, padx=3, pady=3, sticky="we")

    # Bind the calculate function to the Calculate button.
    btn_calculate.config(command=calculate)

    # Give focus to the radius entry box.
    ent_radius.focus()

# Call the main function if the script is executed directly.
if __name__ == "__main__":
    main()
