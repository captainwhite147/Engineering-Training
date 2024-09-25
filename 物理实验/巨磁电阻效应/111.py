# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# from scipy.interpolate import interp1d
# # import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
#
#
# # 设置字体为微软雅黑
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用于支持中文字体
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# df=pd.read_excel('1111111111.xlsx',sheet_name='Sheet2')
# x=df['t']
# y=df['p']
# z=df['p2']
# # Interpolation function (cubic)
# interp_func = interp1d(x, y, kind='cubic')
#
# # Generate finer x values for a smoother curve
# x_fine = np.linspace(min(x), max(x), 500)
# y_fine = interp_func(x_fine)
#
# # Create plot
# plt.figure(figsize=(8, 6))
#
# # Plot interpolated line and original scatter points
# plt.plot(x_fine, y_fine, color='black')  # interpolated curve in black
# plt.scatter(x, y, color='black')  # original data points in black
#
# interp_func = interp1d(x, z, kind='cubic')
#
# # Generate finer x values for a smoother curve
# x_fine = np.linspace(min(x), max(x), 500)
# z_fine = interp_func(x_fine)
#
#
#
# # Plot interpolated line and original scatter points
# plt.plot(x_fine, z_fine,linestyle='-' ,color='black')  # interpolated curve in black
# plt.scatter(x, z, color='black')  # original data points in black
# # Add labels for axes
# plt.title("两种充电情况下超级电容的充电特性",fontsize=15)
# plt.xlabel("时间/min", fontsize=12)
# plt.ylabel("功率/mW", fontsize=12)
# # plt.savefig('p2.png',dpi=300)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.font_manager as fm

# 设置字体为微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用于支持中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

df = pd.read_excel('1111111111.xlsx', sheet_name='Sheet2')
x = df['t']
y = df['p']
z = df['p2']

# 创建图像
plt.figure(figsize=(10, 6))

# 第一条曲线 y 的插值并绘制 (实线)
interp_func_y = interp1d(x, y, kind='cubic')
x_fine = np.linspace(min(x), max(x), 500)
y_fine = interp_func_y(x_fine)
plt.plot(x_fine, y_fine, color='black', linestyle='-', label='直接对超级电容充电')  # 实线
plt.scatter(x, y, color='black')  # 原始数据点

# 第二条曲线 z 的插值并绘制 (虚线)
interp_func_z = interp1d(x, z, kind='cubic')
z_fine = interp_func_z(x_fine)
plt.plot(x_fine, z_fine, color='black', linestyle='--', label='加DC-DC后对超级电容充电')  # 虚线
plt.scatter(x, z, color='black')  # 原始数据点

# 设置图例，放在右上角
# 设置图例，放在图的外面
plt.legend(loc='lower right',framealpha=0.5)
# 添加标题和坐标轴标签
plt.title("两种充电情况下超级电容的充电特性", fontsize=15)
plt.xlabel("时间/min", fontsize=12)
plt.ylabel("功率/mW", fontsize=12)

# 显示图像
plt.savefig('p3.png',dpi=300)