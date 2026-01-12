import tkinter as tk

# Init the window
window = tk.Tk()
window.title("Grid example - Responsive Layout Buttons")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
win_width = screen_width
win_height = screen_height
min_size = 400
window.minsize(min_size, min_size)
window.maxsize(screen_width, screen_height)
win_pos_x = 0
win_pos_y = 0
window.geometry(f"{win_width}x{win_height}+{win_pos_x}+{win_pos_y}")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure((0, 1, 2, 3), weight=1)

# Functions


def size_window(operator):
    global window
    global win_width
    global win_height
    factor = entry1.get()
    win_width = int(round(eval(f"{win_width} {operator} {factor}")))
    win_height = int(round(eval(f"{win_height} {operator} {factor}")))
    pos_x = (screen_width - win_width) // 2
    pos_y = (screen_height - win_height) // 2
    window.geometry(f"{win_width}x{win_height}+{pos_x}+{pos_y}")
    window.update()
    label2["text"] = f"{win_width=}, {win_height=}, {pos_x}, {pos_y}"


def downsize():
    size_window("/")


def upsize():
    size_window("*")


# Controls

label1 = tk.Label(window, text="L F G", bg="black", fg="white")
entry1 = tk.Entry(window, bg="white", fg="black")
button1 = tk.Button(window, text="DOWNSIZE", bg="red", command=downsize)
button2 = tk.Button(window, text="UPSIZE", bg="green", command=upsize)

label2 = tk.Label(
    window, text="Please type a factor for window sizing.", bg="black", fg="white"
)

label1.grid(row=0, column=0, columnspan=2, sticky="NSEW")
entry1.grid(row=1, column=0, columnspan=2)
button1.grid(row=2, column=0, sticky="NSEW", padx=(10, 5), pady=(10, 10))
button2.grid(row=2, column=1, sticky="NSEW", padx=(5, 10), pady=(10, 10))
label2.grid(row=3, column=0, columnspan=2, sticky="NSEW")

window.mainloop()
