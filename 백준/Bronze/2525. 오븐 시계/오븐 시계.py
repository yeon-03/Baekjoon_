a, b = map(int, input().split())
c = int(input())

new_a = a + (b + c) // 60

if b + c >= 60:
  new_b = (b + c) % 60
  if new_a > 23:
    new_a = new_a % 24
  else:
    new_a = new_a
else:
  new_b = b + c
  new_a = a

print(new_a, new_b)