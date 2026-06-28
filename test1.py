# รับค่าน้ำหนักและส่วนสูงจากผู้ใช้
weight = float(input("กรอกน้ำหนัก (กิโลกรัม): "))
height = float(input("กรอกส่วนสูง (เมตร): "))

# คำนวณ BMI
bmi = weight / (height ** 2)

# แสดงผล
print(f"\nค่า BMI ของคุณคือ: {bmi:.2f}")

# แปลผล BMI
if bmi < 18.5:
    print("อยู่ในเกณฑ์น้ำหนักน้อย")
elif bmi < 25:
    print("อยู่ในเกณฑ์ปกติ")
elif bmi < 30:
    print("อยู่ในเกณฑ์น้ำหนักเกิน")
else:
    print("อยู่ในเกณฑ์อ้วน")