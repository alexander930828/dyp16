import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
reverse_num = num[::-1]

increase = [1]*(n)
decrease = [1]*(n)

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_num[i] > reverse_num[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0] * (n)
for i in range(n):
    result[i] = increase[i] + decrease[n-i-1] -1

print(max(result))