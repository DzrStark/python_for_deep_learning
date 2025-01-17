# 循环语句

# for循环： for 变量名 in 循环体
# 1-100求和
total = 0
for i in range(1,101):      # range（a,b） 只覆盖了从a到b-1
    total = total+i
print(str(total))

# while循环：while 条件
# 求中位数
num=0
summary=0
user_input=input("输入你想输入的数字，结束请用单个字母q结束")
while user_input != "q" :
    num=num+1
    summary=summary+int(user_input)
    user_input = input("输入你想输入的数字，结束请用单个字母q结束")
medium=summary/num
print("中位数为："+str(medium))