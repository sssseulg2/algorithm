while True:
    string = input()

    if string == '.':
        break

    stack = []

    for i in string:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)

        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
            
    if not stack:
        print('yes')
    else:
        print('no')
