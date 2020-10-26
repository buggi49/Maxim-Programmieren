'''import time # ist ein modul, module sind code von andern Leuten den wir in unser Projekt importieren können
i = 2 # integer ganze zahl ohne komma positive und negativ
f = 1.1 # float eine zahl mit komma, positiv und negativ
# ab hier ist der Buchstabe i immer die Zahl 1
print(str(f + 1)) # str konvertiert variablen zu strings (text)
time.sleep(5) # 5 sekunden warten, funktioniert nur wen das modul "time" importiert wurde
'''


'''
import time
s = 'Hallo' # string ist genau das gleiche wie text
s2 = "Hallo" # string
# die variable s ist genau das gleiche wie s2
s3 = "Hallo!123%"
b = True # bool (=boolean)
print("HelloWorld")
Hello = "Test"
print("Hello")
print(Hello) # Gibt "Test" aus
time.sleep(5)
'''


'''
import time
b = True # bool (=boolean)
b2 = False
b3 = 'True'
b4 = 'False'

print(b)
print(b2)
print(b3)
time.sleep(5)
'''


'''
while True: # das bedeutet immer
    print('Hello World')
while False: # das bedeutet niemals
    print('Hello World')
'''


'''
# Hier schreiben wir unsere eigene Funktion
def UnsereDef(i): # def bedeutet Funktion
    z = i + 1
    return z

    # oder
    # i += 1
    # return i

r = UnsereDef(2)
print(str(r))
'''

'''
i = 1
b = 3
if b - 1 == i: # == heißt wenn das gleich ist
    print('Erstes Statement Stimmt')
elif b - 2 == i: # else if, wenn das vorherige statement falsch ist, kann dieses noch greifen
    print('Zweites Statement Stimmt')
elif b - 3 == i: # else if, wenn das vorherige statement falsch ist, kann dieses noch greifen
    print('Drittes Statement Stimmt')
else:
    print('Alle Statements Falsch')
'''
