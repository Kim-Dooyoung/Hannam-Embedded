import sys

option = int(input("기능 선택 (1, 2, 3 중 택): "))

# 구현된 기능 삽입 필요


def switch_case(option):
    if option == 1:
        return "1번 기능 구현"
    elif option == 2:
        return "2번 기능 구현"
    elif option == 3:
        return "3번 기능 구현"
    else:
        print("1, 2, 3 중 하나를 택해주세요.")
        sys.exit()


print(switch_case(option))
