# BMI = 体重 / （身高^2）
height = input("输入你的身高（m）：") # input得到的值默认为字符类型
weight = input("输入你的体重（kg）：")
BMI = int(weight) / (float(height)**2)
print("您的BMI是"+str(BMI))