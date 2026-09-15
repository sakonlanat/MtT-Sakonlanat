# นำเข้าโมดูลทั้ง 10 ตัว
from modules import m1_calc
from modules import m2_string
from modules import m3_datetime
from modules import m4_converter
from modules import m5_validator
from modules import m6_randomizer
from modules import m7_stats
from modules import m8_formatter
from modules import m9_geometry
from modules import m10_finance

def main():
    print("=== เริ่มทำงานโปรแกรมอเนกประสงค์ (10 Modules Ecosystem) ===")
    
    # 1. เรียกใช้ m1_calc
    print(f"[Module 1] ผลบวก 10 + 5 = {m1_calc.add(10, 5)}")
    
    # 2. เรียกใช้ m2_string
    print(f"[Module 2] คำกลับด้านของ 'Python' = {m2_string.reverse_text('Python')}")
    
    # 3. เรียกใช้ m3_datetime
    print(f"[Module 3] วันที่ปัจจุบันคือ = {m3_datetime.get_current_date()}")
    
    # 4. เรียกใช้ m4_converter
    print(f"[Module 4] แปลง 37°C เป็น ฟาเรนไฮต์ = {m4_converter.celsius_to_fahrenheit(37)}°F")
    
    # 5. เรียกใช้ m5_validator
    print(f"[Module 5] เลข 42 เป็นเลขคู่หรือไม่? = {m5_validator.is_even(42)}")
    
    # 6. เรียกใช้ m6_randomizer
    print(f"[Module 6] สุ่มเลขนำโชควันนี้ = {m6_randomizer.generate_lucky_number()}")
    
    # 7. เรียกใช้ m7_stats
    print(f"[Module 7] ค่าเฉลี่ยของ [10, 20, 30, 40] = {m7_stats.calculate_average([10, 20, 30, 40])}")
    
    # 8. เรียกใช้ m8_formatter
    print(f"[Module 8] จัดรูปแบบเงิน 1500000 = {m8_formatter.format_currency(1500000)}")
    
    # 9. เรียกใช้ m9_geometry
    print(f"[Module 9] พื้นที่วงกลม (รัศมี 5 ซม.) = {m9_geometry.area_of_circle(5):.2f} ตร.ซม.")
    
    # 10. เรียกใช้ m10_finance
    print(f"[Module 10] ดอกเบี้ยอย่างง่าย (เงินต้น 10,000, ดอกเบี้ย 5%, เวลา 2 ปี) = {m10_finance.simple_interest(10000, 5, 2)}")

    print("=================== ทำงานเสร็จสิ้น ===================")

if __name__ == "__main__":
    main()
