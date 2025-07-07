H, M = map(int, input().split())

if M < 45:
  new_M = 60 + (M - 45)
  new_H = H - 1
else:
  new_M = M - 45
  new_H = H

if new_H < 0:
  new_H = 23

print(new_H, new_M)