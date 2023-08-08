import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Face Recognition system")

l1 = tk.Label(window, text="Name", font=("Algerian",20))
l1.grid(column=0, row=0)
t1 = tk.Entry(window, width=50, bd=5)
t1.grid(column=1, row=0)

l2 = tk.Label(window, text="Age", font=("Algerian",20))
l2.grid(column=0, row=1)
t2 = tk.Entry(window, width=50, bd=5)
t2.grid(column=1, row=1)

l3 = tk.Label(window, text="Address", font=("Algerian",20))
l3.grid(column=0, row=2)
t3 = tk.Entry(window, width=50, bd=5)
t3.grid(column=1, row=2)


b1 = tk.Button(window, text="Training", font=("Algerian",20),bg="orange",fg="red")
b1.grid(column=0, row=4)

b2 = tk.Button(window, text="Detect the faces", font=("Algerian",20), bg="green", fg="orange")
b2.grid(column=1, row=4)

b3 = tk.Button(window, text="Generate dataset", font=("Algerian",20), bg="pink", fg="black")
b3.grid(column=2, row=4)

window.geometry("800x200")
window.mainloop()