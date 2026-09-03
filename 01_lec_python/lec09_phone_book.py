class PhoneBook:

    def save(self, addr_list):  #1. save할 때 일로 갖고와
        name = input("이름을 입력하세요")
        tel = input("전화번호를 입력하세요")

        addr_list.append([name, tel])
        print(f"{name}, {tel} 저장되었습니다")
        return addr_list   #2. 추가추가 하고 다시 호출로 가져가

    def update(self, addr_list):  #4. update할 때 갖고와
        print("수정")
        search_name = input("수정하려면 이름을 입력하세요")
        update_tel = input("수정할 전화번호를 입력하세요")
        for v in addr_list:
            if (v[0] == search_name):
                v[1] = update_tel
        return addr_list    #5. 수정 다 하면 호출로

    def delete(self, addr_list):
        print("삭제")
        search_name = input("삭제할 사람의 이름을 입력하세요")
        for v in addr_list:
            if (v[0] == search_name):
                addr_list.remove(v)
        return addr_list

    def select(self, addr_list):  #7. select할 때 갖고와
        print(f"{len(addr_list)}건 조회")
        for v in addr_list:
            print(v[0], v[1])   #return할 필요 없으니 생략