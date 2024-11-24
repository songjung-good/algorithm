import sys
input = sys.stdin.read

# 입력 처리
data = input().split()
N = int(data[0])
N_lst = list(map(int, data[1:]))

# 정렬
N_lst.sort(reverse=True)

# 출력
sys.stdout.write('\n'.join(map(str, N_lst)) + '\n')