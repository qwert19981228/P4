```python
1.A0-A6的值是什么?
    A0=dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
    A1=range(10)
    A2=sorted([i for i in A l if i in A0])
    A3=sorted([A0[s] for s in A0 ])
    A4=[i for i in A l if i in A3]
    A5={i:i*i for i in A1}
    A6=[[i,i*i] for i in A1]

    A0:{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    A1:range(0,10)
    A2:[]
    A3:[1,2,3,4,5]
    A4:[1,2,3,4,5]
    A5:{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    A6:[[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
```

```python
2.给定一个 int list a，满足 a[i+1] >=a[i],给定int key，找出list a中第一个大于等于key的元素的index，无满足要求的元素则返回-1。
函数定义：
    def findindex(int_list,int_key)

答案示例：
    #定义函数
    def findIndex(int_list, int_key):
        '''
        给定一个int list a，满足a[i+1]>=a[i]，给定int key,找出list a中第一个大于等于key的元素的index，无满足要求的元素则返回-1.
        :param int_list:
        :param int_key:
        :return:
        '''
        for i in int_list:
            if i >= int_key:
                return int_list.index(i)
                break
        if int_key not in int_list:
            return -1

    if __name__ == "__main__":
        #定义一个 int list,并初始化
        list1 = [1,1,2,2,3,3,4,4,5,5,6,6]
        #调用函数，并传入参数，注：传入的int_key值是一个不存在int_list的值．返回－１；
        index1 = findIndex(list1, 8)
        print (index1)

        # 调用函数，并传入参数，注：传入的int_key的值在int_list的值．返回其首次出现时对应的下标；
        index2 = findIndex(list1, 3)
        print(index2)
```

```python
3.常用的版本控制工具及其常用命令

答案:
	git: 
		git add .
		git status 
		git commit 提交至本地仓库
		git origin
		git push
```

```python
4.D = [x * x for x in range(1,10)],请写出D的输出结果
  #生成数  x = 1,2,3,4,5,6,7,8,9
  # 所以结果是如下：
  [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```python
5.表达式[1]*2的值为（C）
	A：[2]	B:[1]	C:[1,1]	D:[1,2]
```

