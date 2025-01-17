# 函数的定义
# 求矩形面积
def area(high, weight):
    s=high*weight
    return s

a=input("输入矩形的长：")
b=input("输入矩形的宽：")
temp=area(int(a),int(b))
print(f"这个矩形的面积为：{temp}")