N=int(input())
ans = ''
ans += N // 5 * 'V'
ans += N % 5 * 'I'
print(ans)