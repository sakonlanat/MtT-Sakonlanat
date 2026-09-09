import mymodule as mx
import platform

from mymodule import greeting, person1

# คำสั่งในบรรทัดที่ 6 ของรูปภาพ (แก้ข้อผิดพลาดเรื่องวงเล็บ)
print(person1["age"]) 

x = platform.system()
print(x) # หมายเหตุ: ในรูปพิมพ์ผิดเป็น pront ให้แก้เป็น print ครับ

x = dir(platform)
print(x)

mx.greeting("Jonathan")

a = mx.person1["age"]
print(a)

