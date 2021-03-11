#daydayup.py
#q1 每天进步1‰与每天退步11‰
#dayup =pow (1.001,365)
#daydown =pow (0.999,365)
#print ("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))

#q2 一年365天，每天进步5‰或1%，累计进步多少呢？/一年365天，每天退步5‰或1%，累计进步多少呢？
#dayup5 =pow(1.005,365)
#dayup1 =pow(1.01,365)
#daydown5 =pow(0.995,365)
#daydown1 =pow(0.99,365)
#print("向上5‰:{:2f},向上1%:{:.2f}".format(dayup5,dayup1))
#print("向下5‰:{:.2f},向下1%:{:.2f}".format(daydown5,daydown1))

#dayfactor =0.005
#dayup =pow(1+dayfactor,365)
#daydown =pow (1-dayfactor,365)
#print("向上:{:.2f},向下:.{:2f}".format(dayup,daydown))             # 变量的使用
#dayfactor =0.01
#dayup =pow(1+dayfactor,365)
#daydown =pow (1-dayfactor,365)
#print("向上:{:.2f},向下:.{:2f}".format(dayup,daydown))             # 变量的使用！ 不使用另一个变量，而是对这个变量重新赋值

#q3  一年365天，一周5个工作日，每天进步1%- 一年365天，一周2个休息日，每天退步1%
dayup =1.0
dayfactor =0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup =dayup* (1-dayfactor)
    else:
        dayup =dayup* (1+dayfactor)
print("工作日的力量:{:.2f}".format(dayup))
     
 



