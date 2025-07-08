x = int(input())
N = int(input())

c = 0

for i in range(1, N+1):
    a, b = map(int, input().split())
    c += a * b

if x == c:
     print("Yes")
else:
    print("No")