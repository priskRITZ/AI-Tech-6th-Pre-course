# while True:
#     print("구구단 몇 단을 계산할까요(1~9)?")
#     dan = int(input())
#     if 1 <= dan and dan <= 9:
#         print(f"구구단 {dan}을 계산합니다.")
#         for i in range(1,10):
#             print(f"{dan} X {i} = {dan*i}")
#     elif dan == 0: # 0 입력시 종료
#         break
#     else: # 9보다 큰 값 입력시
#         print("잘못 입력하셨습니다.")
# print("구구단 게임을 종료합니다")

# try except을 넣어 int(input())에 str 타입 입력시 예외처리 추가해보았다.
while True:
    print("구구단 몇 단을 계산할까요(1~9)?")
    try:
        dan = int(input())
        if 1 <= dan and dan <= 9:
            print(f"구구단 {dan}을 계산합니다.")
            for i in range(1,10):
                print(f"{dan} X {i} = {dan*i}")
        elif dan == 0: # 0 입력시 종료
            break
        else: # 9보다 큰 값 입력시
            print("잘못 입력하셨습니다.")
    except ValueError:
        print("1~9 사이의 정수를 입력해 주세요.")
print("구구단 게임을 종료합니다")


