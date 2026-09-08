from lec09_phone_book import PhoneBook

addr_list = []
pb = PhoneBook()  #self가 있기 때문에 pb 변수로 메모리 주소 가져옴

while (True):
    print("______________________________________")
    print("1:등록  2:수정   3:삭제   4:조회   Q:종료")
    menu = input("메뉴를 선택하세요")

    if (menu in ["Q", "q"]):
        print("종료")
        break

    elif (menu == "1"):
        addr_list = pb.save(addr_list)   #3. 추가한 게 저장되면 다시 가져옴 (=클래스 호출 형태)

    elif (menu == "2"):
        addr_list = pb.update(addr_list)          #6. 수정한 게 저장되면 다시 가져옴 (=클래스 호출 형태)

    elif (menu == "3"):
        addr_list = pb.delete(addr_list)

    elif (menu == "4"):
        pb.select(addr_list)        #8. 조회할거 주기만 하는 거


    else:
        print(f"잘못된 메뉴 번호를 선택하셨습니다.")