# if_elif_else结构
score = int(input("你的成绩为："))
if score==100:
    print("满分！")
elif score>=80:
    print("优秀")
else:
    print("普通")

# 逻辑运算(and/or/not)
if (score >= 90 and score ==100):
    print("A")
if( score >= 90 or score >= 60):
    print("B")