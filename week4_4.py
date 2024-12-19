""" Example
นักวิจัยรายงานว่าอัตราดอกเบี้ยเฉลี่ยของเงินฝากประจำ 1 ปีในธนาคารระดับประเทศ มากกว่า 3.5% ต่อปี 
ตัวอย่างธนาคาร 25 แห่งที่เลือกมามีอัตราดอกเบี้ยเฉลี่ย 3.8% ต่อปี ที่ระดับนัยสำคัญ 
𝛼 = 0.05
ให้ทดสอบสมมติฐานว่าค่าเฉลี่ยอัตราดอกเบี้ยในธนาคารมากกว่า 3.5% ต่อปี
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# ข้อมูลเริ่มต้น
sample_data = [3.2, 3.5, 3.8, 3.7, 3.6, 
               3.9, 4.0, 3.7, 3.4, 3.6, 
               3.8, 3.5, 3.9, 3.6, 3.8, 
               3.4, 3.6, 3.7, 4.1, 3.9]  # ข้อมูลอัตราดอกเบี้ยจากธนาคาร 20 แห่ง
population_mean = 3.5  # ค่าเฉลี่ยที่อ้างอิงจากประชากร


alpha = 0.05  # ระดับนัยสำคัญ

# Step 1: คำนวณค่าเฉลี่ยของตัวอย่าง (sample mean) และขนาดตัวอย่าง (sample size)
sample_mean = np.mean(sample_data)
sample_size = len(sample_data)

# คำนวณค่าเบี่ยงเบนมาตรฐานของประชากร (Population Standard Deviation)
population_std_dev = np.sqrt(np.sum((np.array(sample_data) - sample_mean) ** 2) / len(sample_data))

# Step 2: คำนวณค่า z-critical
z_critical = norm.ppf(1 - alpha)  # ค่า critical value ของ z สำหรับ one-tailed test

# Step 3: คำนวณค่า z-test
z_test = (sample_mean - population_mean) / (population_std_dev / np.sqrt(sample_size))

# Step 4: เตรียมกราฟสำหรับแสดงผล
x = np.linspace(-4, 4, 1000)  # สร้างช่วงค่า z-score
y = norm.pdf(x, 0, 1)  # คำนวณค่า density ของการแจกแจงปกติมาตรฐาน

# Plot กราฟ
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Standard Normal Distribution', color='blue')  # เส้นกราฟการแจกแจงปกติ
plt.axvline(z_critical, color='red', linestyle='--', label=f'Critical Value (z = {round(z_critical,2)})')  # เส้นค่าวิกฤต
plt.axvline(z_test, color='green', linestyle='--', label=f'Test Value (z = {round(z_test,2)})')  # เส้นค่าทดสอบ
plt.fill_between(x, y, 0, where=(x > z_critical), color='red', alpha=0.3, label='Rejection Region')  # พื้นที่ปฏิเสธ H0
plt.title('Right-Tailed Z-Test')
plt.xlabel('Z-Score')
plt.ylabel('Probability Density')
plt.legend()
plt.grid()
plt.show()

# Step 5: สรุปผลลัพธ์
print("ค่าเฉลี่ยของตัวอย่าง (sample mean):", round(sample_mean, 3))
print("ค่าวิกฤต (critical value):", round(z_critical, 3))
print("ค่าทดสอบ (test value):", round(z_test, 3))

if z_test > z_critical:
    print("สรุป: ปฏิเสธสมมติฐานว่าง (Reject H0) และยอมรับว่าค่าเฉลี่ยอัตราดอกเบี้ยมากกว่า 3.5%")
else:
    print("สรุป: ไม่สามารถปฏิเสธสมมติฐานว่าง (Fail to Reject H0)")
