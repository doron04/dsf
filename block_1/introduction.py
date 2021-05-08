# Im Gegensatz zu der Veranstaltung, ist dieses Skript nicht
# mehr linear. D.h. es werden Konzepte wie z.B. Schleifen verwendet
# bevor sie näher erklärt werden.


## 1. Einfache Rechenoperationen

# 1.1 Elementare Rechenoperationen
# Python unterstützt einfache Rechenoperationen mit bekannten Rechenregeln
3 + 3 * 2      # Punkt vor Strichrechnung
(3 + 3) * 2    # Klammern werden zuerst evaluiert

3 ** 3         # Entspricht 3^3 = 27
27 ** (1 / 3)  # Entspricht der 3. Wurzel aus 27 = 3

6 / 3            # Beispiel für die Division

# 1.2 Floor Division und Modulus (Rest)
# Weitere typsche Operationen
5 // 3         # Floor Division -> Entspricht 1
-7 // 3        # Entspricht -3, erste ganze Zahl kleiner als -2,333 

5 % 3          # Modulu Operation, Entspricht 2

# Reihenfolge der Evaluation:
# Zuerst werden Klammern evaluiert
# Dann Potenzierungen
# Dann Multiplikations- und Divisionsoperationen
# Zuletzt Addition und Subtraktion

# Ein erstes sehr einfaches Programm:
# Der Nutzer soll über die built-in input Funktion gebeten werden 2
# Zahlen einzugeben, von diesem soll die Summe zurückgegeben werden.

help(input)  # Gibt den Docstring der input Funktion wieder -> Funktion gibt einen String zurück

a = int(intput('Please enter your first number\n'))   # \n steht für newline, Eingabe in nächsten Zeile
b = int(intput('Please enter your second number\n'))  

print(a + b)  # Printed die Summe an die Konsole

## 2 Datentypen
# Jeder Datentyp und jedes Objekt kann in Python in einer Variable
# oder Konstante gespeichert werden:

x = 3
print(x)

CONSTANT = 1e10   # Variablen die nicht mehr verändert werden sollen
                  # sollten als solche gekennzeichnet sein und groß geschrieben werden

# 2.2 Zahlen (int und float)
type(3)     # Python weist ganzen Zahlen automatisch den Datentype int zu
type(3.1)   # Dezimalzahlen erhalten ebenso automatisch den Datentyp float für Gleitkommazahl (https://de.wikipedia.org/wiki/Gleitkommazahl)

# Alle wesentlichen Operationen sind zwischen diesen Datentypen definiert:
3 * 2.1 ** 2.1 / 0.5 / 2
3 + 2.1 - 1

# Byte Darstellung von ganzen Zahlen
for number in range(-16, 16):
    print(f'{number} in byteform {number:#010b}')  # Ausführungen hierzu im Skript, siehe Gl. 1.1

# Exkurs: Nicht alle rationale/reelle Zahlen lassen sich durch Gleitkommazahlen abbilden
0.5 == 2**(-1)              # Ist in den Maschinenzahlen
0.75 == 2**(-1) + 2**(-2)   # Ist in den Maschinenzahlen

format(0.1, '.20')         # Lässt sich nicht als Gleitkommazahl darstellen (s. Skript S. 4)
(0.1 * 0.1 - 0.01) * 1e20  # Sollte 0 sein
#-------------------------------------------------------------------------------------------

# 2.3 Strings
# Kann durch single quotes ' oder double quotes " definiert werden
s = 'Hallo Welt'
s = "Hallo Welt"

# Zugriff auf einzelne Elementen über string[#:#]
s[0]     # erstes Element
s[1]     # zweites Element
s[-1]    # letztes Element
s[-2]    # vorletztes Element
s[0:3]   # ersten 3 Elemente
s[1:4]   # zweites bis zum 4. Element
s[::-1]  # in umgekehrter Reihenfolge

# Multiline strings über triple Quotes
s_long = '''This is a 
very long string.'''

# Einige Special Character in Strings
print('Hello\nWorld')  # \n startet eine neue Zeile
print('Hello\tWorld')  # \t fügt einen Tab ein
print('Special Character \\')  # \ als eine 'escape sequence'

# Raw Strings
print(r'Hello\tWorld')  # Zeigt den String 'as is' -> nützlich für regex Operationen

# Formated Strings
some_number = 13
print(f'We can insert variables: {some_number}')  # f'{}' Variablen in geschweifter Klammer

# Addition von Strings
s1 = 'Hallo'
s2 = 'Welt'
print(s1 + ' ' + s2)

# Exkurs: string + string ist ineffizient:
import random
import time
str_length = 1000000
string_list = [str(random.randint(0,99999)) for x in range(str_length)]

s_0 = time.time()
long_string = ''
for string in string_list:
    long_string += string
print(time.time()-s_0)   # 1.01 for   n=1000000

s_0 = time.time()
long_string = ''.join(string_list)
print(time.time()-s_0)    # 0.077 for n=1000000

# Grund: Strings sind immutable, d.h. in Zeile 112 wird die Variable long_string
# jedes mal neu erstellt. str.join() ist eine built-in string Methode, die diese
# Problematik umgeht.
#-------------------------------------------------------------------------------

# 2.4 Listen
example_list = [1, 2, 3, 4, 5]

# Datenzugriff analog zum string...
example_list[0]     # Ausgabe des ersten Elements
example_list[-1]    # Ausgabe des letzten Elements

example_list[::-1]  # in umgekehrter Reihenfolge

# ... aber nicht immutable, d.h. reassignment ist möglich:
example_list[1] = 11
print(example_list)

# Kompakte Erstellung einer Liste:
example_list = list(range(1,6))  # Inklusive 1, Exklusive 6

# Verschachtelte Listen: 
nested_list = [
    list(range(3)),
    list(range(3,6))
    ]

print(nested_list)
nested_list[0]     # Erstes Element der äußeren Liste ist wieder eine Liste...
nested_list[0][0]  # und kann wiederum nach dem ersten Element gefragt werden

# Kann sozusagen als zwei dimensionale Matrix aufgefasst werden:
#    0  1  2
# 0 [0, 1, 2]
# 1 [3, 4, 5]

nested_list[0][0]  # Erste Liste, erstes Element
nested_list[0][1]  # Erste Liste, zweites Element
nested_list[1][0]  # Zweite Liste, erstes Element
nested_list[1][1]  # Zweite Liste, zweites Element

# Funktionen und Methoden von Listen
len(nested_list)      # nested list hat 2 Listen als Elemente
len(nested_list[0])   # die erste dieser Listen hat 3 ints als Elemente
sum(example_list)     # Summe der Einträge
min(example_list)     # kleinstes Element
max(example_list)     # größtes Element

example_list.append(11)  # hängt ein zusätzliches Element an das Ende der Liste

# Addition von Listen
l1 = list(range(3))
l2 = list(range(3,6))
print(l1 + l2)      # Hängt die Listen aneinander, nicht kommutativ!
l1 + l2 == l2 + l1  # Reihenfolge von Bedeutung

new_list = l1 + l2
print(new_list)
# Alternative Schreibweise für append:
new_list += [6]  # Kurz für new_list = new_list + [6]

# 2.5 Dictionaries
# Ein Dictionary ist ein nicht geordneter Datentyp, der aus key-value pairs besteht.

from input import example_dict as nested_dict
# Wenn der obige import nicht funktioniert, tested ob 
# der Befehl pwd (in der Shell) den Folder block_1 rausgibt
# Falls nicht, navigiert mit cd im Terminal zu dem Ordner

nested_dict['Milan']         # Gibt wieder ein Dictionary zurück
nested_dict['Milan']['age']  # ... wodurch abermals nach einem key gefragt werden kann

nested_dict['Milan']['age'] = 28            # Bestehende Einträge können einfach überschrieben werden
nested_dict['Milan']['city'] = 'Frankfurt'  # und neue angelegt werden

len(nested_dict)             # Anzahl der key value pairs
del nested_dict['Milan']     # bestehende Einträge können gelöscht werden
len(nested_dict)             

example_dict.clear()         # Löscht alle Einträge -> leeres dict
print(example_dict)

# 3 Logische Operatoren
# Aussagen können entweder True oder False sein

# 3.1 Vergleiche von Zahlen (ints und floats)
3 == 3   # Entspricht der Gleichheit
5 > 3    # Entspricht dem größer als
3 > 3    
3 >= 3   # Entspricht dem größer gleich
5 < 3    # kleiner als und gleich analog
3 != 4   # Entspicht dem ungleich
3 != 3   

# 3.2 Vergleiche von Strings
s1 = 'Hallo Welt!'
s2 = 'Nicht Hallo Welt!'
s3 = 'Hallo Welt!'

s1 == s2
s1 == s3

# 3.3 Vergleich von Listen
# Reihenfolge ist von Bedeutung
l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,3,2]

l1 == l2
l1 == l3

# nicht jedoch für sets, i.e.
set(l1) == set(l3)   # Entspricht der Menge, i.e. {1,2,3}

# 3.4 Vergleich von Dictionaries
# Ordnung ist ebenfalls nicht von Bedeutung für Dictionaries:
d1 = {'Milan': 30, 'Doron': 27}
d2 = {'Milan': 31, 'Doron': 25}
d3 = {'Doron': 27, 'Milan': 30}

d1 == d2
d1 == d3

# 3.5 Verknüpfung von Aussagen
# Siehe Skript Table 2 
# AND
True and True  
True and False
False and True
False and False

# OR
True or True
True or False
False or True
False or False

# Negation
not True
not False

## 4 If Condition
import random                   # Importiert Funktionen random.function_name aufgerufen werden können
number = random.randint(1,100)  # Gibt eine ganze Zahl zwischen 1 und 100 zurück

# If keyword gefolgt von einem Statement das True oder False ist:
if number > 50:
    print('This statement will only show'\
         'if the random number is > 50!')

if True:
    print('This will always print')

# Man kann auch deutlich granularer Konditionen abfragen:
if  random_number  <= 10:
    print(’The  roll  was  below or  equal  to 10’)
elif  random_number  <= 20:
    print(’The  roll  was  below or  equal  to 20’)
elif  random_number  <= 30:
    print(’The  roll  was  below or  equal  to 30’)
else:
    print(’The  roll  was  greater  than 30’)

# Weitere Konditionen 
for number in [3, 6, 10, 11]:
    if number >= 5 and number <= 10:
        print('number is between 5 and 10')

for number in [7, 10]:
    if not(number<=5 or number>=10):
        print('number is between 4 and 9')

# In Line If Condition
for statement in [0,1]:
    x = 3 if statement else 5
    print(x)

# In vielen professionellen Programmen sieht man oftmals statements wie:
some_list = []
if some_list:
    print('do something')

print(bool(some_list))  # Leere Listen werden als False evaluiert

some_list.append(0)     
print(bool(some_list))  # Nicht leere Listen als True

# Im Folgenden einige der häufigsten Konditionen die in If-Statements
# vorkommen:
print(bool(''))         # Emptystring wird als False gewertet
type('')                # ist aber vom type string (nicht None)
print(bool('a'))        # Jeder nicht leere string wird als True gewertet
print(bool(None))       # None evaluiert zu False
print(bool(0))          # 0 (type int) wird zu False evaluiert...
print(bool(-1))         # ...jeder andere float/int Wert zu True

## Loops
# 5.1 While Loop
# Es wird Gleichung 3.1 aus dem Skript in einem kleinen Programm
# festgehalten:

i = 0   # Variable welche im Block der While Loop erhöht und in der..
        # .. Eintrittsbedingung abgefragt wird
first_n_numbers = int(input('Enter  integer\n'))

result = 0
while i < first_n_numbers:
    i += 1
    result += i

print(f'Ergebnis der numerischen Lösungs: {result}\n'\
      f'Ergebnis der analytischen Lösung: '\
      f'{int(first_n_numbers*(first_n_numbers+1)/2)}')


# 5.2 For Loop
# Wir nutzen das gleiche Beispiel:
first_n_numbers = int(input('Enter  integer\n'))

result = 0
for i in range(1, first_n_numbers+1):
    result+=i

print(f'Ergebnis der numerischen Lösungs: {result}\n'\
      f'Ergebnis der analytischen Lösung: '\
      f'{int(first_n_numbers*(first_n_numbers+1)/2)}')

# 5.3 Erstellen von Listen & Dictionaries mit Schleifen &
# If-Konditionen
even_numbers = [x for x in range(100) if x%2 == 0]
uneven_numbers = [x for x in range(100) if x%2 != 0]

# Summe der ersten 100 Zahlen
sum([x + 1 for x in range(100)])

# Dictionary füllen
example_dict = {k: v for k, v in zip('ABC', range(3))}
print(example_dict)
help(zip)

# Eine elegantere Lösung:
print(dict(zip('ABC', range(3))))

## 6 Funktionen
# 6.1 def Keyword & default Argumente
# Wir greifen abermals das Summenbeispiel auf:

def sum_of_first_n_numbers(
    end,        # Notwendiges Argument
    start = 1   # Argument mit Default Wert
    ):
    '''Funktion zur Berechnung der Summe aller ganzen
    Zahlen in einem Intervall.
    '''
    return sum(range(start, end + 1))

print(sum_of_first_n_numbers(100))     # mit Default Start Wert
print(sum_of_first_n_numbers(100, 5))  # Default Startwert überschrieben
print(
    sum_of_first_n_numbers(
        start=15,                      # Startwert wird explizit angegeben
        end=150                        # Endwert wird explizit angegeben
        )
      )

help(sum_of_first_n_numbers)           # Gibt den Docstring und den Funktionsheader zurück

# 6.2 Lambda Funktionen als Kurzschreibweise für Funktionsdefinitionen
# Wird nur für sehr einfache überschaubare Funktionen verwendet
sum_of_numbers = lambda start, end: sum(range(start, end+1))
sum_of_numbers(1,100)  # Gleicher Output, keine optionalen Argumente

# OPTIONAL / EXKURS 6.3 args & kwargs
# 6.3.1 args
# Wenn man die Anzahl der Argumente bei der Funktionsdefinition noch nicht
# kenn, kann man dies mit *args kennzeichnen.

def sum_some_numbers(*args):    # * ist notwendig, args Konvention, *numbs funktioniert ebenso
    '''Args steht hier für eine beliebige Anzahl an
    Argumenten die in der Funktion als Tupel abrufbar sind.
    '''
    print(args)
    print(type(args))
    return sum(args)

sum_some_numbers(1, 45, 8, 11, 15)

# 6.3.2 kwargs
# Ähnlicher Use-case wie für *args, lediglich mit benannten argumenten (keyword arguments)

def kwargs_example(**kwargs):   # ** ist notwendig, kwargs ebenfalls eine Konvention
'''Einfaches Funktionsbeispiel zur Veranschaulichung
 des **kwargs Fuktionsarguments'''
    print(kwargs)
    return list(kwargs.keys()), list(kwargs.values())

keys, values = kwargs_example(first_arg=3, second_arg=5, third_arg=8)
print(keys, values)