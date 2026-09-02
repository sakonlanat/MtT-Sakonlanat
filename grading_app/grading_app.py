import tkinter as tk
from tkinter import messagebox, ttk


def calculate_all_grades():
    try:
        results = []
        has_data = False

        # ลูปดึงข้อมูลจากแถวทั้ง 20 คน
        for i in range(20):
            name = entry_rows[i]["name"].get().strip()
            mid_str = entry_rows[i]["mid"].get().strip()
            final_str = entry_rows[i]["final"].get().strip()

            # ถ้าไม่มีข้อมูลในแถวนั้นเลย ให้ข้ามไป
            if not name and not mid_str and not final_str:
                continue

            # ถ้ากรอกบางช่องแต่ไม่ครบ ให้แจ้งเตือน
            if not name or not mid_str or not final_str:
                messagebox.showerror(
                    "ข้อมูลไม่ครบ",
                    f"กรุณากรอกข้อมูลของลำดับที่ {i+1} ให้ครบทุกช่อง",
                )
                return

            has_data = True
            mid = float(mid_str)
            final = float(final_str)

            # ตรวจสอบช่วงคะแนน
            if not (0 <= mid <= 50 and 0 <= final <= 50):
                messagebox.showerror(
                    "คะแนนไม่ถูกต้อง",
                    f"ลำดับที่ {i+1}: คะแนน Midterm และ Final ต้องอยู่ระหว่าง 0 - 50",
                )
                return

            total = mid + final

            # เกณฑ์การตัดเกรด
            if total >= 80:
                grade = "A"
            elif total >= 70:
                grade = "B"
            elif total >= 60:
                grade = "C"
            elif total >= 50:
                grade = "D"
            else:
                grade = "F"

            results.append((name, total, grade))

        if not has_data:
            messagebox.showwarning(
                "ไม่มีข้อมูล", "กรุณากรอกข้อมูลนักศึกษาอย่างน้อย 1 คน"
            )
            return

        # แสดงผลลัพธ์ในตารางสรุปด้านขวา
        for item in tree.get_children():
            tree.delete(item)

        for name, total, grade in results:
            tree.insert("", "end", values=(name, f"{total:.2f}", grade))

    except ValueError:
        messagebox.showerror(
            "ข้อผิดพลาด", "กรุณากรอกคะแนนเป็นตัวเลขเท่านั้น (ใช้จุดทศนิยมได้)"
        )


# สร้างหน้าต่างหลักแบบ Wide-Screen
root = tk.Tk()
root.title("Basic Computer Programming - Grading System")
root.geometry("1000x650")
root.configure(bg="#F4F6F9")

# ปรับแต่งสไตล์ของวัตถุควบคุม (TTK Style)
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TLabel", background="#F4F6F9", font=("Helvetica", 10), foreground="#333333"
)
style.configure(
    "Title.TLabel", font=("Helvetica", 16, "bold"), foreground="#2C3E50"
)
style.configure(
    "Heading.TLabel", font=("Helvetica", 11, "bold"), foreground="#4A5568"
)

# --- ส่วนหัวโปรแกรม ---
header_frame = tk.Frame(root, bg="#2C3E50", height=60)
header_frame.pack(fill="x", side="top")
header_frame.pack_propagate(False)

title_label = tk.Label(
    header_frame,
    text="Basic Computer Programming Grading System (20 Students)",
    font=("Helvetica", 14, "bold"),
    fg="white",
    bg="#2C3E50",
)
title_label.pack(pady=15)

# --- ส่วนเนื้อหาหลัก (แบ่งซ้าย-ขวา) ---
main_container = tk.Frame(root, bg="#F4F6F9")
main_container.pack(fill="both", expand=True, padx=20, pady=15)

# ฝั่งซ้าย: ส่วนกรอกข้อมูล (พร้อมแถบเลื่อน Scrollbar)
left_frame = tk.LabelFrame(
    main_container,
    text=" กรอกข้อมูลนักศึกษา ",
    font=("Helvetica", 11, "bold"),
    bg="#FFFFFF",
    fg="#2C3E50",
    bd=2,
    relief="groove",
)
left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

# การสร้าง Canvas เพื่อทำให้พื้นที่กรอกข้อมูลเลื่อนขึ้น-ลงได้
canvas = tk.Canvas(left_frame, bg="#FFFFFF", highlightthickness=0)
scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#FFFFFF")

scrollable_frame.bind(
    "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True, padx=5, pady=5)
scrollbar.pack(side="right", fill="y")

# หัวตารางสำหรับกรอกข้อมูล
ttk.Label(scrollable_frame, text="ลำดับ", style="Heading.TLabel").grid(
    row=0, column=0, padx=5, pady=5
)
ttk.Label(
    scrollable_frame, text="ชื่อ - นามสกุล", style="Heading.TLabel"
).grid(row=0, column=1, padx=5, pady=5)
ttk.Label(
    scrollable_frame, text="Midterm (50)", style="Heading.TLabel"
).grid(row=0, column=2, padx=5, pady=5)
ttk.Label(scrollable_frame, text="Final (50)", style="Heading.TLabel").grid(
    row=0, column=3, padx=5, pady=5
)

# สร้างช่องกรอกข้อมูล 20 แถว
entry_rows = []
for i in range(20):
    bg_color = "#F8FAFC" if i % 2 == 0 else "#FFFFFF"
    row_frame = tk.Frame(scrollable_frame, bg=bg_color)
    row_frame.grid(row=i + 1, column=0, columnspan=4, sticky="ew", pady=2)

    # เลขลำดับ
    lbl_num = tk.Label(
        row_frame,
        text=f"{i+1:02d}",
        width=4,
        font=("Helvetica", 10, "bold"),
        fg="#718096",
        bg=bg_color,
    )
    lbl_num.pack(side="left", padx=5, pady=4)

    # ช่องชื่อ
    ent_name = tk.Entry(
        row_frame,
        width=22,
        font=("Helvetica", 10),
        bd=1,
        relief="solid",
        highlightthickness=1,
        highlightbackground="#E2E8F0",
    )
    ent_name.pack(side="left", padx=5, pady=4)

    # ช่อง Midterm
    ent_mid = tk.Entry(
        row_frame,
        width=10,
        font=("Helvetica", 10),
        justify="center",
        bd=1,
        relief="solid",
        highlightthickness=1,
        highlightbackground="#E2E8F0",
    )
    ent_mid.pack(side="left", padx=12, pady=4)

    # ช่อง Final
    ent_final = tk.Entry(
        row_frame,
        width=10,
        font=("Helvetica", 10),
        justify="center",
        bd=1,
        relief="solid",
        highlightthickness=1,
        highlightbackground="#E2E8F0",
    )
    ent_final.pack(side="left", padx=10, pady=4)

    entry_rows.append({"name": ent_name, "mid": ent_mid, "final": ent_final})

# ฝั่งขวา: ส่วนแสดงผลลัพธ์และปุ่มคำนวณ
right_frame = tk.Frame(main_container, bg="#F4F6F9", width=400)
right_frame.pack(side="right", fill="both", padx=(10, 0))

# ปุ่มคำนวณสไตล์โมเดิร์น
btn_calculate = tk.Button(
    right_frame,
    text=" Calculate & Grade ",
    command=calculate_all_grades,
    bg="#10B981",
    fg="white",
    font=("Helvetica", 12, "bold"),
    bd=0,
    cursor="hand2",
    activebackground="#059669",
    activeforeground="white",
    height=2,
)
btn_calculate.pack(fill="x", pady=(0, 15))

# ตารางแสดงผลสรุปเกรด (Treeview)
result_box = tk.LabelFrame(
    right_frame,
    text=" สรุปผลการเรียน ",
    font=("Helvetica", 11, "bold"),
    bg="#FFFFFF",
    fg="#2C3E50",
    bd=2,
    relief="groove",
)
result_box.pack(fill="both", expand=True)

columns = ("name", "total", "grade")
tree = ttk.Treeview(result_box, columns=columns, show="headings")

tree.heading("name", text="ชื่อ - นามสกุล")
tree.heading("total", text="คะแนนรวม")
tree.heading("grade", text="เกรด")

tree.column("name", width=180, anchor="w")
tree.column("total", width=90, anchor="center")
tree.column("grade", width=70, anchor="center")

# ปรับแต่งสีตารางผลลัพธ์
style.configure(
    "Treeview",
    rowheight=25,
    font=("Helvetica", 10),
    background="#FFFFFF",
    fieldbackground="#FFFFFF",
)
style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))

tree.pack(fill="both", expand=True, padx=5, pady=5)

root.mainloop()
