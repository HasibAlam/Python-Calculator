import os
import tkinter as tk
import sys

# Check if we're running in a headless environment
if os.environ.get('DISPLAY', '') == '':
    print("No display found. Running in headless mode.")
    sys.exit()

# Tkinter GUI code
calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "ERROR")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x400")
root.title("Hasib's Python Calculator")
# Colors for buttons and background
button_color_orange = "#FFA500"  # Orange for operation buttons
button_color_black = "#333333"   # Black for number buttons
button_color_green = "#32CD32"   # Green for the equal button
text_color_white = "#FF0000"     # White text color
bg_color = "#000000"             # Black background for the window
text_bg_color = "#000000"        # Black background for the display
text_fg_color = "#FFFFFF"        # White foreground for the display text

# Set background color for the window
root.configure(bg=bg_color)

# Text display area
text_result = tk.Text(root, height=2, width=20, font=("Arial", 24), bg=text_bg_color, fg=text_fg_color)
text_result.grid(columnspan=5, sticky="nsew")

# Button 1
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), height=2, width=5, font=("Arial", 14),
                  bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_1.grid(row=2, column=1, sticky="nsew")

# Button 2
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), height=2, width=5, font=("Arial", 14),
                  bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_2.grid(row=2, column=2, sticky="nsew")

# Button 3
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), height=2, width=5, font=("Arial", 14),
                  bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_3.grid(row=2, column=3, sticky="nsew")

# Button 4
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), height=2, width=5, font=("Arial", 14),
                  bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_4.grid(row=3, column=1, sticky="nsew")

# Button 5
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), height=2, width=5, font=("Arial", 14),
                  bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_5.grid(row=3, column=2, sticky="nsew")

# Button 6
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), height=2, width=5, font=("Arial", 14),
                  bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_6.grid(row=3, column=3, sticky="nsew")

# Button 7
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), height=2, width=5, font=("Arial", 14),
                  bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_7.grid(row=4, column=1, sticky="nsew")

# Button 8
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), height=2, width=5, font=("Arial", 14),
                  bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_8.grid(row=4, column=2, sticky="nsew")

# Button 9
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), height=2, width=5, font=("Arial", 14),
                  bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_9.grid(row=4, column=3, sticky="nsew")

# Button 0
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), height=2, width=5, font=("Arial", 14),
                  bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_0.grid(row=5, column=2, sticky="nsew")

# Button +
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), height=2, width=5, font=("Arial", 14),
                     bg=button_color_orange, fg=text_color_white, highlightbackground=button_color_orange)
btn_plus.grid(row=2, column=4, sticky="nsew")

# Button -
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), height=2, width=5, font=("Arial", 14),
                      bg=button_color_orange, fg=text_color_white, highlightbackground=button_color_orange)
btn_minus.grid(row=3, column=4, sticky="nsew")

# Button *
btn_mul = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), height=2, width=5, font=("Arial", 14),
                    bg=button_color_orange, fg=text_color_white, highlightbackground=button_color_orange)
btn_mul.grid(row=4, column=4, sticky="nsew")

# Button ÷
btn_div = tk.Button(root, text="÷", command=lambda: add_to_calculation("/"), height=2, width=5, font=("Arial", 14),
                    bg=button_color_orange, fg=text_color_white, highlightbackground=button_color_orange)
btn_div.grid(row=5, column=4, sticky="nsew")

# Button (
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), height=2, width=5, font=("Arial", 14),
                     bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_open.grid(row=5, column=1, sticky="nsew")

# Button )
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), height=2, width=5, font=("Arial", 14),
                      bg=button_color_black, fg=text_color_white, highlightbackground=button_color_black)
btn_close.grid(row=5, column=3, sticky="nsew")

# Button =
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, height=2, width=11, font=("Arial", 14),
                       bg=button_color_green, fg=text_color_white, highlightbackground=button_color_green)
btn_equals.grid(row=6, column=3, columnspan=2, sticky="nsew")

# Button clear
btn_clear = tk.Button(root, text="clear", command=clear_field, height=2, width=11, font=("Arial", 14),
                      bg=button_color_orange, fg=text_color_white, highlightbackground=button_color_orange)
btn_clear.grid(row=6, column=1, columnspan=2, sticky="nsew")

# Make the calculator and display responsive
for i in range(1, 7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Make the text display responsive as well
text_result.grid(row=1, column=1, columnspan=4, sticky="nsew")

root.mainloop()