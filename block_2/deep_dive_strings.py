import regex as re
# 1 Strings Deep Dive
# 1.1 Strings recap

s = 'Data Science in Finance'

s[0]    # selektiert das erste Zeichen des Strings
s[3:5]  # selektiert Zeichen 3 bis 5 (exklusive)
s[::-1]  # gibt den String in umgekehrter Reihenfolge zurück

len(s)  # gibt aus wie lang ein String ist

# 1.2 Rechnen mit Strings!?
'Pizza' == 'Schokolade'  # False

'Pizza' < 'Schokolade'  # True

'Pizza' > 'Schokolade'  # False

# Wieso ist Pizza kleiner als Schokolade?

help(ord)   # die ord() Funktion

ord('A')    # 65
ord('a')    # 97

'A' < 'a'   # True -> 65 < 97

# Der "Wert" eines Wortes ergibt sich aus der Summe seiner Unicode Werte
sum_var = 0
for character in 'Pizza':
    sum_var += ord(character)       # sum_var = sum_var + unc(character)

sum_var

# List Comprehension (gleiches Ergebnis)
sum([ord(character) for character in 'Pizza'])
sum([ord(character) for character in 'Schokolde'])

'Pizza' > 'Schokolade'  # 526 > 924 --> False

# 1.3 String-Sonderzeichen

print('Dies is ein Test-String')     # Keine Sonderzeichen
print('Dies is \n ein Test-String')  # Line-Break "\n"
print('Dies is \t ein Test-String')  # Tab "\t"

# 1.4 Fromatted-String (f-string)

f'{132.1294:.2f}'   # formatieren von floats
f'{10000000:,d}'    # formatieren von integers
f'{10000000:e}'     # scientific numbers

# 1.5 Nutzung von Variablen innerhalb eines f-strings
str_var = 'Emma'
f'{str_var} ist ein großartiger Coder'

# f-string innerhalb eines Loops
results_dict = {}
for i in range(10):
    results_dict[f'topic_{i}'] = []

results_dict


# 1.6 String-Methoden zur Verarbeitung von Strings

# Leerzeichen entfernen
s = '     Emma ist ein     großartiger Coder        '
s.strip()   # alle Leerzeichen rechts und links entfernen
s.lstrip()  # alle Leerzeichen links entfernen
s.rstrip()  # alle Leerzeichen rechts entfernen

# 1.7 Groß- und Kleinbuchstaben

s = 'emma ist ein großartiger Coder'

s.capitalize()  # Erste Buchstabe eines Strings groß
s.title()       # Ersten Buchstaben eines jeden Wortes groß
s.upper()       # Alle Buchstaben groß
"DIES  IST EIN TEST".lower()    # Alle Buchstaben klein

# 1.8 Suchabfragen für Substrings

s = 'Das ist ein Teststring, keine Liste'

'string' in s   # True
'abc' in s      # False


s.index('string')  # identifiziert den Index des Starts des Substrings
s.index('ein')
s.rindex('ein')   # identifiziert den Index des Starts des Substrings (rechts)

s[s.rindex('ein'):]     # Kombination Index und Slicing

s.count('ein')          # zählt wie oft ein Substring vorkommt

# 1.9 Split, Join und Replace

s.split()       # Splittet einen String anhand von Leerzeichen
s.split(',')    # Splittet einen String anhand von Kommata

s = 'Dies ist Linie 1\mDies ist Linie 2\nDies ist Linie 3'

s.splitlines()   # Splittet einen String anhand des Linebreaks (=split('\n'))

letters_list = ['A', 'B', 'C', 'D']

" --> ".join(letters_list)  # Fügt eine Liste zusammen

s.replace('Linie', 'xxx')   # Ersetzt einen Substring

##############################################################################
##############################################################################

# 2. Regular expressions

# Für Regexes wird idR die Raw-String Notation empfohlen, da diese
# intuitiver ist
print('Output von zwei Backslashs > \\\\ <')
print(r'Output von vier Backslashs > \\\\ <')

s = 'Dies ist ein Test-String'

# Regexes bieten viel mehr Informationen
re.search(r'ist', s)

# 2.1 Wildcard und Anchor

# Die Wildcard matcht jedes mögliche Zeichen
re.search(r'.', s)          # matcht das erste Zeichen
re.search(r'Die.', s)       # matcht das 's' von Die(s)
re.search(r'Test.', s)      # matcht das '-' von Test(-)String

# Der Start Anchor ^
re.search(r'^Dies', s)         # matcht, da 'Dies' zu Beginn des Strings steht
re.search(r'^Test', s)         # kein Match, obwohl 'Test' im String enthalten

# Der End Anchor $
re.search(r'ing$', s)         # matcht, da 'ing' am Ende des Strings steht
re.search(r'Test$', s)        # kein Match, obwohl 'Test' im String enthalten

# 2.2 Quantifizierungen von wiederkehrenden Mustern

s = 'XXXXXAAAAA'

# ? matcht Null oder eine Wiederholung des Suchbegriffs
re.search(r'XXX?', s)  # matcht die ersten 3 Xs
re.search(r'XXZ?', s)  # matcht die ersten 2 Xs, kein Error, 0 Matches Z

# + matcht einen oder mehr Wiederholungen des Suchbegriffs
re.search(r'X+', s)    # matcht alle Xs
re.search(r'X+A+', s)  # matcht den gesamten String
re.search(r'XXZ+', s)  # kein Match, da mind. ein Z vorausgesetzt

# * matcht Null oder mehr Wiederholungen des Suchbegriffs
re.search(r'X*', s)    # matcht alle Xs
re.search(r'X*A*', s)  # matcht den gesamten String
re.search(r'XXZ*', s)  # matcht die ersten 2 Xs, kein Error, 0 Matches Z

# {} matcht spezifische Anzahl
re.search(r'X{2}', s)      # matcht genau 2 Xs
re.search(r'X{2,4}', s)    # matcht zwischen 2 und 4 Xs, immer Maximum
re.search(r'X{100}', s)    # kein Match, da mind. 100 X vorausgesetzt


# 2.3 Spezifische Charakterklassen
s = 'dies ist EIN Test_String inkl. Zahlen 837421 + usw.'

# [] Spezifiziert bestimmte Charakterklassen für die Suchanfrage
re.search(r'[A-Z]', s)  # matcht nur Großbuchstaben von A-Z
re.search(r'[A-Z]+', s)  # inkl. +
re.search(r'[0-9]+', s)  # matcht nur Zahlen von 0-9

# \d Numerische Zahlen von 0-9
re.search(r'\d+', s)    # spezifisch: [0-9]+

# \w Buchstabe, eine numerische Ziffer oder das Unterstrichzeichen
re.search(r'\w+', s)    # spezifisch: [a-zA-Z0-9_]+

# \s Jedes Leer-, Tabulator- oder Zeilenumbruchzeichen
re.search(r'\s', s)    # spezifisch: [\r\n\t\f\v ]

# Spezifische Charakterklassen können auch mit ^ verneint werden
re.search(r'\W+', s)    # matcht Leerzeichen von s

# similar to
re.search(r'[^a-zA-Z0-9_]+', s)  # \W+


# 2.4 Greedy und Non-Greedy Matches

s = '<li> <h1> TEXT </h1> </li>'

re.search(r'<.*>', s)   # Greedy Quantifier - matcht alles

re.search(r'<.*?>', s)  # Non-Greedy Quantifier - matcht "kleinsten" match

# 2.5 Der ODER-Operator

re.search(r'<h1>|<li>', s)  # matcht <hi> ODER <li>

re.search(r'<h1>|<li>|</h1>', s)  # kann unendlich erweitert werden

# 2.6 Word Boundaries

s = 'She plays badminton bad'

# keine Boundaries
re.search(r'bad', s)    # matcht bad(minton)

# Wort muss mit 'bad' anfangen
re.search(r'\bbad', s)   # matcht bad(minton)

# d.h. \blearn matcht learn, learning, learned, learnes, etc.

# Wort muss mit 'minton' aufhören
re.search(r'minton\b', s)   # matcht (bad)minton

# somit matcht bad
re.search(r'minton\b', s)   # matcht (bad)minton

# matcht ganz explizites Wort
re.search(r'\bbad\b', s)   # matcht bad


# 2.7 Lookarounds

s = """
    Mrs. Emma Rich ist die Beste. Mr. Richard Smith, ist ein Experte in 
    Machine Learning Applications.
    """

# ?=REGEX: Positiver Lookahead
re.search(r'ist', s)                # matcht span=(20, 23)
re.search(r'ist(?=\sein)', s)       # span=(54, 57)

# ?!REGEX: Negativer Lookahead
re.search(r'ist', s)                # matcht span=(20, 23)
re.search(r'ist(?!\sdie)', s)       # span=(54, 57)

# ?<=REGEX: Positiver Lookbehind
re.search(r'ist', s)                # matcht span=(20, 23)
re.search(r'(?<=Smith,\s)ist', s)   # span=(54, 57)

# ?!REGEX: Negativer Lookahead
re.search(r'ist', s)                # matcht span=(20, 23)
re.search(r'(?<!Rich\s)ist', s)     # span=(54, 57)


# Identifzieren von Namen (Mr/s. VORNAME NACHNAME)
re.search(r'(?<=Mrs?\.\s)[A-Z][a-z]+\s[A-Z][a-z]+', s)

# matcht alle Namen
re.findall(r'(?<=Mrs?\.\s)[A-Z][a-z]+\s[A-Z][a-z]+', s)

# substituiert alle Namen mit GENIUS
re.sub(r'(?<=Mrs?\.\s)[A-Z][a-z]+\s[A-Z][a-z]+', 'GENIUS', s)

# 2.8 Capturing Groups

# der Match kann über .group() aufgerufen werden
re.search(r'(?<=Mrs?\.\s)[A-Z][a-z]+\s[A-Z][a-z]+', s).group()  # 'Emma Rich'

# die obigen Lookarounds können auch mit capture groupings extrahiert werden
# Gruppen werden mit () gesetzt, im Folgenden zwei Gruppen
name_re = re.compile(r'(Mrs?\.\s)([A-Z][a-z]+\s[A-Z][a-z]+)')

name_re.search(s).group()        # gibt kompletten Match aus: Mrs Emma Rich
name_re.search(s).group(1)       # gibt erste Gruppe aus: Mrs.
name_re.search(s).group(2)       # gibt erste Gruppe aus: Emma Rich

# für unsere Aufgabe ist "Mrs. " eine unnütze Information, daher wären hier
# Lookaround zu empfehlen, da für die groups Speicher verbraucht wird.
# Sollte ein Regex jedoch so konstruiert sein, dass mehrere Gruppen relevante
# Informationen enthalten, bieten sich groupings an.

# 2.9 Sonderfunktionen

s = """Dies ist ein Test in Linie 1\n
        Hier kommt Linie 2\n
        Und schließlich Linie 3
    """

# re.DOTALL
# "By default" brechen Quantifizierungen bei Zeilenumbrüchen ab

re.search(r'.*', s)             # matcht ALLES, bricht jedoch nach Linie 1 ab
re.search(r'.*', s, re.DOTALL)  # matcht den gesamten String

# re.IGNORECASE
# "By default" sind Regexes  case-sensitive
s = 'AAAaaa'

re.search(r'a+', s)  # matcht 'aaa'
re.search(r'a+', s, re.IGNORECASE)  # matcht 'AAAaaa'

# re.VERBOSE
# Regexes können komplex werden, sodass Kommentare hilfreich sein können
# durch re.VERBOSE werden Leerzeichen und '#' ignoriert


s = """
    Mrs. Emma Rich ist die Beste. Mr. Richard Smith, ist ein Experte in 
    Machine Learning Applications.
    """

# matcht alle Namen
re.findall(r'(?<=Mrs?\.\s)[A-Z][a-z]+\s[A-Z][a-z]+', s)

# gleiches Ergebnis und überischtlicher, kommentierter Code
re.findall(r"""
            (?<=Mrs?\.\s)       # Lookbehind for "Mr" or "Mrs" followed by space
            [A-Z][a-z]+\s       # Capitalized word followed by space
            [A-Z][a-z]+         # Capitalized word
            """, s, re.VERBOSE)

# NOTE: Daher sollte man sich angewöhnen Leerzeichen mit \s zu definieren
