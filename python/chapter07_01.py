# Chapter07-1
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError....
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외를 무시

# SyntaxError

# print('SyntaxError)
# print(3 + 5))
# if True
#   pass

# NameError
a = 5
b = 10
# print(c)

# ZeroDivisionError
# print(100 / 0)

# IndexError
x = [10, 20, 30]
# print(x[4])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# KeyError

dic = {
    "name": "seop",
    "age": 30.,
    "city": "busan"
}

# print(dic["hobby"])
print(dic.get("hpbby"))

# 에외가 없다고 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외처리 권장


# AttributeError: 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time

print(time.time())
# print(time.tim2())

# ValueError
x = [10, 20, 30]
x.remove(10)
print(x)
# x.remove(300)
print()

# FileNotFoundError
# f = open('test.txt')


# TypeError: 자료형에 맞지않는 연산을 수행할 경우
x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)

print(x + list(y))
print(x + list(z))

# 예외 처리
# try: 예외가 발생할 가능성이 있는 코드 실행
# except 예외명: 예외 처리하겠다.
# except 예외명:
# else: try 블록의 코드가 에러가 없을 시 실행
# finally: 항상 실행 됌

name = ['byoen', 'seop', 'lee']

# ex1
try:
    z = 'seop'
    x = name.index(z)
    print('{} Found It! {} in name'.format(z, x + 1))
except ValueError:
    print('Not Found it! ValueError')
else:
    print('Ok')

print()

# ex2
try:
    z = 'ep'
    x = name.index(z)
    print('{} Found It! {} in name'.format(z, x + 1))
except:
    print('Not Found it! Exception')
else:
    print('Ok')

print()

# ex3
try:
    z = 'ep'
    x = name.index(z)
    print('{} Found It! {} in name'.format(z, x + 1))
except Exception as e:
    print(e)
    print('Not Found it! Exception')
else:
    print('Ok')
finally:
    print('finished')

print()

# ex4
# 예외 발생: raise
# raise 직접 예외 발생

try:
    a = 'seop'
    if a == 'byeon':
        print('okay')

    else:
        raise ValueError

except ValueError:
    print('Occurred ValueError')

else:
    print('okay')
