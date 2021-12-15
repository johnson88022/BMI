high = float(input("輸入你的身高(cm)"))
weight = float(input("輸入你的體重(kg)"))
high = high/100
bmi = weight/ (high**2)
print("你的BMI值為: ",bmi )
if bmi < 18.5 and bmi >0 : 
	print("太輕了啦!")
elif bmi >= 18.5 and bmi < 27 :
	print("體重正常!")
elif bmi >= 27 and bmi < 30 :
	print("注意飲食!")
elif bmi >= 30 and bmi < 35 :
	print("努力運動!")
else:
	print("太重了啦!")