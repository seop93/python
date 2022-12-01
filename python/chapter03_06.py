# Chapter03_6
# 집합(Set) 특징
# 집합(Set) 자료형(순서x, 중복x)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([3, 4, 5, 6])
d = set([1, 2, 'pen'])
e = {'fdf', 'vd', 'bds'}
f = {43, 'foo', (1, 2, 3), 3,.34}

print('a - ', type(a), a)
print('a - ', type(b), b)
print('a - ', type(c), c)
print('a - ', type(d), d)
print('a - ', type(e), e)
print('a - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])


# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 - ', l2)

#길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print('s1 & s2', s1 & s2)
print('s1 & s2', s1.intersection())

print('s1 | s2', s1 | s2)
print('s1 | s2', s1.union(s2))

print('s1 - s2', s1 - s2)
print('s1 - s2', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 ', s1.isdisjoint(s2)) # false 가 있다는 뜻 반대로 나옴

# 부분 집합 확인 -> 한 집합에 포함이되니?
print(s1.issubset(s2))
print(s1. issubset(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
# list는 append, insert
# set은 add
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7)

s1.discard(3)
print('s1 - ', s1)
s1.discard(7)

s1.clear()
print('s1 - ', s1)

a = [1, 2, 3]
a.clear()
print('a - ', a)