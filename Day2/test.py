a=10
b=3
c=2
a+=b  #a=a+b
print(a)
a*=b  #a=a*b
c*=a+2  #c=c*(a+2)
print(a,c)
# 海象运算符
print((e:= 10))  # 10
print(e)         # 10

print(d:= 10)  # 10
print(d+1)       # 10

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False
'''
比较运算符的优先级高于赋值运算符，所以上面的flag0 = 1 == 1先做1 == 1产生布尔值True，再将这个值赋值给变量flag0。print函数可以输出多个值，多个值之间可以用,进行分隔，输出的内容默认以空格分开。
'''