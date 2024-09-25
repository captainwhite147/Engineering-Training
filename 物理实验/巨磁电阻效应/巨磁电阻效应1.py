import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 读取 Excel 数据
df1 = pd.read_excel('巨磁电阻效应.xlsx', '表1')
print(df1)
df = df1.iloc[2:, 1:]
df.columns = ['B', '增大', '减小']
print(df)

# 设置字体为微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用于支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 假设 df 是你的 DataFrame
x = df.iloc[:, 0]  # 第一列作为横坐标
y1 = df.iloc[:, 1]  # 第二列作为第一条线的纵坐标
y2 = df.iloc[:, 2]  # 第三列作为第二条线的纵坐标

# 创建图像和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制第二列的折线图，颜色为蓝色
ax.plot(x, y1, label='增大', color='blue')
# 在每个数据点上添加小黑圆点
ax.scatter(x, y1, color='black', s=10)  # s 控制点的大小

# 绘制第三列的折线图，颜色为橙色
ax.plot(x, y2, label='减小', color='orange')
# 在每个数据点上添加小黑圆点
ax.scatter(x, y2, color='black', s=10)  # s 控制点的大小

# 设置网格线更深，颜色和线宽
ax.grid(True, color='grey', linewidth=1.5)

# 添加标题和坐标轴标签
ax.set_title('磁电转换特性曲线', pad=20)  # pad 控制标题的距离
ax.set_xlabel('磁感应强度/高斯', labelpad=15)
ax.set_ylabel('电压表读数/mV', labelpad=15)

# 显示图例
ax.legend()

# 保存为图片
plt.savefig('图11.png', dpi=300)

# 显示图像
plt.show()