# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많으 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
# () 튜플 [] 리스트 {} 딕셔너리
a = {'name': 'kim', 'phone': '010', 'birth': 3}
b = {0: 'hello'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'name': 'niceman',
    'city': 'seoul',
    'age': 33
}

e = dict([
    ('name', 'niceman'),
    ('city', 'seoul')
])

f = dict(
    Name='niceman',
    Lge=33,
    status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력

# print('a - ', a.get['name']) # 존재 -> None 처리
# 벨류값 가져와라
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('status'))
print('f - ', f.get('Name'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 키의 길이
print('a -', len(a))
print('b -', len(b))
print('c -', len(c))
print('d -', len(d))

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능

print('a - ', a.keys())  # 키만 가지고 옴
print('b - ', b.keys())
print('c - ', c.keys())
print('a -', list(a.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())

print('a ', list(a.items()))

print('a - ', a.pop('name'))
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem())  # LIFO
print('f - ')

print()

print('a - ', 'birth' in a)
print('d - ', 'key' in d)

# 수정
a['test'] = 'test_dict'
print('a - ', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth = 'sdsd')
print('a - ', a)

temp = {'address' : 'busan'}

a.update(temp)
print('a - ', a)

a['birth'] = 300
print(a)