while True:
    print("구구단 몇 단을 계산할까요(1~9)?")
    dan = int(input())
    if dan > 9:
        continue
    elif dan == 0:
        break
    print(f"구구단 {dan}을 계산합니다.")
    for i in range(1,10):
        print(f"{dan} X {i} = {dan*i}")
print("구구단 게임을 종료합니다")
 