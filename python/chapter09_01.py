# Chpater08-2
# 파이썬 외장(External)함수
# 실제 프로그램 개발 중 자주 ㅏ용
# 종류 : sys, prickle, shutil, temfile, time, random 등

# ex1 구글 검
import sys

print(sys.argv)

# ex2(강제 종료)
# sys.exit()

# ex3(파이썬 패키지 위치)
print(sys.path)

# pickle : 객체 파일 쓰기
import pickle

# ex4(쓰기)

# f = open("text.obj", 'wb')  # write byte
# obj = {1: 'ptyon', 2: 'study', 3: 'basic'}
# pickle.dump(obj, f)
# f.close()
#
# # ex5(읽기)
# f = open('test.obj', 'rb')  # read byte
# data = pickle.load(f)
# print(data, type(data))
# f.close()

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어 있으면), rename

# ex6
import os
print(os.environ)

# ex7(현재 경로)
print(os.getcwd())

# time: 시간 관련 처리
import time

# ex8
print(time.time())

# ex9(형태 변환)
print(time.localtime(time.time()))

# ex10(간단 표현)
print(time.ctime())

# ex11(형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# ex12(시간 간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(1)

# random : 난수 리턴
import  random

# ex13
print(random.random()) # 0 ~ 1 사이 실수

# ex14
print(random.randint(1,45))
print(random.randrange(1,45))

# ex15(섞기)
d = [1,2,3,4,5,6,7]
random.shuffle(d)
print(d)

# ex16(무작위 선택)
c = random.choice(d)
print(c)

# webbrawser : 본인 OS의 웹 브라우저 실행

import webbrowser
webbrowser.open("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%EC%83%81%EC%86%8D")
webbrowser.open_new("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC+%EC%83%81%EC%86%8D")