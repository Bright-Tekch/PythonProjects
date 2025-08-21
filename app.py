import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            screen_var.set(result)
            expression = str(result)
        except Exception as e:
            screen_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        screen_var.set("")
    else:
        expression += text
        screen_var.set(expression)

expression = ""
root = tk.Tk()
root.title("Calculator")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20 bold", bd=10, relief=tk.SUNKEN, justify=tk.RIGHT)
screen.pack(fill=tk.BOTH, ipadx=8)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 0, 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font="Arial 15 bold", padx=20, pady=20)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
