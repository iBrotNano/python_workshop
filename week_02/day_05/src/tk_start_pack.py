import tkinter as tk

a = 0
window = tk.Tk()
window.geometry("400x400")


def _button():
    global a
    print(f"button pressed, value of a => {a}")
    print(f"text of label1 before click: {label1["text"]}")
    a += 1
    label1["text"] = str(a)
    print(f"text of label1 after click: {label1.cget("text")}")


label1 = tk.Label(window, text="Mein Label", bg="green")
button1 = tk.Button(window, text="Klick", bg="purple", command=_button)
button2 = tk.Button(window, text="Klick", bg="orange")
label1.pack(fill="both", side="left", expand=1)
button1.pack(fill="both", side="left", expand=1)
button2.pack(fill="both", side="left", expand=1)
window.mainloop()
