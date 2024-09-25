# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
#
# # 读取 Excel 数据
# df1 = pd.read_excel('巨磁电阻效应.xlsx', '表2')
# print(df1)
# df = df1.iloc[3:,[1,3,5]]
# df.columns = ['B', '减小', '增大']
# print(df)
#
# # 设置字体为微软雅黑
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用于支持中文字体
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# R=2*2/0.710*1000
# print(R)
# r=[]
# for i in range(len(df)):
#    r.append(R)
# # 假设 df 是你的 DataFrame
# x = df.iloc[:, 0]  # 第一列作为横坐标
# y1 = r  # 第二列作为第一条线的纵坐标
# y2 = r  # 第三列作为第二条线的纵坐标
#
# # 创建图像和子图
# fig, ax = plt.subplots(figsize=(10, 6))
#
# # 绘制第二列的折线图，颜色为蓝色
# ax.plot(x, y1, label='增大', color='blue')
# # 在每个数据点上添加小黑圆点
# ax.scatter(x, y1, color='black', s=10)  # s 控制点的大小
#
# # 绘制第三列的折线图，颜色为橙色
# ax.plot(x, y2, label='减小', color='orange')
# # 在每个数据点上添加小黑圆点
# ax.scatter(x, y2, color='black', s=10)  # s 控制点的大小
#
# # 设置网格线更深，颜色和线宽
# ax.grid(True, color='grey', linewidth=1.5)
#
# # 添加标题和坐标轴标签
# ax.set_title('磁阻特性曲线', pad=20)  # pad 控制标题的距离
# ax.set_xlabel('磁感应强度/高斯', labelpad=15)
# ax.set_ylabel('R13和R24的磁阻/Ω', labelpad=15)
#
# # 显示图例
# ax.legend()
#
# # 保存为图片
# plt.savefig('图34.png', dpi=300)
#
# # 显示图像
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
# import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# 设置字体为微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用于支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# Provided data (x: "测量点到中央极大值的距离X（mm）", y: "相对光强")
x = [-2.75, -2.65, -2.55, -2.45, -2.35, -2.25, -2.15, -2.05, -1.95, -1.85,
     -1.75, -1.65, -1.55, -1.45, -1.35, -1.25, -1.15, -1.05, -0.95, -0.85,
     -0.75, -0.65, -0.55, -0.45, -0.35, -0.25, -0.15, -0.05, 0.05, 0.15,
     0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95, 1.05, 1.15, 1.25,
     1.35, 1.45, 1.55, 1.65, 1.75, 1.85, 1.95, 2.05, 2.15, 2.25, 2.35,
     2.45, 2.55, 2.65, 2.75]

y = [0.013, 0.016, 0.023, 0.033, 0.044, 0.057, 0.069, 0.075, 0.075, 0.077,
     0.07, 0.062, 0.048, 0.036, 0.033, 0.044, 0.077, 0.148, 0.25, 0.419,
     0.599, 0.812, 1.037, 1.298, 1.548, 1.759, 1.901, 1.979, 1.983, 1.912,
     1.789, 1.585, 1.336, 1.09, 0.837, 0.596, 0.393, 0.252, 0.147, 0.075,
     0.042, 0.037, 0.047, 0.062, 0.078, 0.089, 0.092, 0.088, 0.076, 0.058,
     0.047, 0.034, 0.022, 0.058, 0.017, 0.013]

# Interpolation function (cubic)
interp_func = interp1d(x, y, kind='cubic')

# Generate finer x values for a smoother curve
x_fine = np.linspace(min(x), max(x), 500)
y_fine = interp_func(x_fine)

# Create plot
plt.figure(figsize=(8, 6))

# Plot interpolated line and original scatter points
plt.plot(x_fine, y_fine, color='black')  # interpolated curve in black
plt.scatter(x, y, color='black')  # original data points in black

# Add labels for axes
plt.title("相对光强分布曲线",fontsize=15)
plt.xlabel("测量点到中央极大值的距离X（mm）", fontsize=12)
plt.ylabel("相对光强", fontsize=12)


# Display the plot

plt.savefig("11111.png", dpi=300)