# 짝수 + 짝수 = 짝수
# 홀수 + 짝수 = 홀수
# 홀수 + 홀수 = 짝수
# 짝수 + 홀수 + 짝수 + 홀수 = 짝수
# 누적합 -> 999,999,900 이므로 불가
# i * (i - 1) / 2 - j * (j - 1) / 2 = N
#  2 =< L = i - j +1 <= 100


# 1. 수열 생성 가능 여부 확인
# 홀수로는 나머지가 없고, 나누어떨어지면 되고, 짝수로는 .5로 나누어떨어져야 함 
# 2.1 홀수
# 나누는 수 3, 나눌 수 3, 몫: 1
# 수열 시작 몫 - 나눌 수 // 2 ~ + 나누는 수 - 1
# 2.2 짝수
# 나누는 수 4, 나눌 수 6, 몫: 1, 
# 수열 시작 몫 - 나눌 수 // 2 ~ + 나누는 수  - 1 

N, L = map(int, input().split())

for i in range(L, min(101, N)):
    A = N / i
    B = N // i
    C = N % i
    if i % 2 == 0 and A - B == 0.5 and B - i // 2 >= 0 : # 나누는 수가 짝수
        for j in range(B - i // 2 + 1, B - i // 2 + i):
            print(j, end=" ")
        exit(0)
    elif i % 2 != 0 and C == 0 and B - i // 2 >= 0: # 나누는 수가 홀수
        for j in range(B - i // 2, B - i // 2 + i):
            print(j, end=" ")
        exit(0)
print(-1)