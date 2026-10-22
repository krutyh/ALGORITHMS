s = input().strip()
stack = []
ans = True

for c in s:
    if c in ['(', '[', '{']:
        stack.append(c)

    elif c in [')', ']', '}']:
        if len(stack) != 0 and (
            (c == ')' and stack[-1] == '(') or
            (c == ']' and stack[-1] == '[') or
            (c == '}' and stack[-1] == '{')
        ):
            stack.pop()
        else:
            ans = False
            break

if len(stack) != 0:
    ans = False

print('yes' if ans else 'no')
