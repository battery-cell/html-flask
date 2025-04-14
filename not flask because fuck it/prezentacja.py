import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser

root = tk.Tk()
root.title("Tkinter - 15 ciekawych elementów")
root.geometry("400x600")

# 1. Label – etykieta z tekstem
label = tk.Label(root, text="1. To jest Label", font=("Arial", 12))
label.pack(pady=5)

# 2. Button – przycisk z akcją
def on_click():
    messagebox.showinfo("Kliknięto", "Kliknięto przycisk!")

button = tk.Button(root, text="2. Kliknij mnie", command=on_click)
button.pack(pady=5)

# 3. Entry – pole tekstowe do wpisywania danych
entry = tk.Entry(root)
entry.pack(pady=5)
entry.insert(0, "3. Tu wpisz tekst")

# 4. Text – większe pole tekstowe
text = tk.Text(root, height=3, width=30)
text.insert(tk.END, "4. Większe pole tekstowe")
text.pack(pady=5)

# 5. Checkbutton – pole wyboru
check_var = tk.BooleanVar()
check = tk.Checkbutton(root, text="5. Zgadzam się", variable=check_var)
check.pack(pady=5)

# 6. Radiobutton – przyciski opcji
radio_var = tk.StringVar(value="Brak")
tk.Label(root, text="6. Wybierz opcję:").pack()
tk.Radiobutton(root, text="Opcja A", variable=radio_var, value="A").pack()
tk.Radiobutton(root, text="Opcja B", variable=radio_var, value="B").pack()

# 7. Listbox – lista wyboru
listbox = tk.Listbox(root)
for i in range(5):
    listbox.insert(tk.END, f"7. Element {i+1}")
listbox.pack(pady=5)

# 8. Scale – suwak
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="8. Wybierz wartość")
scale.pack(pady=5)

# 9. Spinbox – licznik
spin = tk.Spinbox(root, from_=0, to=10)
spin.pack(pady=5)

# 10. Messagebox – komunikaty
def show_warning():
    messagebox.showwarning("Uwaga", "To jest ostrzeżenie!")

warn_button = tk.Button(root, text="10. Ostrzeżenie", command=show_warning)
warn_button.pack(pady=5)

# 11. Canvas – rysowanie
canvas = tk.Canvas(root, width=100, height=50, bg="white")
canvas.create_oval(10, 10, 90, 40, fill="blue")
canvas.pack(pady=5)

# 12. Menu – menu główne
def say_hello():
    messagebox.showinfo("Menu", "Cześć!")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="12. Powiedz Cześć", command=say_hello)
menu_bar.add_cascade(label="Plik", menu=file_menu)
root.config(menu=menu_bar)

# 13. filedialog – wybór pliku
def choose_file():
    file_path = filedialog.askopenfilename()
    messagebox.showinfo("Wybrano plik", file_path)

file_btn = tk.Button(root, text="13. Wybierz plik", command=choose_file)
file_btn.pack(pady=5)

# 14. colorchooser – wybór koloru
def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        root.config(bg=color)

color_btn = tk.Button(root, text="14. Wybierz kolor tła", command=choose_color)
color_btn.pack(pady=5)

# 15. Frame – ramka do organizacji elementów
frame = tk.Frame(root, borderwidth=2, relief="groove")
tk.Label(frame, text="15. To jest w ramce").pack()
frame.pack(pady=10)

root.mainloop()
