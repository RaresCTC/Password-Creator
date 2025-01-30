import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        l = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Eroare", "Introduceți un număr valid pentru lungimea parolei.")
        return

    lc = ""
    if letters_var.get():
        lc += string.ascii_letters
    if numbers_var.get():
        lc += string.digits
    if special_var.get():
        lc += string.punctuation

    if not lc:
        messagebox.showerror("Eroare", "Selectați cel puțin un tip de caracter.")
        return

    password = ''.join(random.choice(lc) for _ in range(l))
    result_label.config(text=f"Parola random este: {password}")

# Creează fereastra principală
root = tk.Tk()
root.title("Generator de Parole")

# Lungimea parolei
tk.Label(root, text="Lungime dorită parola:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Opțiuni de caractere
tk.Label(root, text="Alege caractere pentru parola:").pack()
letters_var = tk.BooleanVar()
tk.Checkbutton(root, text="Litere", variable=letters_var).pack()
numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Numere", variable=numbers_var).pack()
special_var = tk.BooleanVar()
tk.Checkbutton(root, text="Caractere speciale", variable=special_var).pack()

# Buton pentru generarea parolei
generate_button = tk.Button(root, text="Generează parola", command=generate_password)
generate_button.pack()

# Etichetă pentru afișarea rezultatului
result_label = tk.Label(root, text="")
result_label.pack()

# Rulează bucla aplicației
root.mainloop()