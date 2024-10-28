import tkinter as tk
def fn_click():
    label.config(text="Boommm🎆🔥")


window = tk.Tk()
window.title("Button app")
window.geometry("400x250")

label = tk.Label(window, text="Hello Man")
label.pack(pady=30)

button = tk.Button(window, text="Click here", command=fn_click)
button.pack(pady=10)
window.mainloop()