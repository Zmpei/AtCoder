n = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
a_list = list(alpha)
name = []
while n // 26 != 0:
    name.append(n % 26 - 1)
    n = n//26
name.reverse()
for a in name:
    print(alpha[a], sep='', end='')
# if n <= 26:
#     print(a_list[n-1])
#
# elif n <= 26 + 26**2:
#     if n % 26 == 0:
#         temp1 = n // 27
#         temp2 = 26
#     else:
#         temp1 = n // 26
#         temp2 = n % 26
#     print((a_list[temp1]), a_list[temp2], sep='')
#     sys.exit()
#
# elif n <= 26 + 26**2 + 26**3:
#     if n % 26 == 0:
#         temp1 = n // 27**2
#         temp2 = n // 27**2
#         temp3 = 26
#     else:
#         temp1 = n // 27**2
#         temp2 = n // 27**2
#         temp3 = n % 26
#     print((a_list[temp1]), a_list[temp2], a_list[temp3], sep='')



