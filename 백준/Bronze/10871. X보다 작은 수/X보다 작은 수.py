n, x = map(int, input().split())
a = map(int, input().split())

b = []

for i in a:
    if i < x:
        b.append(i)

str_b = map(str, b)
print(' '.join(str_b))