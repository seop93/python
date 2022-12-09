# Chapter08-1
# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수 위주
# int(), tuple() 자주씀

# 절대값
# abs()

print(abs(-3))

# all, any: iterable 요소 검사(참, 거짓)
print(all([1, 2, 3, '']))  # and
print(any([1, 2, 3, '']))  # or

# chr : 아스키 -> 문자, ord: 문자 -> 아스키
print(chr(67))
print(ord('C'))

# enumerate: 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):  # enumerate 두개를 리턴 앞에 인덱스 번호를 붙여준다. i 를 생성
    print(i, name)


# filter : 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 추출
def conv_pos(x):
    return abs(x) > 2


x = [1, 3, 4, 5, 6, 7, 74, 2]
print(list(filter(conv_pos, [1, -3, 2, 5, 0, 6])))
print(list(filter(lambda x: abs(x) > 2, x)))

# id: 객체의 주소값(래퍼런스) 반환

print(id(int(5)))
print(id(4))

# Len: 요소의 길으 반환
print(len('sdsfdfds'))
print(len([2, 3, 4, 5, 2, 34, 2]))

# max,min : 최대값, 최소값
print(max([1, 23, 4, 5]))
print(max('python'))

print(min([1, 2, 3, 4, 5, 6]))
print(min('abcdefg'))


# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)


print(list(map(conv_abs, [1, 23, 5, -2, -2, 0.2])))
print(list(map(lambda x: abs(x), [1, 2, 34, 3, 4])))

# pow : 제곱값 반환
print(pow(2, 10))

# range : 반복가능한 객체(Iterable) 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))

# round : 반올림
print(round(6.3423, 2))
print(round(5.4))

# sorted: 반복가능한 객체(Iterable)
print(sorted([3,45,6,3,23,11]))
print(sorted(['e','w','d','d','u']))

# sum : 반복가능한 객체(Iterable) 합
print(sum([1,2,3,4,5,6,7]))
print(sum(range(1,101)))

# type: 자료형
print(type(3))
print(type({2,3,4}))
print(type(()))
print(type([]))
print(type({"f":"d"}))

# zip : 반복가능한(Iterable)의 요소를 묶어서 튜플로 반환
print(list(zip([10,20,30],[40,50,60])))
print(type((zip([10,20,30],[40,50,60]))))