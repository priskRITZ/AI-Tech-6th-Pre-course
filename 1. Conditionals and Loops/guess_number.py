import random

rand_num = random.randint(1,100)
my_num = 999
counter = 0
print("숫자를 맞춰보세요 (1~100)")

while rand_num != my_num:
    my_num = int(input())
    counter += 1
    if my_num > rand_num: # 사용자의 입력값이 rand_num 보다 클 때
        print("숫자가 정답보다 큽니다")
    elif my_num < rand_num: # 사용자의 입력값이 rand_num 보다 작을 때
        print("숫자가 정답보다 작습니다")       
    else: 
        print(f"정답입니다. 난수 생성된 숫자는 {rand_num}입니다")

print(f"정답까지 {counter}번째 시도를 하였습니다.")
