import random
import time


class EsportsPlayer:
    """คลาสสำหรับจำลองข้อมูลและพฤติกรรมของนักแข่ง eSports"""

    def __init__(self, name: str, role: str, skill_level: int):
        # Properties (Attributes)
        self.name = name
        self.role = role
        self.skill_level = skill_level  # ระดับฝีมือ 1-100
        self.energy = 100  # พลังงานเริ่มต้น
        self.is_injured = False
        self.matches_played = 0
        self.kills = 0

    # Methods
    def train(self):
        """ฝึกซ้อมเพื่อเพิ่มระดับฝีมือ แต่จะเสียพลังงาน"""
        if self.energy > 20:
            self.skill_level += random.randint(1, 5)
            self.energy -= 15
            print(
                f"🏋️ {self.name} ฝึกซ้อมอย่างหนัก! ฝีมือเพิ่มเป็น {self.skill_level} (พลังงานเหลือ {self.energy}%)"
            )
        else:
            print(f"❌ {self.name} เหนื่อยเกินกว่าจะซ้อม กรุณาให้พักผ่อน")

    def rest(self):
        """พักผ่อนเพื่อฟื้นฟูพลังงาน"""
        self.energy = min(100, self.energy + 30)
        print(f"🛌 {self.name} ได้พักผ่อนอย่างเต็มอิ่ม พลังงานฟื้นฟูเป็น {self.energy}%")

    def play_match(self):
        """จำลองการเล่นแมตช์การแข่งขัน"""
        if self.energy < 30:
            print(f"⚠️ {self.name} พลังงานต่ำเกินไป เสี่ยงต่อการบาดเจ็บ!")
            if random.random() < 0.4:
                self.is_injured = True
                print(f"🚑 บาดเจ็บ! {self.name} ต้องพักรักษาตัว")
                return

        # คำนวณผลงานในเกม
        self.matches_played += 1
        self.energy -= 25
        match_kills = random.randint(1, 15) + (self.skill_level // 10)
        self.kills += match_kills
        print(f"🎮 {self.name} ลงแข่งแมตช์ที่ {self.matches_played} ทำไปได้ {match_kills} Kills!")

    def show_stats(self):
        """แสดงสถิติปัจจุบันของตัวผู้เล่น"""
        status = "บาดเจ็บ" if self.is_injured else "พร้อมแข่ง"
        print(f"\n--- สถิติของ {self.name} ---")
        print(f"ตำแหน่ง: {self.role}")
        print(f"ระดับฝีมือ: {self.skill_level}")
        print(f"พลังงาน: {self.energy}%")
        print(f"สถานะ: {status}")
        print(f"จำนวนนัดที่แข่ง: {self.matches_played}")
        print(f"จำนวน Kills ทั้งหมด: {self.kills}")
        print("-" * 25)


# =====================================================================
# การสร้างออบเจกต์ (Object) จำนวน 5 ออบเจกต์ และเรียกใช้งาน Method ต่างๆ
# =====================================================================

if __name__ == "__main__":
    print("=== ยินดีต้อนรับสู่ระบบจำลองทีมนักกีฬา eSports ===")
    time.sleep(0.5)

    # 1. สร้าง Object ตัวที่ 1: Faker
    player1 = EsportsPlayer(name="Faker", role="Mid Laner", skill_level=95)

    # 2. สร้าง Object ตัวที่ 2: Zeus
    player2 = EsportsPlayer(name="Zeus", role="Top Laner", skill_level=90)

    # 3. สร้าง Object ตัวที่ 3: Oner
    player3 = EsportsPlayer(name="Oner", role="Jungler", skill_level=88)

    # 4. สร้าง Object ตัวที่ 4: Gumayusi
    player4 = EsportsPlayer(name="Gumayusi", role="AD Carry", skill_level=92)

    # 5. สร้าง Object ตัวที่ 5: Keria
    player5 = EsportsPlayer(name="Keria", role="Support", skill_level=91)

    # รวบรวมออบเจกต์ไว้ในลิสต์เพื่อความสะดวกในการวนลูป
    team_members = [player1, player2, player3, player4, player5]

    print(f"\nสร้างตัวละครนักแข่งสำเร็จทั้งหมด {len(team_members)} คน")

    # --- การทดสอบเรียกใช้งาน Method ของ Object ต่างๆ ---

    print("\n--- วันที่ 1: การฝึกซ้อมช่วงเช้า ---")
    player1.train()
    player2.train()
    player3.train()

    print("\n--- วันที่ 2: การแข่งขันแมตช์แรกของฤดูกาล ---")
    for player in team_members:
        player.play_match()

    print("\n--- วันที่ 3: ผู้เล่นบางคนซ้อมเพิ่มและบางคนพักผ่อน ---")
    player4.train()
    player5.train()
    player3.rest()  # Oner พักผ่อนเนื่องจากเหนื่อย

    print("\n--- วันที่ 4: แข่งขันแมตช์ต่อเนื่อง ---")
    player1.play_match()
    player2.play_match()
    player4.play_match()
    player5.play_match()

    print("\n--- วันที่ 5: ตรวจสอบสถานะและซ้อมใหญ่ก่อนนัดชิง ---")
    player1.train()
    player1.train()
    player1.train()  # ลองให้ Faker ซ้อมหนักจนพลังงานเหลือน้อย
    player1.play_match()  # ลองให้แข่งตอนพลังงานน้อยเพื่อดูการทำงานของเงื่อนไข

    print("\n=== สรุปผลงานและสถิติของทีมเมื่อสิ้นสุดสัปดาห์ ===")
    for player in team_members:
        player.show_stats()
        time.sleep(0.3)
