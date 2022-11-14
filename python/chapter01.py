# Chpater 02 - 1
# 파이썬 완전 기초
# print 사용법
#

# 기본 출력
print(' Python Start!')
print(" Python Start")
print(''' Pyton Start! ''')
print(""" Python Start! """)

print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
print('Welcome to', end='     ')
print('IT News', end=' ')
print('Web Site')

# file옵션

import sys

# print('Learn Python', file='test.txt')
print()

# format사용(d : 3, s :'python', f: 3.1445454)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s
#10칸 만드는데 빈공간은 왼쪽부터
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

#10칸 만드는데 빈공간은 오른쪽부터
print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

#왼쪽부터 달러로 채우고 nice문 출력
print('{:$>10}'.format('nice'))
#중앙정렬
print('{:^10}'.format('nice'))
#절삭
print('%.5s' % ('Pythonstudy'))
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f
print('%1.18f' % (3.141114124324))
print('{:f}'.format(3.1512412421143))

print('%06.2f' % (3.14124324324234))
print('{:06.2f}'.format(3.1342434242423))