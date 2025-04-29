# put your python code here
n = int(input())
matrix = [input().split() for _ in range(n)]


for j in range(n):
    for i in range(n-1, -1, -1):
        print(matrix[i][j], end = ' ')
    print()