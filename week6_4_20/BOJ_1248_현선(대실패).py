
# 접근 : 얘는 -10부터 10까지 안다.
# N의 최대값은 10
# -10 ~ 10까지 수를 가지고 N개를 뽑는 순열.
# 일단 N개 뽑아서, 조건에 맞으면 그놈 출력, 아니면 다른 순열 뽑아서 다시
# 아니 근데 중복될 수도 있네 

# 실패


def check(idx):
    total = 0
    for i in range(idx, -1, -1):
        total += sel[i]
        print(i, idx)
        if total > 0 and S_list[i][idx] == '+':
            return True
        elif total < 0 and S_list[i][idx] == '-':
            return True
        elif total == 0 and S_list[i][idx] == '0':
            return True
    return False


def soonyeol(level):
    if level >= N:
        return sel
    for i in range(-10, 11, 1):
        sel[level] = i
        # 만약 하나씩 돌면서 조건에 부합하면? 순열 원소 추가
        if check(level):
            soonyeol(level+1)

N = int(input())
S = input()
S_list = [S[:len(S)//2], S[len(S)//2:]]
sel = [0] * N
print(soonyeol(0))
