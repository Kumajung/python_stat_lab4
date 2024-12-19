""" Example
นักวิจัยรายงานว่า GPA เฉลี่ยของนักเรียนในโรงเรียนแห่งหนึ่งเกินกว่า 3.0
จากการสุ่มตัวอย่างข้อมูล GPA ของนักเรียนจำนวน 1,000 คน
โดยนำเข้าจากภายนอกไฟล์ gpa_data.csv
ที่ระดับนัยสำคัญ 𝛼 = 0.05 ให้ทดสอบสมมติฐานว่า GPA เฉลี่ยของนักเรียนในโรงเรียนแห่งนี้เกินกว่า 3.0
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Step 1: โหลดข้อมูลจากไฟล์ CSV
file_path = "/kaggle/input/gpa-data/gpa_data.csv"  # ระบุเส้นทางไฟล์ CSV
data = pd.read_csv(file_path)
gpa_data = data['GPA'].values  # สมมติว่าคอลัมน์ GPA มีชื่อว่า 'GPA'

# ค่าอ้างอิงประชากรและระดับนัยสำคัญ
population_mean = 3.0  # ค่า GPA ที่อ้างอิงจากประชากร
alpha = 0.05  # ระดับนัยสำคัญ

# Step 2: คำนวณค่าเฉลี่ยตัวอย่างและขนาดตัวอย่าง
sample_mean = np.mean(gpa_data)  # ค่าเฉลี่ยตัวอย่าง
sample_size = len(gpa_data)  # ขนาดตัวอย่าง

# คำนวณค่าเบี่ยงเบนมาตรฐานของประชากร (Population Standard Deviation)
population_std_dev = np.sqrt(np.sum((gpa_data - sample_mean) ** 2) / len(gpa_data))

# Step 3: คำนวณค่า z-critical
z_critical = norm.ppf(1 - alpha)  # ค่า critical value ของ z สำหรับ one-tailed test

# Step 4: คำนวณค่า z-test
z_test = (sample_mean - population_mean) / (population_std_dev / np.sqrt(sample_size))

# Step 5: เตรียมกราฟแสดงผล
x = np.linspace(-4, 4, 1000)  # สร้างช่วงค่า z-score
y = norm.pdf(x, 0, 1)  # คำนวณค่า density ของการแจกแจงปกติมาตรฐาน

# Plot กราฟ
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Standard Normal Distribution', color='blue')  # เส้นกราฟการแจกแจงปกติ
plt.axvline(z_critical, color='red', linestyle='--', label=f'Critical Value (z = {round(z_critical, 2)})')  # เส้นค่าวิกฤต
plt.axvline(z_test, color='green', linestyle='--', label=f'Test Value (z = {round(z_test, 2)})')  # เส้นค่าทดสอบ
plt.fill_between(x, y, 0, where=(x > z_critical), color='red', alpha=0.3, label='Rejection Region')  # พื้นที่ปฏิเสธ H0
plt.title('Right-Tailed Z-Test')
plt.xlabel('Z-Score')
plt.ylabel('Probability Density')
plt.legend()
plt.grid()
plt.show()

# Step 6: สรุปผลลัพธ์
print("ค่าเฉลี่ยของตัวอย่าง (sample mean):", round(sample_mean, 3))
print("ค่าวิกฤต (critical value):", round(z_critical, 3))
print("ค่าทดสอบ (test value):", round(z_test, 3))

# ตรวจสอบว่าค่าทดสอบอยู่ในพื้นที่ปฏิเสธสมมติฐานว่างหรือไม่
if z_test > z_critical:
    print("สรุป: ปฏิเสธสมมติฐานว่าง (Reject H0) และยอมรับว่า GPA เฉลี่ยของนักเรียนเกินกว่า 3.0")
else:
    print("สรุป: ไม่สามารถปฏิเสธสมมติฐานว่าง (Fail to Reject H0)")
