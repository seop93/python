# Chapter04-3
# 파이썬 반복문
# While 실습

# while <expr>:
#      <statement(s)>

# ex1
n = 5
while n > 0:
    print(n)
    n -= 1

# ex2
a = ["foo", "bar", "baz"]

while a:
    print(a.pop())

# ex3
# break, continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)

print("Loop Ended")

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print("Loop Ended")

# if 중첩

i = 1

while i <= 10:
    print("i", i)
    if i == 6:
        break
    i += 1

# While - else

n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')

# ex7

a = ["bar", "kim", "lee", "kang"]
s = "kang"
i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1

else:
    print(s, "not found")

print(i)

while True:
    print(a)
    if not a:
        break
    print(a.pop())