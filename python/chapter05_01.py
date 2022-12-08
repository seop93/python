# Chapter05-1
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lmabda)

# 함수 정의 방법
# def function_name(parameter):
# code

# ex1
def first_func(w):
    print("Hello", w)


word = "Goodboy"

first_func(word)


# ex2

def return_func(w):
    return "Hello, " + str(w)


# ex3(다중반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]


a = func_mul(10)
print(a)
print(a[2])
print(type(a), a, tuple(a))


def func_dic(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {"v1": y1, "v2": y2, "v3": y3}


d = func_dic(10)

print(type(d), d, d.items(), d.keys(), d.values())

# 중요
# *args, **rwargs

# *args(언팩킹)
print("언팩킹")

def args_func(*args):  # 매개변수 명 자유
    for i,v in enumerate(args):
        print("Result: {}".format(i),v)
    print("------")


args_func("Lee", "park")
args_func("l", "2", "3")
args_func(1, 2, 3, 4)


# **rwargs(언팩킹)
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print("----")


kwargs_func(name1="lee", name2='park')
kwargs_func(name1="lee", name2="les", name3="23")


# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)


example(10, 20, "lee", "kim", 'park', age1=10, args2=20, args3=30)


# 중첩함수

def nested_func(num):
    def func_in_func(num):
        print(num)

    print("In Fact")
    func_in_func(num + 100)


nested_func(100)


# 실행불가
# func_in_func(1000)

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가도성 오히려 감소

# def mul_func(x, y):
#     return x * y
#
#
# a = lambda x, y: x * y

def mul_func(x, y):
    return x * y


print(mul_func(10, 20))

mul_func_var = mul_func
print(mul_func_var(20, 30))

# 람다 함수 -> 할당
lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50, 50))


def func_final(x, y, func):
    print(">>>>>", x * y * func(10, 10))


func_final(10, 20, mul_func_var)
