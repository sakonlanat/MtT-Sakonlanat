import tkinter as tk
from tkinter import ttk, messagebox

# ==========================================
# 1. ส่วนของ Logic ฟังก์ชันจัดการ String
# ==========================================
def process_string():
    input_text = entry_input.get()
    search_word = entry_search.get()
    
    if not input_text:
        messagebox.showwarning("คำเตือน", "กรุณากรอกข้อความเริ่มต้นก่อนครับ")
        return

    # ล้างค่าในตารางผลลัพธ์เก่าก่อน
    for item in tree.get_children():
        tree.delete(item)

    # ------------------------------------------
    # หมวดการค้นหา (Searching Functions)
    # ------------------------------------------
    # 1. find()
    idx_find = input_text.find(search_word) if search_word else "ไม่ได้ระบุคำค้น"
    tree.insert("", "end", values=("1. find()", f"ค้นหาตำแหน่ง '{search_word}'", str(idx_find)))
    
    # 2. index()
    if search_word:
        try:
            idx_index = input_text.index(search_word)
        except ValueError:
            idx_index = "ไม่พบข้อความ (Error)"
    else:
        idx_index = "ไม่ได้ระบุคำค้น"
    tree.insert("", "end", values=("2. index()", f"ค้นหาดัชนี '{search_word}'", str(idx_index)))
    
    # 3. count()
    cnt = input_text.count(search_word) if search_word else 0
    tree.insert("", "end", values=("3. count()", f"นับจำนวนคำว่า '{search_word}'", f"พบ {cnt} ครั้ง"))
    
    # 4. startswith()
    is_start = input_text.strip().startswith(search_word) if search_word else "ไม่ได้ระบุคำค้น"
    tree.insert("", "end", values=("4. startswith()", f"ขึ้นต้นด้วย '{search_word}' หรือไม่?", str(is_start)))
    
    # 5. endswith()
    is_end = input_text.strip().endswith(search_word) if search_word else "ไม่ได้ระบุคำค้น"
    tree.insert("", "end", values=("5. endswith()", f"ลงท้ายด้วย '{search_word}' หรือไม่?", str(is_end)))

    # ------------------------------------------
    # หมวดการจัดรูปแบบ (Formatting Functions)
    # ------------------------------------------
    # 6. strip()
    tree.insert("", "end", values=("6. strip()", "ตัดช่องว่างหน้า-หลังออก", f"'{input_text.strip()}'"))
    
    # 7. replace()
    rep = input_text.replace(search_word, "[เปลี่ยนแล้ว]") if search_word else input_text
    tree.insert("", "end", values=("7. replace()", f"แทนที่ '{search_word}' ด้วย [เปลี่ยนแล้ว]", rep))
    
    # 8. upper() & lower()
    tree.insert("", "end", values=("8. upper() / lower()", "แปลงตัวพิมพ์ใหญ่ / เล็ก", f"ใหญ่: {input_text.upper()} | เล็ก: {input_text.lower()}"))
    
    # 9. center()
    tree.insert("", "end", values=("9. center()", "จัดกึ่งกลางความกว้าง 50 เติม -", input_text.strip().center(50, "-")))
    
    # 10. f-strings
    f_res = f"ข้อความของคุณมีความยาวทั้งสิ้น {len(input_text):03d} ตัวอักษร"
    tree.insert("", "end", values=("10. f-strings", "จัดฟอร์แมตความยาวด้วย f-string :03d", f_res))

# ==========================================
# 2. ส่วนของการสร้างหน้าจอ GUI (Tkinter)
# ==========================================
root = tk.Tk()
root.title("โปรแกรมสาธิต 10 String Functions")
root.geometry("800x550")
root.configure(bg="#f5f5f5")

# สไตล์ส่วนควบคุม
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
style.configure("Treeview", font=("Helvetica", 10), rowheight=25)

# ส่วนกรอกข้อมูล (Inputs)
frame_input = tk.LabelFrame(root, text=" ส่วนข้อมูลนำเข้า ", font=("Helvetica", 11, "bold"), bg="#f5f5f5", padx=15, pady=10)
frame_input.pack(fill="x", padx=15, pady=10)

tk.Label(frame_input, text="1. กรอกข้อความเริ่มต้น (String):", font=("Helvetica", 10), bg="#f5f5f5").grid(row=0, column=0, sticky="w", pady=5)
entry_input = ttk.Entry(frame_input, width=60)
entry_input.grid(row=0, column=1, padx=10, pady=5)
entry_input.insert(0, "   Hello, Welcome to Python Programming World!   ") # ค่าเริ่มต้นตัวอย่าง

tk.Label(frame_input, text="2. คำค้นหา/แทนที่ (Search Keyword):", font=("Helvetica", 10), bg="#f5f5f5").grid(row=1, column=0, sticky="w", pady=5)
entry_search = ttk.Entry(frame_input, width=30)
entry_search.grid(row=1, column=1, sticky="w", padx=10, pady=5)
entry_search.insert(0, "Python") # ค่าเริ่มต้นตัวอย่าง

# ปุ่มประมวลผล
btn_process = ttk.Button(frame_input, text="ประมวลผลข้อความ", command=process_string)
btn_process.grid(row=2, column=1, sticky="e", pady=10)

# ส่วนแสดงผลลัพธ์ (Output Table)
frame_output = tk.LabelFrame(root, text=" ผลลัพธ์การทำงานของ 10 Functions ", font=("Helvetica", 11, "bold"), bg="#f5f5f5", padx=15, pady=10)
frame_output.pack(fill="both", expand=True, padx=15, pady=5)

# สร้างตาราง Treeview
columns = ("function", "description", "result")
tree = ttk.Treeview(frame_output, columns=columns, show="headings")

# กำหนดหัวข้อคอลัมน์
tree.heading("function", text="ฟังก์ชัน (Methods)")
tree.heading("description", text="คำอธิบายการทดสอบ")
tree.heading("result", text="ผลลัพธ์ที่ได้ (Result)")

# กำหนดความกว้างคอลัมน์
tree.column("function", width=150, anchor="w")
tree.column("description", width=250, anchor="w")
tree.column("result", width=350, anchor="w")

# แถบเลื่อน (Scrollbar)
scrollbar = ttk.Scrollbar(frame_output, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# สั่งให้รันฟังก์ชันครั้งแรกทันทีตอนเปิดโปรแกรม เพื่อแสดงตัวอย่าง
process_string()

# เริ่มทำงานโปรแกรม GUI
root.mainloop()
