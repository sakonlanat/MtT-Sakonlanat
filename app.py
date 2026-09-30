import os
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# กำหนดพาธของไฟล์ข้อมูล
DATA_DIR = "./Data"
FILE_PATH = os.path.join(DATA_DIR, "Mc.txt")

# สร้างโฟลเดอร์ Data ถ้ายังไม่มี
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# ฟังก์ชันบันทึกข้อมูล
def save_data():
    mc_id = entry_id.get().strip()
    volt = entry_volt.get().strip()
    amp = entry_amp.get().strip()
    
    if not mc_id or not volt or not amp:
        messagebox.showwarning("แจ้งเตือน", "กรุณากรอกข้อมูลให้ครบทุกช่อง")
        return
    
    try:
        # ตรวจสอบว่า Volt และ Amp เป็นตัวเลขหรือไม่
        float(volt)
        float(amp)
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "Volt และ Amp ต้องเป็นตัวเลขเท่านั้น")
        return

    # บันทึกข้อมูลลงไฟล์ (ต่อท้ายไฟล์)
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"{mc_id},{volt},{amp}\n")
        
    messagebox.showinfo("สำเร็จ", "บันทึกข้อมูลเรียบร้อยแล้ว")
    
    # ล้างช่องกรอกข้อมูล
    entry_id.delete(0, tk.END)
    entry_volt.delete(0, tk.END)
    entry_amp.delete(0, tk.END)
    
    # อัปเดตตารางและกราฟ
    load_data()

# ฟังก์ชันโหลดข้อมูลมาแสดงในตารางและเตรียมไว้สำหรับพล็อต
def load_data():
    # ล้างข้อมูลเดิมในตาราง
    for item in tree.get_children():
        tree.delete(item)
        
    if not os.path.exists(FILE_PATH):
        return [], [], []

    ids, volts, amps = [], [], []
    
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 3:
                    mc_id, volt, amp = parts
                    tree.insert("", tk.END, values=(mc_id, volt, amp))
                    ids.append(mc_id)
                    volts.append(float(volt))
                    amps.append(float(amp))
                    
    return ids, volts, amps

# ฟังก์ชันพล็อตเตอร์กราฟลงใน GUI
def plot_graph():
    ids, volts, amps = load_data()
    
    if not ids:
        messagebox.showwarning("แจ้งเตือน", "ไม่มีข้อมูลสำหรับพล็อตเตอร์กราฟ")
        return
        
    # เคลียร์กราฟเก่า
    ax1.clear()
    ax2.clear()
    
    x = range(len(ids))
    
    # พล็อต Volt (แกนซ้าย)
    color = 'tab:blue'
    ax1.set_xlabel('Machine ID')
    ax1.set_ylabel('Volt (V)', color=color)
    ax1.plot(x, volts, color=color, marker='o', linestyle='-', label='Volt')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_xticks(x)
    ax1.set_xticklabels(ids, rotation=45)
    
    # พล็อต Amp (แกนขวา)
    color = 'tab:red'
    ax2.set_ylabel('Amp (A)', color=color)
    ax2.plot(x, amps, color=color, marker='x', linestyle='--', label='Amp')
    ax2.tick_params(axis='y', labelcolor=color)
    
    fig.tight_layout()
    canvas.draw()

# สร้างหน้าต่างหลัก GUI
root = tk.Tk()
root.title("ระบบบันทึกและแสดงผลข้อมูล ID, Volt, Amp")
root.geometry("800x600")

# ส่วนกรอกข้อมูล (Input Frame)
frame_input = tk.LabelFrame(root, text=" กรอกข้อมูล Machine ", padx=10, pady=10)
frame_input.pack(fill="x", padx=15, pady=10)

tk.Label(frame_input, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_id = tk.Entry(frame_input)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Volt:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
entry_volt = tk.Entry(frame_input)
entry_volt.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_input, text="Amp:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
entry_amp = tk.Entry(frame_input)
entry_amp.grid(row=0, column=5, padx=5, pady=5)

btn_save = tk.Button(frame_input, text="บันทึกข้อมูล", command=save_data, bg="#4CAF50", fg="white", width=12)
btn_save.grid(row=0, column=6, padx=15, pady=5)

# ส่วนแสดงผล (Data Frame Split)
frame_display = tk.Frame(root)
frame_display.pack(fill="both", expand=True, padx=15, pady=5)

# ฝั่งซ้าย: ตาราง (Treeview)
frame_table = tk.LabelFrame(frame_display, text=" รายการข้อมูลในไฟล์ ", padx=5, pady=5)
frame_table.pack(side="left", fill="both", expand=True, padx=(0, 5))

columns = ("id", "volt", "amp")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
tree.heading("id", text="Machine ID")
tree.heading("volt", text="Volt (V)")
tree.heading("amp", text="Amp (A)")
tree.column("id", width=100, anchor="center")
tree.column("volt", width=80, anchor="center")
tree.column("amp", width=80, anchor="center")

scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# ฝั่งขวา: กราฟ (Matplotlib Chart)
frame_graph = tk.LabelFrame(frame_display, text=" กราฟแสดงผล ", padx=5, pady=5)
frame_graph.pack(side="right", fill="both", expand=True, padx=(5, 0))

btn_plot = tk.Button(frame_graph, text="อัปเดต / พล็อตเตอร์กราฟ", command=plot_graph, bg="#008CBA", fg="white")
btn_plot.pack(fill="x", pady=5)

# เตรียม Figure สำหรับพล็อตใน Tkinter (มี 2 แกน Y ร่วมกัน)
fig, ax1 = plt.subplots(figsize=(4, 3))
ax2 = ax1.twinx()
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
canvas.get_tk_widget().pack(fill="both", expand=True)

# โหลดข้อมูลครั้งแรกเมื่อเปิดโปรแกรม
load_data()

# เริ่มรัน GUI
root.mainloop()
