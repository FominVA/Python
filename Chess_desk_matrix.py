# Шахматная доска
# Входные данные: 3 4
a = input().split()
n = int(a[0])
m = int(a[1])
desk = []

for i in range(n):
    temp = ['.']*m
    desk.append(temp)
    
for i in range(n):
    for j in range(m):       
        if i%2 == 0 and j%2 != 0:
            desk[i][j] = '*'
        elif i%2 != 0 and j%2 == 0:
            desk[i][j] = '*'
            
for i in range(n):
    for j in range(m):
        print(' '.join(str(desk[i][j])), end =' ')
    print()


    changes

changes1
