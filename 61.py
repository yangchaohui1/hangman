体重 = float(input())
身高 = float(input())
a = 身高/(体重*体重)
bmi = int(a)
if bmi<18.5:
    print('bmi=',bmi,',你的体重过轻')
elif 18.5<=bmi<25:
    print('bmi=',bmi,',你的体重正常')
elif 25<=bmi<28:
    print('bmi=',bmi,',你的体重过重')
elif 28<=bmi<32:
    print('bmi=',bmi,',你的体重属于肥胖')
else:
    print('bmi=',bmi,',你的体重属于严重肥胖')

