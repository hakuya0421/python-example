height = input('키를 입력하세요 (cm) : ')
weight = input('몸무게를 입력하세요(kg) : ')
height = int(height)
weight = float(weight)
BMI = weight / height ** 2 * 10000
print('당신의 BMI 지수는 : {:.2f} '.format(BMI))