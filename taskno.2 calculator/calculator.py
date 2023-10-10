import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import platform

def on_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        calculate()
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

def on_key(event):
    key = event.char
    if key in '0123456789-+*/':
        screen.set(screen.get() + key)
    elif event.keysym == "Return":
        calculate()

def calculate():
    try:
        result = eval(screen.get())
        screen.set(result)
    except Exception as e:
        screen.set("Error")

def toggle_dark_mode():
    global bg_photo
    if dark_mode.get():
        root.configure(bg="black")
        
        for btn in button_objects:
            if btn.cget("text") in ('+', '-', '*', '/', '='):
                btn.configure(bg="orange", fg="white", activebackground="orange", activeforeground="white")
            else:
                btn.configure(bg="black", fg="white", activebackground="black", activeforeground="white")
        
        frame.configure(bg="black")
        dark_mode_button.configure(bg="black", fg="white", activebackground="black", activeforeground="white")
        
        bg_image = Image.open("t1.png")
        bg_image = bg_image.resize((400, 600), Image.BILINEAR)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label.configure(image=bg_photo)
        bg_label.image = bg_photo
        
    else:
        root.configure(bg="white")
        
        for btn in button_objects:
            if btn.cget("text") in ('+', '-', '*', '/', '='):
                btn.configure(bg="orange", fg="white", activebackground="orange", activeforeground="white")
            else:
                btn.configure(bg="white", fg="black", activebackground="white", activeforeground="black")
        
        frame.configure(bg="white")
        dark_mode_button.configure(bg="white", fg="black", activebackground="white", activeforeground="black")
        
        bg_image = Image.open("t2.png")
        bg_image = bg_image.resize((400, 600), Image.BILINEAR)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label.configure(image=bg_photo)
        bg_label.image = bg_photo

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

root.resizable(False, False)

if platform.system() == "Windows":
    root.attributes("-alpha", 1.0)

bg_image = Image.open("t2.png")
bg_image = bg_image.resize((400, 600), Image.BILINEAR)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

dark_mode = tk.BooleanVar()
dark_mode.set(False)

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 40 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10, anchor="n")

frame = tk.Frame(root, bg="white")
frame.pack()

button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0
button_objects = []

for label in button_labels:
    if label in ('+', '-', '*', '/', '='):
        btn = tk.Button(frame, text=label, font="lucida 25 bold", bg="orange", fg="white", activebackground="orange", activeforeground="white")
    else:
        btn = tk.Button(frame, text=label, font="lucida 25 bold")
    btn.grid(row=row, column=col, padx=10, pady=10)
    btn.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1
    button_objects.append(btn)

dark_mode_button = tk.Checkbutton(root, text="Dark Mode", variable=dark_mode, command=toggle_dark_mode, bg="white", fg="black", activebackground="white", activeforeground="black")
dark_mode_button.pack(pady=10)

root.bind("<Key>", on_key)

root.mainloop()
