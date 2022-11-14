# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700
# 출력
print(n)
print(type(n))
print()

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

# 선언
var = 75
# 재선언
var = "Change Value"
# 출력
print(var)
print(type(var))

# Object Reference
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(n), type(m))
print()

# id(identity) 확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
# 파이썬은 내부적으로 같은 값이면 주소값을 같이 한다. (효율성)
m = 500
n = 500

print(id(m), id(n))
print(id(m) ==  id(n))

#다양한 변수 선언
# Camel Case: numberOfCollege
# Pascal Case: NumberOfCollege
# Snake Case: number_of_college_graduates 파이썬의 변수 선언할 때

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
__age = 6
age__ = 7
_AGE_ = 7

#예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""








