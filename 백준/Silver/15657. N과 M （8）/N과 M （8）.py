N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))

def generate_sequence(sequence, start):
    if len(sequence) == M:
        print(*sequence)
        return
    for i in range(start, N):
        generate_sequence(sequence + [numbers[i]], i)

generate_sequence([], 0)