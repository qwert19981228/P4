# 
# 3. 赋值运算符
# 	1. =
# 	2. +=
# 	3. -=
# 	4. *=
# 	5. /=
# 	6. %=
# 	7. **=
# 	8. //=

# 1. 赋值
# 1.1 单一赋值
a = 10 				# 先算=右边的, 再算=左边的

# 1.2 连续赋值
a = b = c = 20		# 连等, a,b,c 都引用了对象20
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 1.3 多段赋值, 
# 	看上去从前向后, 依次赋值, 各自独占一个内存
a,b,c = 1,2,3
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))
# 
# 底层:
# 	a,b,c = 1,2,3
# 	先是 x=1  y=2  z=3 		这里的xyz都是临时变量
# 	最终 a=x  b=y  c=z 		


# 例题:
a,b = 0,1
a,b = b, a+b
print(a,b)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


# 2. +=
# 	a += b   ====>  a = a+b
a = 10
b = 5
a += b
print(a, b)


a = 10
b = 3
a -= b
print(a, b)


a = 10
b = 3
a **= b 	# a = a ** b
print(a,b)







