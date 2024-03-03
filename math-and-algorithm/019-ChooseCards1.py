from collections import Counter

N = int(input())
A = Counter(input().split())

red = A['1'] * (A['1']-1) // 2
yellow = A['2'] * (A['2']-1) // 2
blue = A['3'] * (A['3']-1) // 2

print(red + yellow + blue)