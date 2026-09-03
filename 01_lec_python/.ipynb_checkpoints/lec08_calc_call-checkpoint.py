#class 호출 _ < from 모듈 import 클래스 >

#add
from lec_python.lec08_calc import CalcClass   #from 패키지.모듈 import 클래스 호출
cc = CalcClass()                   #정의에 self가 있음 > 클래스 객체 생성 = 내가 부를 이름
a = cc.add(3, 8)       #정의에 return이 있음 > 값이 들어갈 변수 = 객체.함수add(덧셈할 값)
print(a)

#sub
a = cc.sub(10, 2)
print(a)

#mul
a = cc.mul(6, 2)
print(a)

#div
a = cc.div(20, 2)
print(a)