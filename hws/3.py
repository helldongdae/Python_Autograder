max = 0
idx = 0
for i in range(10):
    a = int(input())
    if a > max:
        max = a
        idx = i+1
print(max)
