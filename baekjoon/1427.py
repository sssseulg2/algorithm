N = input()

str_N = sorted(list(str(N)))
str_N.reverse()
answer = ''.join(str_N)

print(answer)