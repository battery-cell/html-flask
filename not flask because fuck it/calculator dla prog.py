from tkinter import *
from tkinter import messagebox

def oblicz_bmi():
    try:
        waga = float(Entry1.get())
        wzrost = float(Entry2.get())
        if wzrost <= 0 or waga <= 0:
            raise ValueError

        bmi = waga / (wzrost ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            interpretacja = "Niedowaga"
        elif 18.5 <= bmi < 25:
            interpretacja = "Prawidłowa masa ciała"
        elif 25 <= bmi < 30:
            interpretacja = "Nadwaga"
        else:
            interpretacja = "Otyłość"

        wynik_label.config(text=f"BMI: {bmi} - {interpretacja}")
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawne dane liczbowe!")

def resetuj():
    Entry1.delete(0, END)
    Entry2.delete(0, END)
    wynik_label.config(text="")

window = Tk()
window.geometry("500x500")
window.title("Kalkulator grubastwa")

# Wybór płci
rad1 = Radiobutton(window, value=1, text="Mężczyzna")
rad1.grid(row=1, column=1)
rad2 = Radiobutton(window, value=2, text="Kobieta")
rad2.grid(row=1, column=2)

# Pole na wagę
Entry1 = Spinbox(window, from_=1, to=300)
Entry1.grid(row=2, column=2)
label1 = Label(window, text="Twoje KG")
label1.grid(row=2, column=1)

# Pole na wzrost
Entry2 = Spinbox(window, from_=0.5, to=2.5, increment=0.01)
Entry2.grid(row=3, column=2)
label2 = Label(window, text="Twój wzrost w M")
label2.grid(row=3, column=1)

# Przycisk do obliczenia BMI
button1 = Button(text="Skalkulatuj BMI", command=oblicz_bmi)
button1.grid(row=4, column=1)

# Przycisk resetujący
button2 = Button(text="Resetuj", command=resetuj)
button2.grid(row=4, column=2)

# Etykieta na wynik
wynik_label = Label(window, text="", font=("Arial", 14))
wynik_label.grid(row=5, column=1, columnspan=2)

window.mainloop()
