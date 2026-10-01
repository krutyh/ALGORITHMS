def f(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

a, b, c, d = map(int, input().split())

if a < 0:
    a, b, c, d = -a, -b, -c, -d

left = -2000.0
right = 2000.0

for _ in range(100):
    m = (left + right) / 2
    if f(m, a, b, c, d) < 0:
        left = m
    else:
        right = m

print(f"{right:.6f}")
