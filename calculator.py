import tkinter as tk

# -------------------------
# สร้างหน้าต่าง
# -------------------------
root = tk.Tk()
root.title("เครื่องคิดเลข")
root.geometry("420x620")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

expression = ""
equation = tk.StringVar()

# -------------------------
# ฟังก์ชัน
# -------------------------
def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# -------------------------
# ช่องแสดงผล
# -------------------------
display = tk.Entry(
    root,
    textvariable=equation,
    font=("Segoe UI", 28),
    justify="right",
    bg="#2d2d44",
    fg="white",
    relief="flat",
    bd=0
)

display.pack(fill="x", padx=15, pady=15, ipady=20)

# -------------------------
# เฟรมปุ่ม
# -------------------------
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(fill="both", expand=True, padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"]
]

btn_color = "#4A86E8"
op_color = "#F39C12"
clear_color = "#E74C3C"

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "C":
            color = clear_color
            cmd = clear

        elif text in ["+", "-", "*", "/"]:
            color = op_color
            cmd = lambda x=text: press(x)

        else:
            color = btn_color
            cmd = lambda x=text: press(x)

        button = tk.Button(
            frame,
            text=text,
            font=("Segoe UI", 20, "bold"),
            bg=color,
            fg="white",
            relief="flat",
            activebackground="#5B9CF2",
            activeforeground="white",
            command=cmd
        )

        button.grid(
            row=r,
            column=c,
            sticky="nsew",
            padx=6,
            pady=6
        )

# ทำให้ปุ่มขยายเต็มพื้นที่
for i in range(4):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

# -------------------------
# ปุ่ม =
# -------------------------
equal_btn = tk.Button(
    root,
    text="=",
    font=("Segoe UI", 24, "bold"),
    bg="#2ECC71",
    fg="white",
    relief="flat",
    activebackground="#27AE60",
    activeforeground="white",
    command=equal
)

equal_btn.pack(fill="x", padx=15, pady=(0,15), ipady=18)

root.mainloop()