import tkinter as tk

current_calculation = ""


def add_text(symbol):
    global current_calculation
    current_calculation += symbol
    main_textbox.configure(state="normal")
    main_textbox.delete(0, "end")
    main_textbox.insert("end", current_calculation)
    main_textbox.xview_moveto(1)
    main_textbox.configure(state="readonly")

def calculate():
    global current_calculation
    main_textbox.configure(state="normal")
    try:
        current_calculation = str(eval(current_calculation))
        main_textbox.delete(0, "end")
        main_textbox.insert("end", current_calculation)
    except:
        clear_text()
        main_textbox.configure(state="normal")
        main_textbox.insert("end", "ERROR")
    main_textbox.xview_moveto(1)
    main_textbox.configure(state="readonly")

def clear_text():
    global current_calculation
    current_calculation = ""
    main_textbox.configure(state="normal")
    main_textbox.delete(0, "end")
    main_textbox.configure(state="readonly")










# GUI

root = tk.Tk()
root.title("Calculator")
root.geometry("417x508")
root.configure(bg="#585858")
root.resizable(False, False)

button_width = 10
button_height = 4
button_color = "#A5A5A5"
pad_x = 2
pad_y = 2
font_family = "Arial"
font_size = 0
font = (font_family, font_size)


main_textbox = tk.Entry(root, width=17, font=(font, 32))
main_textbox.grid(row=1, columnspan=4, padx=pad_x, pady=pad_y)
main_textbox.configure(state="readonly")


btn_1 = tk.Button(root, text="1", width=button_width, height=button_height, font=font, command=lambda: add_text("1"), bg=button_color)
btn_1.grid(row=2, column=0, padx=pad_x, pady=pad_y)
btn_2 = tk.Button(root, text="2", width=button_width, height=button_height, font=font, command=lambda: add_text("2"), bg=button_color)
btn_2.grid(row=2, column=1, padx=pad_x, pady=pad_y)
btn_3 = tk.Button(root, text="3", width=button_width, height=button_height, font=font, command=lambda: add_text("3"), bg=button_color)
btn_3.grid(row=2, column=2, padx=pad_x, pady=pad_y)
btn_plus = tk.Button(root, text="+", width=button_width, height=button_height, font=font, command=lambda: add_text("+"), bg=button_color)
btn_plus.grid(row=2, column=3, padx=pad_x, pady=pad_y)

btn_4 = tk.Button(root, text="4", width=button_width, height=button_height, font=font, command=lambda: add_text("4"), bg=button_color)
btn_4.grid(row=3, column=0, padx=pad_x, pady=pad_y)
btn_5 = tk.Button(root, text="5", width=button_width, height=button_height, font=font, command=lambda: add_text("5"), bg=button_color)
btn_5.grid(row=3, column=1, padx=pad_x, pady=pad_y)
btn_6 = tk.Button(root, text="6", width=button_width, height=button_height, font=font, command=lambda: add_text("6"), bg=button_color)
btn_6.grid(row=3, column=2, padx=pad_x, pady=pad_y)
btn_minus = tk.Button(root, text="-", width=button_width, height=button_height, font=font, command=lambda: add_text("-"), bg=button_color)
btn_minus.grid(row=3, column=3, padx=pad_x, pady=pad_y)

btn_7 = tk.Button(root, text="7", width=button_width, height=button_height, font=font, command=lambda: add_text("7"), bg=button_color)
btn_7.grid(row=4, column=0, padx=pad_x, pady=pad_y)
btn_8 = tk.Button(root, text="8", width=button_width, height=button_height, font=font, command=lambda: add_text("8"), bg=button_color)
btn_8.grid(row=4, column=1, padx=pad_x, pady=pad_y)
btn_9 = tk.Button(root, text="9", width=button_width, height=button_height, font=font, command=lambda: add_text("9"), bg=button_color)
btn_9.grid(row=4, column=2, padx=pad_x, pady=pad_y)
btn_mult = tk.Button(root, text="*", width=button_width, height=button_height, font=font, command=lambda: add_text("*"), bg=button_color)
btn_mult.grid(row=4, column=3, padx=pad_x, pady=pad_y)

btn_lbrac = tk.Button(root, text="(", width=button_width, height=button_height, font=font, command=lambda: add_text("("), bg=button_color)
btn_lbrac.grid(row=5, column=0, padx=pad_x, pady=pad_y)
btn_0 = tk.Button(root, text="0", width=button_width, height=button_height, font=font, command=lambda: add_text("0"), bg=button_color)
btn_0.grid(row=5, column=1, padx=pad_x, pady=pad_y)
btn_rbrac = tk.Button(root, text=")", width=button_width, height=button_height, font=font, command=lambda: add_text(")"), bg=button_color)
btn_rbrac.grid(row=5, column=2, padx=pad_x, pady=pad_y)
btn_div = tk.Button(root, text="/", width=button_width, height=button_height, font=font, command=lambda: add_text("/"), bg=button_color)
btn_div.grid(row=5, column=3, padx=pad_x, pady=pad_y)

btn_00 = tk.Button(root, text="00", width=button_width, height=button_height, font=font, command=lambda: add_text("00"), bg=button_color)
btn_00.grid(row=6, column=0, padx=pad_x, pady=pad_y)
btn_dot = tk.Button(root, text=".", width=button_width, height=button_height, font=font, command=lambda: add_text("."), bg=button_color)
btn_dot.grid(row=6, column=1, padx=pad_x, pady=pad_y)
btn_ac = tk.Button(root, text="AC", width=button_width, height=button_height, font=font, command=clear_text, bg="#FFBABA")
btn_ac.grid(row=6, column=2, padx=pad_x, pady=pad_y)
btn_eq = tk.Button(root, text="=", width=button_width, height=button_height, font=font, command=calculate, bg="#B3FFB7")
btn_eq.grid(row=6, column=3, padx=pad_x, pady=pad_y)



root.mainloop()