"""
输入半径计算圆的周长和面积

Version: 1.1
Author: 骆昊
"""
import math

r = float(input('请输入圆的半径: '))
c = 2 * math.pi * r
s = math.pi * r ** 2
print(f'周长: {c:.2f}')
print(f'面积: {s:.2f}')   #字符串前面的f表示这个字符串是需要格式化处理的
print('面积：',s)
print(f'面积：%.2f'%s)
print('面积：%.2f'%s)