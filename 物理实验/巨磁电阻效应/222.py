# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# from scipy.interpolate import interp1d
# import matplotlib.font_manager as fm
#
# # 设置字体为微软雅黑
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用于支持中文字体
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# df=pd.read_excel('222.xlsx')
# x1=df['b0h']
# x2=df['b0f']
# y=df['v']
# # 创建图像
# plt.figure(figsize=(10, 6))
# plt.scatter(x1,y,color='black')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.font_manager as fm

# Set font to Microsoft YaHei for Chinese support
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# Load data from Excel
df = pd.read_excel('222.xlsx')
x1 = df['b0h']
x2 = df['b0f']
y = df['v']

# Create figure and subplots
plt.figure(figsize=(12, 10))

# First plot: scatter plot and least squares fitting for x1 vs y

plt.scatter(x1, y, color='black', label='Data (b0h vs v)')
# Least squares polynomial fit (degree 1, linear)
coeffs1 = np.polyfit(x1, y, deg=1)
poly1 = np.poly1d(coeffs1)
y_fit1 = poly1(x1)
plt.plot(x1, y_fit1, color='black')
plt.title(r'$\mathit{^1H}$核的$\nu$与$B_{0}$关系曲线',fontsize=20)
plt.xlabel(r'$B_{0}$(mT)',fontsize=15)
plt.ylabel(r'$\nu$(MHz)',fontsize=15)
plt.savefig('a1.png',dpi=300)
plt.show()

plt.figure(figsize=(12, 10))

plt.scatter(x2, y, color='black', label='Data (b0f vs v)')
# Least squares polynomial fit (degree 1, linear)
coeffs2 = np.polyfit(x2, y, deg=1)
poly2 = np.poly1d(coeffs2)
y_fit2 = poly2(x2)
plt.plot(x2, y_fit2, color='black')
plt.title(r'$\mathit{^{19}F}$核的$\nu$与$B_{0}$关系曲线',fontsize=20)
plt.xlabel(r'$B_{0}$(mT)',fontsize=15)
plt.ylabel(r'$\nu$(MHz)',fontsize=15)
plt.savefig('a2.png',dpi=300)
plt.show()