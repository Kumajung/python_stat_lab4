""" Hypothesis Testing หน้า 54-57
นักวิจัยรายงานว่าเงินเดือนเฉลี่ยของผู้ช่วยศาสตราจารย์ 
มากกว่า 42,000 ดอลลาร์ ตัวอย่างผู้ช่วยศาสตราจารย์ 30 คนมี 
เงินเดือนเฉลี่ย 43,260 ดอลลาร์ ที่ α = 0.05 ให้ทดสอบการอ้างสิทธิ์ว่าผู้ช่วย 
อาจารย์มีรายได้มากกว่า 42,000 ดอลลาร์ต่อปี ค่าเบี่ยงเบนมาตรฐาน
ของประชากรคือ 5230 ดอลลาร์
ขั้นตอนที่ 1: ระบุสมมติฐานและระบุการอ้างสิทธิ์
ขั้นตอนที่ 2: ค้นหาค่าวิกฤต เนื่องจาก α = 0.05 และการทดสอบเป็นการทดสอบหางขวา ค่าวิกฤตคือ z =
ขั้นตอนที่ 3: คํานวณค่าทดสอบ z = 
ขั้นตอนที่ 4: ตัดสินใจ
ขั้นตอนที่ 5: สรุปผลลัพธ์
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# ข้อมูลเริ่มต้น
sample_size = 30
sample_mean = 43260
population_mean = 42000
population_std_dev = 5230
alpha = 0.05

# Step 2: คำนวณค่า z-critical
z_critical = norm.ppf(1 - alpha)  # ค่า critical value ของ z สำหรับ one-tailed test

# Step 3: คำนวณค่า z-test
z_test = (sample_mean - population_mean) / (population_std_dev / np.sqrt(sample_size))

# Step 4: เตรียมกราฟสำหรับแสดงผล
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

# Plot กราฟ
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Standard Normal Distribution', color='blue')
plt.axvline(z_critical, color='red', linestyle='--', label=f'Critical Value (z = {round(z_critical,2)})')
plt.axvline(z_test, color='green', linestyle='--', label=f'Test Value (z = {round(z_test,2)})')
plt.fill_between(x, y, 0, where=(x > z_critical), color='red', alpha=0.3, label='Rejection Region')
plt.title('Right-Tailed Z-Test')
plt.xlabel('Z-Score')
plt.ylabel('Probability Density')
plt.legend()
plt.grid()
plt.show()

print("ค่าวิกฤต: ",round(z_critical,3))
print("ค่าทดสอบ: ",round(z_test,3))