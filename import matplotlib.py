import matplotlib.pyplot as plt
import numpy as np

# 1. สร้างหน้าต่างกราฟ 3x3 แถว/คอลัมน์
fig, axes = plt.subplots(3, 3, figsize=(15, 12))

# กำหนดหัวข้อใหญ่สุดหลักของหน้าต่าง
fig.suptitle("My First Chart", fontsize=18, fontweight='bold')

# สุ่มข้อมูลจำลองสำหรับการพล็อตกราฟแต่ละแบบ
np.random.seed(42)
x_data = np.linspace(0, 10, 50)

# =========================================================================
# แถวที่ 1
# =========================================================================

# 1. แผนภูมิจุดกระจายแบบสีเดียว (Scatter Plot)
axes[0, 0].scatter(np.random.rand(50), np.random.rand(50), color='purple', alpha=0.7)
axes[0, 0].set_title("Scatter Plot")
axes[0, 0].set_xlabel("X Axis")
axes[0, 0].set_ylabel("Y Axis")

# 2. แผนภูมิจุดกระจายหลากสีแบบไล่ระดับความหนาแน่น (Color Scatter)
sc = axes[0, 1].scatter(np.random.rand(100), np.random.rand(100), c=np.random.rand(100), cmap='viridis', alpha=0.8)
axes[0, 1].set_title("Color Scatter Plot")
axes[0, 1].set_xlabel("Density X")
axes[0, 1].set_ylabel("Density Y")

# 3. แผนภูมิแท่งแนวนอน (Horizontal Bar Chart)
y_pos = np.arange(4)
performance = [10, 8, 12, 14]
axes[0, 2].barh(y_pos, performance, align='center', color='steelblue')
axes[0, 2].set_yticks(y_pos)
axes[0, 2].set_yticklabels(['A', 'B', 'C', 'D'])
axes[0, 2].invert_yaxis()  # ให้เรียงจากบนลงล่าง
axes[0, 2].set_title("Horizontal Bar Chart")
axes[0, 2].set_xlabel("Values")
axes[0, 2].set_ylabel("Categories")

# =========================================================================
# แถวที่ 2
# =========================================================================

# 4. แผนภูมิพื้นที่ (Filled Area Chart)
axes[1, 0].plot(x_data, x_data**1.5, color='navy')
axes[1, 0].fill_between(x_data, x_data**1.5, color='lightblue', alpha=0.5)
axes[1, 0].set_title("Filled Area Chart")
axes[1, 0].set_xlabel("Timeline")
axes[1, 0].set_ylabel("Growth Metric")

# 5. แผนภูมิเส้นหลายเส้น/แผนภูมิเรดาร์จำลอง (Line Comparison)
axes[1, 1].plot(x_data, x_data, label='Trend A', color='blue')
axes[1, 1].plot(x_data, 10 - x_data, label='Trend B', color='orange')
axes[1, 1].plot(x_data, np.sin(x_data)*5 + 5, label='Trend C', color='green')
axes[1, 1].set_title("Multi-Line Chart")
axes[1, 1].set_xlabel("Time Step")
axes[1, 1].set_ylabel("Index Value")

# 6. แผนภูมิเส้นแบบจุดเชื่อมโยง (Point & Line Chart)
x_line = [1, 2, 3, 4, 5]
y_line = [3, 7, 5, 2, 8]
axes[1, 2].plot(x_line, y_line, marker='o', color='brown', markerfacecolor='red', markersize=8)
axes[1, 2].set_title("Connected Points")
axes[1, 2].set_xlabel("Step Count")
axes[1, 2].set_ylabel("Score")

# =========================================================================
# แถวที่ 3
# =========================================================================

# 7. แผนภูมิฮิสโตแกรมแจกแจงความถี่ (Histogram)
data_hist = np.random.normal(0, 1, 1000)
axes[2, 0].hist(data_hist, bins=15, color='royalblue', edgecolor='black', alpha=0.8)
axes[2, 0].set_title("Histogram Distribution")
axes[2, 0].set_xlabel("Range Interval")
axes[2, 0].set_ylabel("Frequency")

# 8. แผนภูมิวงกลมแบบแยกชิ้น (Exploded Pie Chart)
labels_pie1 = ['Part A', 'Part B', 'Part C']
sizes_pie1 = [45, 30, 25]
explode = (0.1, 0, 0)  # แยกชิ้นแรกออกมาเล็กน้อย
axes[2, 1].pie(sizes_pie1, explode=explode, labels=labels_pie1, autopct='%1.1f%%', shadow=True, startangle=140)
axes[2, 1].set_title("Exploded Pie Chart")
axes[2, 1].set_xlabel("Ratio Summary")
axes[2, 1].set_ylabel("Distribution")

# 9. แผนภูมิวงกลมมาตรฐานแบบมีคำอธิบาย (Standard Pie Chart)
labels_pie2 = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
sizes_pie2 = [40, 20, 25, 15]
axes[2, 2].pie(sizes_pie2, labels=labels_pie2, autopct='%1.1f%%', startangle=90)
axes[2, 2].legend(loc="upper right", bbox_to_anchor=(1.3, 1))
axes[2, 2].set_title("Standard Pie Chart")
axes[2, 2].set_xlabel("Categories Summary")
axes[2, 2].set_ylabel("Segmentation")

# จัดระยะห่างระหว่างกราฟย่อยแต่ละตัวให้เหมาะสมสวยงาม ไม่ซ้อนทับกัน
plt.tight_layout()

# 2. แสดงผลกราฟ
plt.show()
