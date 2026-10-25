import tkinter as tk
import random

def lottery():
    first.config(text=f"{random.randint(0,999999):06d}")
    front.config(text=f"{random.randint(0,999):03d}   {random.randint(0,999):03d}")
    back3.config(text=f"{random.randint(0,999):03d}   {random.randint(0,999):03d}")
    back2.config(text=f"{random.randint(0,99):02d}")

app = tk.Tk()
app.title("โปรแกรมสุ่มตัวเลข")
app.geometry("300x300")

tk.Label(app, text="โปรแกรมสุ่มตัวเลข", font=("Arial", 14, "bold")).pack()

tk.Label(app, text="รางวัลที่ 1").pack()
first = tk.Label(app, text="------", font=("Arial", 18), fg="red")
first.pack()

tk.Label(app, text="เลขหน้า 3 ตัว").pack()
front = tk.Label(app, text="---   ---", font=("Arial", 14))
front.pack()

tk.Label(app, text="เลขท้าย 3 ตัว").pack()
back3 = tk.Label(app, text="---   ---", font=("Arial", 14))
back3.pack()

tk.Label(app, text="เลขท้าย 2 ตัว").pack()
back2 = tk.Label(app, text="--", font=("Arial", 16))
back2.pack()

tk.Button(app, text="สุ่มเลข", command=lottery).pack(pady=10)

app.mainloop()