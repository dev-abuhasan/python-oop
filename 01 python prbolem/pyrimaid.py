
# n = int(input())

# for i in range(1, n + 1):
#     row = "#" * i 
#     print(row)



import tkinter as tk
import pyautogui

n = int(input("Enter the number of rows for the triangle pattern: "))

window = tk.Tk()
window.title("Triangle Pattern")
window.geometry("400x400")

for i in range(1, n + 1):
    row = "#" * i
    label = tk.Label(window, text=row, font=("Arial", 12))
    label.pack()

window.mainloop()
