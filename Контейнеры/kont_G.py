n = int(input())
arr = list(map(int, input().split()))

st = []
now = 1

for x in arr:
    st.append(x)
    
    while st and st[-1] == now:
        st.pop()
        now += 1

if len(st) == 0:
    print("YES")
else:
    print("NO")
