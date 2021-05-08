# Task_1

nums = [1, 2, 3, 4, 5]

for i in range(1, len(nums) + 1):
    print(nums[:i])

# Task_2 
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print('')

## Funktionsdefinitionen

import random   # 

# ek = rf + (rm-rf)*beta

def capm(beta, rf=0.03, rm=0.07):
    '''
    Berechnet für gegebenes Beta, RF, und RM die Eigenkapitalrendite
    '''
    return rf + (rm-rf)*beta

print(capm(beta=1.3, rm=0.07, rf=0.03))


x = 1
x += 1  # x = x + 1

def square(number):
    return number**2
