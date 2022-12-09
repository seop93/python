# Chapter06-2
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y


print('-' * 10)
print('called! inner!')
print(add(5, 5))
print(subtract(10, 3))
print(multiply(2, 3))
print(divide(10, 2))
print(power(2, 4))

# __name__ 사용 # -> 테스트 해볼 때
if __name__ == "__main__":
    print('-' * 10)
    print('called! inner!')
    print(add(5, 5))
    print(subtract(10, 3))
    print(multiply(2, 3))
    print(divide(10, 2))
    print(power(2, 4))
