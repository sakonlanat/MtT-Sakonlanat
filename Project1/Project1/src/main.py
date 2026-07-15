import sys
import os
import importlib.util

# 1. หาตำแหน่งของโฟลเดอร์ที่ไฟล์ main.py นี้ตั้งอยู่จริงๆ
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. บังคับชี้เป้าไปที่ไฟล์ snake_game.py ที่อยู่ในโฟลเดอร์เดียวกันโดยตรง (Absolute Path)
snake_game_path = os.path.join(current_dir, "snake_game.py")

# 3. โหลดโมดูลเกมเข้ามาทำงานโดยตรงจากตำแหน่งไฟล์ (ไม่ผ่านระบบค้นหาปกติของ Python)
spec = importlib.util.spec_from_file_location("snake_game", snake_game_path)
if spec is None or spec.loader is None:
    raise ImportError(f"ไม่สามารถโหลดไฟล์เกมจากตำแหน่งนี้ได้: {snake_game_path}")
snake_game = importlib.util.module_from_spec(spec)
spec.loader.exec_module(snake_game)

# 4. จัดการระบบ Path สำหรับเครื่องคิดเลข
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
from src.calpkg.calculator import add, subtract


def main():
    # ทำงานส่วนคำนวณของเครื่องคิดเลข
    print("Hello, World!")
    a = 5
    b = 3
    result_add = add(a, b)
    print(f"the sum of {a} and {b} is: {result_add}")
    result_subtract = subtract(a, b)
    print(f"the difference of {a} and {b} is: {result_subtract}")
    
    # ทำงานส่วนเรียกเปิดเกมงู
    print("\nกำลังเปิดเกมงู...")
    snake_game.start_game()

if __name__ == "__main__":
    main()
