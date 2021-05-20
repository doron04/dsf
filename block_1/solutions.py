# Übungsaufgaben Block I

# Aufgabe 1
nums = [1, 2, 3, 4, 5]

# Lösung Part a)
for i in range(1, len(nums) + 1):
    print(nums[:i])

# Lösung Part b)
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

# Lösung
for column in range(len(grid[0])):
    for row in range(len(grid)):
        print(grid[row][column], end='')
    print('')


# Aufgabe 3
items = ['Emma', 123, 434, 'is', 132, 'a great', 312, 'coder']

# Hier sollen die str und in Werte von einander getrennt werden
# und in zwei Listen gespeichert werden.

# Lösung mit For Loop
str_list = []
int_list = []
for item in items:
    if isinstance(item, str):
        str_list.append(item)
    elif isinstance(item, int):
        int_list.append(item)


# Lösung mit List Comprehensions
str_list = [item for item in items if isinstance(item, str)]
int_list = [item for item in items if isinstance(item, int)]


# Aufgabe 4
text = input()

# Hier soll getestet werden, ob der input() nicht länger als 250 Zeichen ist

# Lösung
if len(text) > 250:
    print("Der Text ist zu lang, versuchen Sie es erneut")
    del text

else:
    print(text)


# Aufgabe 5
# Hier soll eine Funktion geschrieben werden, die für einen beliebigen Integer
# die Collatz-Sequenz ausgibt

# Lösung
def sequencer(i):
    """
    This function returns a collatz sequence
    """
    # set while loop
    while i != 1:

        # test if even
        if i % 2 == 0:
            i = i/2
            print(int(i))

        # else (if uneven)
        else:
            i = i * 3 + 1
            print(int(i))


# Aufgabe 6
# Hier soll eine Funktion geschrieben werden, die für eine vorgegebene range()
# alle Primzahlen ausgibt

# Lösung
def get_prime_nums(lower, upper):
    """
    This function returns all prime numbers for a given range
    """

    for num in range(lower, upper + 1):

        # all prime numbers are greater than 1
        if num > 1:

            # iterate through possible factors
            for i in range(2, num):

                # break loop is num is not a prime number
                if (num % i) == 0:
                    break

            # else: print prime number
            else:
                print(num)


# Aufgabe 7
items = [['DE', 998, 134, 412], ['UK', 123, 432, 124],
         ['ITA', 652, 435, 324]
         ]

# Hier soll die Liste in ein Dictionary transformiert werden, wobei die jeweils
# ersten Einträge die Keys und die Zahlen die Values darstellen sollen.

# Lösung mit For Loop
item_dict = {}

for item in items:
    item_dict[item[0]] = item[1:]

# Lösug mit Dictionary Comprehension
item_dict = {item[0]: item[1:] for item in items}


# Aufgabe 8
# Hier soll eine Funktion geschrieben werden, die testet ob die values des
# obigen Dictionaries einen bestimmten Grenzwert überschreitenn.

def check_threshold(items, threshold=1500):

    for keys, vals in items.items():
        if sum(vals) > threshold:
            print(keys + " exceeds threshold of " + str(threshold))

        else:
            print(keys + " is fine")


check_threshold(item_dict)


# Aufgbae 9
nums = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]

# hier soll mittels filter() eine Lambda Funktion geschrieben werden,
# welche die Liste auf Werte > 5 filtert

# Lösung


def list_filter(x): return x > 5


list(filter(list_filter, nums))

# Alternativer Weg über For Loop bzw List Comprehension:
filtered_list = [num for num in nums if num > 5]


# Aufgabe 10*
tup1 = [(0, 2), (1, 1), (2, 2), (3, 2), (4, 1), (5, 1)]
tup2 = [(0, 5), (1, 2), (2, 2), (3, 1), (4, 0), (5, 4)]

# Hier soll eine Function geschrieben werde, welche die y-Werte der obigen
# Listen mit Tuples (x, y) summiert.

# Lösung mit For Loop


def sum_tuple_y(tup_list):
    """
    Given a tuple of (x, y) this function sums the y-values of 
    a list of tuples.
    """
    sum_y = 0
    for tup in tup_list:
        sum_y += tup[1]

    return sum_y


sum_tuple_y(tup1)

# Lösung mit List Comprehension


def sum_tuple_y(tup_list):
    """
    Given a tuple of (x, y) this function sums the y-values of 
    a list of tuples.
    """
    return sum([tup[1] for tup in tup_list])


sum_tuple_y(tup1)

# Aufgabe 11*

# Hier soll eine Function geschrieben werde, welche die y-Werte der obigen
# Listen mit Tuples (x, y) entlang der x-Werte summiert.

# Lösung


def sum_tuple_x(tup1, tup2):
    """
    Given two lists of tuples of (x, y) this function sums the y-values of 
    across all x-values and returns the output in a dictionary.
    """

    # collect all tuple values in one larger list
    tuple_values = []
    for tup_list in [tup1, tup2]:

        tuple_values += [tup for tup in tup_list]

    # create empty dict
    output = {}

    # iterate through tuple_values
    for x, y in tuple_values:

        # check if entry exists and append dict
        if x in output.keys():
            output[x] += y
        else:
            output[x] = y

    return output
