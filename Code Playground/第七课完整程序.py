print("###################")
print("#身体质量指标BMI计算#")
print("###################")
start = input("开始计算y/n?")
while start == 'y':
    h = float(input("请输入您的身高(m)"))
    w = float(input("请输入您的体重(kg)"))
    bmi = round(w/(h*h),2)
    if bmi <= 18.4:
        s = "偏瘦"
    elif 18.5 <= bmi <= 23.9:
        s = "正常"
    elif 24.0 <= bmi <= 27.9:
        s = "过重"
    else:
        s = "肥胖"
    print("身高："+str(h)+"m")
    print("体重："+str(w)+"kg")
    print("BMI："+str(bmi))
    print("您的身体状态是："+s)
    print("###################")
    start = input("开始计算y/n?")
print("#####程序结束#####")

