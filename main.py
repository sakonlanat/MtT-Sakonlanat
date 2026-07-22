import tkinter as tk
from tkinter import messagebox
import snake_game
import guess_number


# --------------------------
# เปิดเกมงู
# --------------------------
def open_snake():
    root.withdraw()  # ซ่อนหน้าเมนู

    try:
        snake_game.start_game()
    except Exception as e:
        messagebox.showerror("Error", str(e))

    root.deiconify()  # แสดงหน้าเมนูอีกครั้ง


# --------------------------
# เปิดเกมทายตัวเลข
# --------------------------
def open_guess():
    root.withdraw()

    try:
        guess_number.start_game()
    except Exception as e:
        messagebox.showerror("Error", str(e))

    root.deiconify()


# --------------------------
# สร้างหน้าต่างหลัก
# --------------------------
root = tk.Tk()
root.title("Mini Game Project")
root.geometry("450x350")
root.resizable(False, False)
root.configure(bg="#2C3E50")


# --------------------------
# หัวข้อ
# --------------------------
title = tk.Label(
    root,
    text="🎮 MINI GAME PROJECT 🎮",
    font=("Arial", 20, "bold"),
    bg="#2C3E50",
    fg="white"
)
title.pack(pady=25)


# --------------------------
# ปุ่มเกมงู
# --------------------------
btn_snake = tk.Button(
    root,
    text="🐍 Snake Game",
    font=("Arial", 14, "bold"),
    bg="#27AE60",
    fg="white",
    width=20,
    height=2,
    command=open_snake
)
btn_snake.pack(pady=10)


# --------------------------
# ปุ่มเกมทายตัวเลข
# --------------------------
btn_guess = tk.Button(
    root,
    text="🔢 Guess Number",
    font=("Arial", 14, "bold"),
    bg="#2980B9",
    fg="white",
    width=20,
    height=2,
    command=open_guess
)
btn_guess.pack(pady=10)


# --------------------------
# ปุ่มออก
# --------------------------
btn_exit = tk.Button(
    root,
    text="❌ Exit",
    font=("Arial", 14, "bold"),
    bg="#C0392B",
    fg="white",
    width=20,
    height=2,
    command=root.destroy
)
btn_exit.pack(pady=20)


root.mainloop()