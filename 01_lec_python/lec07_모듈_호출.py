# 함수 호출
# 어디에 def가 있는지 알려줘야 함

#[기본 문법]
 #from 모듈명 import 함수 or 클래스
 #변수 = 함수(값)
 #수행코드(변수)

from lec07_모듈 import add
son = add(4, 5 )
print("받았음", son)

import lec07_모듈 as aa
son = aa.add(4, 5)
print("받았음", son)

#------------------------------------------------
 #from 모듈명 import 클래스명  as  별칭
 #변수 = 별칭.함수(값)
 #수행코드(변수)

from lec07_모듈 import PhoneBook
PhoneBook.loginc("jm")

#------------------------------------------------
#클래스 메모리 주소 확인 (객체가 만들어질 때 기본적으로 세팅해놓는 곳)
pb = PhoneBook()
print(pb)

a = pb.addc(5,3)  #클래스를 만들어놨기 때문에 ""pb.""함수, 리턴 걸어놨기 때문에 a에 담음
print(a)

#------------------------------------------------

PhoneBook.loginc("홍길동")

pb.loginc22("jm")  #리턴이 없기 때문에 a와 같은 변수에 담지 않고 바로 호출

bb = pb.loginc33("jm")
print(f"{bb}님 로그인")

