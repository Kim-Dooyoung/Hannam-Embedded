import sys
from function.print_recipy import get_material_description
from function.webcrawling_food import food_search_function
from function.data_visualization_material import run_material  # 함수 이름 수정
from function.data_visualization_food import run_food  # 함수 이름 수정

# 기능 선택 입력
try:
    option = int(input("기능 선택 (1, 2, 3 중 택): "))
except ValueError:
    print("숫자를 입력해 주세요.")
    sys.exit()


def switch_case(option):
    if option == 1:
        return get_material_description()  # 설명 반환
    elif option == 2:
        return food_search_function()  # 음식 검색 기능
    elif option == 3:
        # 3번 옵션에 대해 switch_case_data를 호출하여 기능 선택
        switch_case_data()
    else:
        print("1, 2, 3 중 하나를 택해주세요.")
        sys.exit()


def switch_case_data():
    # 기능 선택 입력
    try:
        option = int(input("기능 선택 (1, 2 중 택): "))
    except ValueError:
        print("숫자를 입력해 주세요.")
        sys.exit()

    if option == 1:
        run_material()
    elif option == 2:
        run_food()
    else:
        print("1, 2 중 하나를 택해주세요.")
        sys.exit()


# 메인 실행
if __name__ == "__main__":
    print(switch_case(option))
