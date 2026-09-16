import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re

class RegexToolkitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Regex GUI Toolkit (10+ Functions)")
        self.root.geometry("950x700")
        
        # 1. ส่วนจัดวาง UI หลัก
        self.setup_ui()
        
    def setup_ui(self):
        # แถบบน: โหลด/ล้างข้อมูล
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill=tk.X)
        ttk.Button(top_frame, text="โหลดไฟล์ข้อความ (.txt)", command=self.load_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(top_frame, text="ล้างข้อมูลทั้งหมด", command=self.clear_all).pack(side=tk.LEFT, padx=5)
        
        # ส่วนแสดงผล: แบ่งซ้าย-ขวา
        paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # ฝั่งซ้าย (Input)
        f_left = ttk.LabelFrame(paned, text=" ข้อความต้นฉบับ (Input Text) ", padding=5)
        self.input_text = tk.Text(f_left, wrap=tk.WORD, font=("Courier New", 10))
        self.input_text.pack(fill=tk.BOTH, expand=True)
        paned.add(f_left, weight=1)
        
        # ฝั่งขวา (Output)
        f_right = ttk.LabelFrame(paned, text=" ผลลัพธ์การประมวลผล (Output Result) ", padding=5)
        self.output_text = tk.Text(f_right, wrap=tk.WORD, font=("Courier New", 10), bg="#f8f9fa")
        self.output_text.pack(fill=tk.BOTH, expand=True)
        paned.add(f_right, weight=1)
        
        # แถบล่าง: ควบคุมพารามิเตอร์
        ctrl_frame = ttk.LabelFrame(self.root, text=" เครื่องมือประมวลผล Regex ", padding=10)
        ctrl_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # เลือกฟังก์ชัน
        ttk.Label(ctrl_frame, text="เลือกฟังก์ชัน:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.functions_list = [
            "1. re.findall (หาข้อความทั้งหมด)",
            "2. re.finditer (หาตำแหน่ง Start-End)",
            "3. re.search (หาคำแรกที่เจอ)",
            "4. re.match (ตรวจสอบคำขึ้นต้นประโยค)",
            "5. re.fullmatch (ตรงกับ Pattern ทั้งหมด 100%)",
            "6. re.sub (ค้นหาและแทนที่ข้อความ)",
            "7. re.subn (แทนที่ข้อความ + นับจำนวน)",
            "8. re.split (ตัดแบ่งข้อความ)",
            "9. re.escape (แปลงข้อความเป็น Regex Safe)",
            "10. Custom Extract (สกัด อีเมล/เบอร์โทร/URL)"
        ]
        self.func_combo = ttk.Combobox(ctrl_frame, values=self.functions_list, width=40, state="readonly")
        self.func_combo.current(0)
        self.func_combo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.func_combo.bind("<<ComboboxSelected>>", self.on_function_change)
        
        # Regex Pattern
        ttk.Label(ctrl_frame, text="Regex Pattern:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.pattern_entry = ttk.Entry(ctrl_frame, width=40)
        self.pattern_entry.insert(0, r"\d+")
        self.pattern_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Replace Text (ใช้เฉพาะฟังก์ชัน 6 และ 7)
        self.repl_label = ttk.Label(ctrl_frame, text="คำที่แทนที่ (Replace):")
        self.repl_entry = ttk.Entry(ctrl_frame, width=25)
        
        # ปุ่มประมวลผล
        ttk.Button(ctrl_frame, text="ประมวลผลข้อมูล", command=self.process_regex).grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

    def on_function_change(self, event):
        selected = self.func_combo.get()
        # เปิด/ซ่อน ช่องแทนที่คำตามฟังก์ชันที่เลือก
        if "re.sub" in selected or "re.subn" in selected:
            self.repl_label.grid(row=1, column=2, sticky=tk.W, padx=10, pady=5)
            self.repl_entry.grid(row=1, column=3, sticky=tk.W, padx=5, pady=5)
        else:
            self.repl_label.grid_forget()
            self.repl_entry.grid_forget()
            
        # เปิด/ปิด ช่องกรอก Pattern อัตโนมัติ
        if "Custom Extract" in selected:
            self.pattern_entry.delete(0, tk.END)
            self.pattern_entry.insert(0, "ระบบสกัดข้อมูลอัตโนมัติ")
            self.pattern_entry.config(state="disabled")
        else:
            self.pattern_entry.config(state="normal")

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.input_text.delete("1.0", tk.END)
                    self.input_text.insert("1.0", f.read())
            except Exception as e:
                messagebox.showerror("Error", f"อ่านไฟล์ล้มเหลว: {str(e)}")

    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

    # 2. ส่วนคำนวณและแยก Logic ออกเป็นฟังก์ชันเพื่อลดการซ้อนของโค้ด
    def execute_regex_logic(self, func_name, pattern, text):
        if "1. re.findall" in func_name:
            res = re.findall(pattern, text)
            return f"--- พบทั้งหมด {len(res)} รายการ ---\n\n" + "\n".join(res)
            
        elif "2. re.finditer" in func_name:
            matches = list(re.finditer(pattern, text))
            out = f"--- รายละเอียดตำแหน่ง ({len(matches)} จุด) ---\n"
            for i, m in enumerate(matches, 1):
                out += f"{i}. พบ '{m.group()}' ที่ index [{m.start()}:{m.end()}]\n"
            return out
            
        elif "3. re.search" in func_name:
            m = re.search(pattern, text)
            if m:
                return f"--- เจอผลลัพธ์แรก ---\nคำที่เจอ: {m.group()}\nIndex: [{m.start()}:{m.end()}]\nGroups: {m.groups()}"
            return "ไม่พบข้อมูลที่ตรงกับ Pattern"
            
        elif "4. re.match" in func_name:
            m = re.match(pattern, text)
            if m:
                return f"พบ Pattern ตรงเงื่อนไขที่ 'ต้นข้อความ':\n{m.group()}"
            return "ข้อความนี้ไม่ได้ขึ้นต้นด้วย Pattern นี้"
            
        elif "5. re.fullmatch" in func_name:
            m = re.fullmatch(pattern, text)
            return "ตรงกับ Pattern ทั้งหมด 100%" if m else "ข้อความทั้งหมดไม่ตรงกับ Pattern แบบร้อยเปอร์เซ็นต์"
            
        elif "6. re.sub" in func_name:
            return f"--- ผลลัพธ์หลังแทนที่ ---\n\n{re.sub(pattern, self.repl_entry.get(), text)}"
            
        elif "7. re.subn" in func_name:
            txt, count = re.subn(pattern, self.repl_entry.get(), text)
            return f"--- แทนที่สำเร็จ {count} จุด ---\n\n{txt}"
            
        elif "8. re.split" in func_name:
            lst = re.split(pattern, text)
            out = f"--- ตัดแบ่งได้ {len(lst)} ส่วน ---\n\n"
            for i, seg in enumerate(lst, 1):
                out += f"ส่วนที่ {i}: {seg}\n"
            return out
            
        elif "9. re.escape" in func_name:
            return f"คำเดิม: {pattern}\nแปลงเป็น Regex Safe: {re.escape(pattern)}"
            
        elif "10. Custom Extract" in func_name:
            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
            phones = re.findall(r'(?:0\d{1,2}[-]?\d{3}[-]?\d{4}|0\d{1,2}\s?\d{3}\s?\d{4})', text)
            urls = re.findall(r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b', text)
            return (f"--- สกัดข้อมูลอัตโนมัติ ---\n\n"
                    f"📧 อีเมล ({len(emails)}):\n" + "\n".join(set(emails)) + "\n\n"
                    f"📞 เบอร์โทร ({len(phones)}):\n" + "\n".join(set(phones)) + "\n\n"
                    f"🌐 URL ({len(urls)}):\n" + "\n".join(set(urls)))
        return "ไม่พบฟังก์ชันที่เลือก"

    # 3. Main Process ควบคุมด้วย Try-Except อย่างปลอดภัย
    def process_regex(self):
        self.output_text.delete("1.0", tk.END)
        text_content = self.input_text.get("1.0", tk.END).strip()
        pattern = self.pattern_entry.get()
        selected_func = self.func_combo.get()
        
        if not text_content and "re.escape" not in selected_func:
            messagebox.showwarning("คำเตือน", "กรุณาใส่ข้อความต้นฉบับฝั่งซ้ายก่อน")
            return

        try:
            # ประมวลผลและนำคำตอบไปแสดงฝั่งขวา
            result = self.execute_regex_logic(selected_func, pattern, text_content)
            self.output_text.insert("1.0", result)
            
        except re.error as regex_err:
            # ดักจับเมื่อเขียน Syntax Regex ผิดพลาด
            err_msg = f"ไวยากรณ์ Regex ผิดพลาด (Invalid Pattern):\n{str(regex_err)}"
            self.output_text.insert("1.0", f"🚨 REGEX ERROR:\n{err_msg}")
            messagebox.showerror("Regex Error", err_msg)
            
        except Exception as e:
            # ดักจับ Error ทั่วไปอื่นๆ
            err_msg = f"เกิดข้อผิดพลาด: {str(e)}"
            self.output_text.insert("1.0", f"🚨 RUNTIME ERROR:\n{err_msg}")
            messagebox.showerror("Runtime Error", err_msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = RegexToolkitApp(root)
    root.mainloop()
