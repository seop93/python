# Chapter06-03
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py: python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추용
# 상대경로: ..(부모디렉토리), .(현재디렉토리) --> 모듈 내부에서만 사

# ex1
import python.sub.sub1.module1 as module
import python.sub.sub2.module2

# 사용
module.mod1_test1()
module.mod1_test2()

print()

python.sub.sub2.module2.mod2_test2()
python.sub.sub2.module2.mod2_test2()

# ex2
from python.sub.sub1 import module1
from python.sub.sub2 import module2 as m2

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test2()
m2.mod2_test2()

print()
# ex3
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()

