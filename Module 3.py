# print(3**5)
# print(-8/-4)
# print(10/2+6)

# a,b,c=5,4,2
# print('Сложение: ',a+b+c)
# print('Вычитание: ',a-b-c)
# print('Умножение: ',a*b*c)
# print('Деление: ',a/b/c)
# print('Возведение в степень: ',a**b**c)


# print(65/0)
# Домашняя работа 3,3

# a,b,c=8,5,3
# print((a/(b+c)-a)/c)


# bus = 5
# metro = 3
# result = (6+((10-bus)**2))/(metro+1)+(132/(2+bus))
# print(result)

# a,b,c=8,2,4
#
# result=(-3+(a**2-12)*c**3**2)/(b*18)
# print(result)



# first_number=int(input('Введите первое число: '))
# second_number=int(input('Введите второе число:'))
# print('Сумма: ', first_number+second_number)


# Домашняя работа 3,4++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a=int(input("Введите первое число :"))
# b=int(input("Введите второе число :"))
# c=int(input("Введите третье число :"))
# d=int(input("Введите четвертое число :"))
# answer=2*(c+5+(a*b)/(4*b))*(d-2*a**3/30)-10
# print(answer)

# a='12'
# b='34'
# c=a+b
# d=int(c)*2
# print(d)
# # or or or or or or or or or
# a='12'
# b='34'
# print(int(a+b)*2)


# a=int('2')
# b=int('5')
# c=int('3')
# num=(6**a+(7-b)*c)
# print(num)


# Домашняя работа 3,5+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# apples=41
# boxes=3
# full_boxes=apples//boxes
# print(full_boxes)
# print(apples%boxes)

# number=int(input('Введите число: '))
# number_house = number%10
# apartment_number=number//10
# print('номер дома: ',number_house)
# print('номер квартиры: ',apartment_number)



# print('В нашем соревновании учавствуют три спортсмена.Каждый круг — 100 метров.')
# athlete1='1 '
# athlete1_ran=204
# print('Первый спортсмен пробежал: ',athlete1_ran,'M')
# whole_circle=athlete1_ran//100
# incomplete_circle_to=athlete1_ran%100
# print('Из них ',whole_circle,'полных круга ','и',incomplete_circle_to,'M',' не полных круга')
#
# athlete2='2 '
# athlete2_ran=186
# print('Второй спортсмен пробежал: ',athlete2_ran,'M')
# whole_circle=athlete2_ran//100
# incomplete_circle_to=athlete2_ran%100
# print('Из них ',whole_circle,'полных круга ','и',incomplete_circle_to,'M',' не полных круга')

# athlete3="3 "
# athlete3_ran=234
# print('Третий спортсмен пробежал: ',athlete3_ran,'M')
# whole_circle=athlete3_ran//100
# incomplete_circle_to=athlete3_ran%100
# print('Из них ',whole_circle,'полных круга ','и',incomplete_circle_to,'M',' не полных круга')
#
# print('Впереди спорстмен под номером ',athlete3)
# print('Он опережает 1 го смортсмена на ',athlete3_ran-athlete1_ran,
# 'М и второго спортсмена на ',athlete3_ran-athlete2_ran,'M')
# Домашняя работа 3,7

print('Задача 1. Язык математики')
a = 8
b = 10
c = 12
d = 18
result= ((-3 + a**2) * b - 2**3)/(c- 2 * d)
print(result)

print('==========================================================')

print('Задача 2. Финансовый отчёт')

# print('1 год:')
# year1_quarter1=int(input('Введите сумму 1 квартала: '))
# year1_quarter2=int(input('Введите сумму 2 квартала: '))
# year1_quarter3=int(input('Введите сумму 3 квартала: '))
# year1_quarter4=int(input('Введите сумму 4 квартала: '))
# qu1_1=year1_quarter1
# qu2_1=year1_quarter2
# qu3_1=year1_quarter3
# qu4_1=year1_quarter4
# half_a_year1=qu1_1 + qu2_1
# half_a_year2=qu3_1 + qu4_1
# print('Сумма 1 полугодия: ',half_a_year1)
# print('Сумма 2 полугодия: ',half_a_year2)
# print('Динамический рост составляет: ', (half_a_year2 -half_a_year1) / half_a_year1 * 100)

print('1 год:')
year1_quarter1=int(input('Введите сумму 1 квартала: '))
year1_quarter2=int(input('Введите сумму 2 квартала: '))
year1_quarter3=int(input('Введите сумму 3 квартала: '))
year1_quarter4=int(input('Введите сумму 4 квартала: '))
half_a_year1= year1_quarter1 + year1_quarter2
half_a_year2= year1_quarter3 + year1_quarter4
print('Сумма 1 полугодия: ',half_a_year1)
print('Сумма 2 полугодия: ',half_a_year2)
print("Итог: ", half_a_year2 / half_a_year1)

print('==========================================================')
print('Задача 3. Следующее и предыдущее')

a=int(input('Введите число:'))
before=(a+1)
print('После числа ', a,'идёт число ', before)
after=(a-1)
print('До числа ', a,'идёт число ',after)

print('==========================================================')
print('Задача 4. Площадь треугольника')

leg1=int(input('Введите длину первого катета: '))
leg2=int(input('Введите длину второго катета: '))
print('Общая площать прямого треугольника составляет: ', leg1 * leg2 / 2, ' см')
print('==========================================================')
print('Задача 5. Часы')

print('Калькулятор минут')
minute=int(input('Введите число: '))
print(minute // 60, 'часов и ', minute % 60, 'минут' )
print('==========================================================')
print('Задача 6')

first_number=int(input('Введите первое трезначное число: '))
second_number=int(input("Введите второе трезначное число: "))
number1= first_number % 100
number2=second_number % 100
print(number1 + number2)

print(' ============================================================')
print('Задача 7. Поездка по кругу')

speed=int(input('Сколько км в час движется Вася: '))
time=int(input('Сколько часов Вася проехал: '))
circle=time * speed // 115
meters=time * speed % 115
print('Вася остановился на ', circle, 'круге и на', meters, 'метре')
print('==========================================================')
print('Задача 8. Режем число на части')

number=int(input('Введите четырёхзначное число: '))
a=number // 1000
c=number // 100
q=c % 10
d=number // 10
w=d % 100
r=w % 10
f=number % 10
print(a, q, r, f)
print('==========================================================')
print('Задача 9. В обратном порядке')

number=int(input('Введите четырёхзначное число: '))
a=number // 1000
c=number // 100
q=c % 10
d=number // 10
w=d % 100
r=w % 10
f=number % 10
print(f, r, q, a, sep='')

print(' ==================================================')
print('Задача 10. Поменять местами: не всё так просто! (необязательная, повышенной сложности)')


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a,b=(a+b-a),(b+a-b)
print(a, b)

