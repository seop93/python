# Chapter04-2
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#   <Loop body>

for v1 in range(10):
    print('v1 is: ', v1)

print()

for v2 in range(1, 11):
    print('v2 is: ', v2)

print()

for v3 in range(0, 11, 2):
    print('v3 is :', v3)

# 1 ~ 1000합

sum1 = 0

for v in range(1,1001):
    sum1 += v

print('1 ~ 1000 Sum: ', sum1)

print('1 ~ 1000 Sum: ', sum(range(1, 1001))) # sum은 리스트를 받는다
print('4 ~ 1000 4의 배수의 합: ', sum(range(4, 1001, 4)))

# Iterables 반복할 수 있는 객체 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

# ex1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('first name:' + name)