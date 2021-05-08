# Python unterstützt elementare Rechenoperationen wie Addition und Subtraktion:

3 + 3   # Beispiel für die Addition

3 - 2   # Beispiel für die Subtraktion

# Python unterstützt ebenfalls die Multiplikation und Division

3 * 3     # Multiplikation

3 * 3 * 3 
3 ** 3       # Potenzierung geht über den **

27 ** (1 / 3)  # Beispiel für die dritte Wurzel aus 27

3 / 2     # Division

# Weitere Operationen die häufig in Programmiersprachen verwendet werden
# sind die sogenannte Floor Division und der Rest

5 // 3   # Ganzzahlige Floor Division
5 % 3    # Modulu Operation

# 1) Werden Klammern evaluiert
# 2) Potenzierung evaluiert
# 3) Multiplikation, Ganzzahlike Division...
# 4) Addition und Subtraktion

a = 3 ** 3
b = 14

a = int(input('Please enter a number\n'))
b = int(input('Please enter another number\n'))

## Datentypen

# Zahlen (ints, floats)
integer_number = 3
type(3)

floating_point_number = 3.1
type(floating_point_number)

# Strings
s = 'Hallo Welt!'

s[0]  # Erster Charakter
s[1]  # Zweiter Charakter

s[0:3]  # Alles von dem ersten bis zum 3 (exklusive)
s[3:7]  # Alles von dem vierten bis zum 6. Eintrag

s[-1]

s[::-1]  # In umgekehrter Reihenfolge

'5' + '3'  # Addition für Strings ist definiert

# Listen
example_list = [1, 2, 3, 4, 5]

example_list[0]    # Ausgabe des ersten Elements
example_list[-1]   # Ausgabe des letzten Elements

example_list[::-1]

new_list = list(range(10,20))  # Schnelle Erstellung einer Liste von 10 bis 20

# Verschachtelte Listen
nested_list = [list(range(3)), list(range(3,6))]
nested_list[1][0]

# Funktionen auf Listen
len(example_list)
sum(example_list)

example_list.append(6)
print(example_list)

list_1 = list(range(3))
list_2 = list(range(3,6))

new_list = list_1 + list_2
new_list = new_list + [6]
new_list += [7]   # Das gleiche wie new_list = new_list + [7]

x = 1
x = x + 1
print(x)


# Dictionaries
# Ein Dictionary ist ein nicht geordneter Datentyp, der aus key-value pairs besteht.



example_dict = {
    'Milan': {  
        'age': 30,
        'employer': 'Deutsche Bank'
    },
    'Doron': {
        'age': 27,
        'employer': 'FinKred' 
    },

    'Laura': {
        'age': 24,
        'employer': 'Deluitte' 
    },

    'Timo': {
        'age': 26,
        'employer': 'DeZettBank'
    },

    'Hubertus': {
        'age': 23,
        'employer': 'KPNE'
    },

    'Anna': {
        'age': 27,
        'employer': 'CSR-Bank' 
    },

    'Lisa': {
        'age': 25,
        'employer': 'DataScienceLab' 
    },

    'Christian': {
        'age': 22,
        'employer': 'PEWECE' 
    },

    'Leon': {
        'age': 33,
        'employer': 'McKy' 
    },

    'Tom': {
        'age': 21,
        'employer': 'Sparküche Bochum' 
    },

    'Jonas': {
        'age': 27,
        'employer': 'SularisBank' 
    },

    'Philipp': {
        'age': 29,
        'employer': 'BECEGE' 
    },

    'Alexander': {
        'age': 31,
        'employer': 'ELGe'
    },

    'Maximilian': {
        'age': 28,
        'employer': 'IFU'
    },

    'Kasimir': {
        'age': 27,
        'employer': 'NBER' 
    },

    'Niklas': {
        'age': 27,
        'employer': 'RUBInvest' 
    },

    'Tobias': {
        'age': 22,
        'employer': 'CobraBank' 
    },

    'Max': {
        'age': 26,
        'employer': 'CreditRiskLab' 
    },

}

example_dict['Doron']['age'] = 29

example_dict['Milan']['city'] = 'Frankfurt'

example_dict.clear()   # Clears all entries in the dictionary
example_dict    
del example_dict       # Completely deletes the variable example dict and frees up memory

## Logische Operatoren

# Zahlen

x = 3
y = 5
z = 3

# Entspricht dem ist gleich

x == z
x 

# Größer > und größer gleich >=
6.1 > 6

# Analog Kleiner < und kleiner gleich <=
3 < 5
3 < 3
3 <= 3

# Strings
s1 = 'Hallo Welt!'
s2 = 'Nicht Hallo Welt!'
s3 = 'Hallo Welt!'


# Listen
l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,3,2]

l1 == l2

l1 == l3

# Dictionary
d1 = {'Milan': 30, 'Doron': 27}
d2 = {'Milan': 31, 'Doron': 25}
d3 = {'Doron': 27, 'Milan': 30}

d1 == d3

### and or keywords

# And
5 > 3 and 3 == 3
5 > 3 and 3 == 5
False and True
False and False

# Or
True or True
True or False
False or True
False or False

# Negation not
not True
not False

# If condition

import random
random.randint(0,100)

number = random.randint(0,100)
number = 55

if number < 10:
    print('The number is less than 10')
elif number >= 10 and number < 20:
    print('The number is greater than 10 and less than 20')
elif number >=20 and number < 30:
    print('The number is greater than 20 and less than 30')
else:
    print('The number is greater than 30')


# While Loop


mylist = []
i = 0
while i < 5000:
    mylist.append(random.randint(0,100))
    print(i)
    i += 1    # i = i + 1

sum(mylist)/(len(mylist))

# Summe der ersten n-Zahlen entspricht n(n+1)/2

i = 0
total = 0
while i <= 550:
    total += i
    i += 1

# for loop:


n = 100
total = 0
for element in range(n+1):
    total += element
print(total)











