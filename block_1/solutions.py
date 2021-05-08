# Aufgabe 1

nums = [1, 2, 3, 4, 5]

# Part a)
for i in range(1, len(nums) + 1):
    print(nums[:i])

# Part b)
for i in range(len(nums)):
    print(nums[i:])

# Aufgabe 2 
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Hierbei geht es darum die Matrix einmal
# zu transponieren. 

for column in range(len(grid[0])):
    for row in range(len(grid)):
        print(grid[row][column], end='')
    print('')