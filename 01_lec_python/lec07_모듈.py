# 함수에 return이 있으면 호출하는 쪽에서 변수에 담아 사용

# 함수 정의
def add(a,b) :
    res = a + b
    return res

# class로 구분 관리해야 함수를 각자 사용할 수 있음
# 그냥 def는 고유 1개만 사용 가능

class PhoneBook :

    #생성자 함수 = 클래스 이름과 똑같은 이름의 함수 : 메모리 초기화 담당
    def __init__(self) :  #self는 메모리를 옮겨담을 주소
        print("init 함수 호출됨")


    def addc(self, a, b):
        res = a + b
        return res

    def loginc(name):
        print(f"{name}님 로그인")

    def loginc22(self, name):
        print(f"{name}님 로그인")

    def loginc33(self, name):
        return name