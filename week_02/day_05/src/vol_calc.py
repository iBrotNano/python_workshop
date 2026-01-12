import tkinter as tk
import tkinter.messagebox as mb

app = tk.Tk()
app.title("Volumenrechner")
app.geometry("400x400+512+200")
app.resizable(False, False)

frame = tk.Frame(app, relief="groove", bd=2).pack()


def clear_fields():
    pressed = mb.askyesnocancel("Clear?", message="Wirklich alles löschen?")

    if pressed:
        hoehe_input.delete(0, tk.END)
        breite_input.delete(0, tk.END)
        tiefe_input.delete(0, tk.END)
        result_output["text"] = ""


def calc_vol():
    h = hoehe_input.get()
    b = breite_input.get()
    t = tiefe_input.get()

    vol = float(h) * float(b) * float(t)
    result_output["text"] = vol


hoehe_caption = tk.Label(
    frame, text="Höhe"
)  # Label Widget als Überschrit für Eingabefeld der Höhe
hoehe_input = tk.Entry(frame)  # Eingabefeld für Höhe

breite_caption = tk.Label(
    frame, text="Breite"
)  # Label Widget als Überschrit für Eingabefeld der Breite
breite_input = tk.Entry(frame)  # Eingabefeld für Breite

tiefe_caption = tk.Label(
    frame, text="Tiefe"
)  # Label Widget als Überschrit für Eingabefeld der Tiefe
tiefe_input = tk.Entry(frame)  # Eingabefeld für Tiefe

clear_button = tk.Button(
    frame, text="CLEAR", command=clear_fields
)  # Button um alle Eingabefelder und Output zu leeren
calc_button = tk.Button(
    frame, text="GET VOLUME", command=calc_vol
)  # Button der die Berechnung des Volumens auslöst

result_caption = tk.Label(
    frame, text="Ergebnis"
)  # Label Widget als Überschrit für Eingabefeld für Ergebnisfeld
result_output = tk.Label(frame)  # Label Widget als Ergebnisfeld

##################################################################

# Platzierung IMMER von Erzeugung auslagern!

hoehe_caption.pack()
hoehe_input.pack()

breite_caption.pack()
breite_input.pack()

tiefe_caption.pack()
tiefe_input.pack()

clear_button.pack(side="left", padx=10, pady=10)
calc_button.pack(side="right", padx=10, pady=10)

result_caption.pack()
result_output.pack()

app.mainloop()
