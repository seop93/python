# chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) # 불변

# 선언

a = ()
b = (1,)  # 원소가 하나 일때는 콤마를 사용해서 튜플임을 알림
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

print(type(a), type(b))

# 인덱싱
print('>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1], d[1])
print('d - ', d[-1])
print('d - ', e[-1])
print('d - ', list(e[-1][1])) # 튜플은 리스트로 형변환이 가능하다

# 수정 x
# d[0] = 1500

# 슬라이싱
print('>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])

# 튜플 연산
print('>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3)) # 3의 위치?
print('a - ', a.count(2)) # 2의 갯수는?

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux') # 팩킹 4개의 원소를 묶다.

print(type(t))
print(t)
print(t[0])
print(t[-1])

# 언팩킹 1
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3 # 이것도 튜플
t3 = 4, # 이것도 튜플
x1, x2, x3 = t2 # 언팩킹
x4, x5, x6 = (4, 5, 6); # 언팩킹

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)