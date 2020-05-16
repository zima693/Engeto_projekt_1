'''
author = Jakub Zimolka
'''
import re
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

database = {
    "bob": {
        "name": "bob",
        "pass": "123"
    },
    "ann": {
        "name": "ann",
        "pass": "pass123"
    },
    "mike": {
        "name": "mike",
        "pass": "password123"
    },
    "liz": {
        "name": "liz",
        "pass": "pass123"
    }
}
text_nr = len(TEXTS)
sep = "-"*50

#Vstup uživatele
print("Hello, please login")
print(sep)
user_name = input("User name: ")
if not user_name in database.keys():
    print("User name does not exist! Exiting")
    quit()
user_pass = input("Password: ")
if user_pass != database.get(user_name).get("pass"):
    print("Password does not match! Exiting")
    quit()
print(sep)

user_select = int(input(f"""We have {text_nr} texts to be analyzed.
Enter a number between 1 and {text_nr} to select: """))
if user_select not in range(1,text_nr+1):
    print("Number out of range! Exiting")
    quit()
text = TEXTS[user_select-1]
print(sep)
print(text)

# Analýza textu
slova = re.split(" |-",text)
slova = [slovo.strip("\n") for slovo in slova]
slova = [slovo for slovo in slova if slovo]
pocet_slov = len(slova)
pocet_istitle = sum([slovo.istitle() for slovo in slova])
pocet_isupper = sum([slovo.isupper() for slovo in slova])
pocet_islower = sum([slovo.islower() for slovo in slova])
pocet_isnumeric = sum([slovo.isnumeric() for slovo in slova])
pozice_isnumeric = [slovo.isnumeric() for slovo in slova]
index_numeric = [i for i in range(len(pozice_isnumeric)) if pozice_isnumeric[i] == bool("True")]
cisla = [j for i, j in enumerate(slova) if i in index_numeric]
cisla = sum([int(cislo) for cislo in cisla])

print(f"""{sep}
In the selected text there are:
{pocet_slov} words,
{pocet_istitle} titlecase words,
{pocet_isupper} uppercase words,
{pocet_islower} lowercase words,
{pocet_isnumeric} numeric strings
""")

delky = [len(slovo) for slovo in slova]
delky = sorted(delky)
nejdelsi = delky[-1]

print(sep)
print("X letter word - count")
for i in range(1,nejdelsi+1):
    print(i, "*"*delky.count(i), delky.count(i))

print(sep)
print(f"If we summed all the numbers in this text we would get: {cisla}")
print(sep)