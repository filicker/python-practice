print(0b100)
print(0o100)
print(0x100)
a=100
b=12.94
c='123'
print(a)
print(b)
print(c)
print(int(b))
print(type(a))  #a是int类型100
print(type(b))  #b是float类型12.94
print(type(c))  #c是str字符串类型123
print(int(c))   #str类型的'123'转成int，输出123
d='hello world'
e=True
print(type(d))
print(type(e))  #bool是布尔类型，值只有True或者false
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
h='101'
print(int(h, base=2))   # str类型的'101'按二进制转成int，输出
"""
chr()：将整数（字符编码）转换成对应的（一个字符的）字符串。
ord()：将（一个字符的）字符串转换成对应的整数（字符编码）。
"""
