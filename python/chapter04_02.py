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



# 로또 추첨번호

lotto_number = [11,23,4,5,67]

for num in lotto_number:
    print("lotto_number: ", num)

words = "beautiful"

for word in words:
    print("word: ", word)

# ex4

my_info = {
    "name" : "Lee",
    "Age" : 33,
    "City" : "Seoul"

}


for k in my_info:
    print("key: ", k)
    print("value: ", my_info[k])
    print()
    print("value: ", my_info.get(k))

for v in my_info.values():
    print('value: ', v)

print()

for k in my_info:
    print("key: ", k)


#ex5

name = "Byeon Heung"
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())


# break
number = [23,4,5,6,123,4,34,5,2,3,50]

for n in number:
    print(n)
    if n == 123:
        break

# continue

lt = ["32","34","seop","섭",4.3,complex(4)]

for n in lt:
    if type(n) is bool:
        continue
    print("current type: ", type(n))
    print("multyply by 2", n * 3)


# for - else

number = [13,4,535,3,6,7,10,34,66]

for num in number:
    if num == 10:
        print("Found : 3")
        break
else:
    print("Not Found: 11")


for num in range(2,10):
    for num2 in range(1,10):
        print(num, "*" ,num2, "=", num * num2)
    print()


#변환 예제
name = "Seopman"
list1 = list(name)
print(reversed(list1))
print("Reversed", reversed(name))
print("list", list(reversed(name)))
print("tuple", tuple(reversed(name)))