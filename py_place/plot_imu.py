import matplotlib.pyplot as plt

# 1. 读取 CSV 数据
times = []
accel_x = []
accel_y = []

with open("fake_imu.csv", "r") as file:
    # 跳过第一行表头
    next(file) 
    for line in file:
        parts = line.strip().split(",")
        times.append(float(parts[0]))
        accel_x.append(float(parts[1]))
        accel_y.append(float(parts[2]))

# 2. 画图
plt.plot(times, accel_x, label="X轴加速度", color="red", marker="o")
plt.plot(times, accel_y, label="Y轴加速度", color="blue", marker="s")

plt.xlabel("时间 (秒)")
plt.ylabel("加速度 (m/s²)")
plt.title("虚拟 IMU 数据曲线")
plt.legend()
plt.grid(True)

plt.savefig("imu_plot.png")
print("图片已保存为 imu_plot.png")
