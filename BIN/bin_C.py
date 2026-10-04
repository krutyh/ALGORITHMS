import math

c = float(input())

left = 0.0
right = math.sqrt(c)

for _ in range(100):
    m = (left + right) / 2
    val = m**2 + math.sqrt(m)

    if val < c:
        left = m
    else:
        right = m

print(f"{right:.7f}")
