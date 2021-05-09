f1 = open("book1.txt","r",encoding='utf-8')
f2 = open("book2.txt","r",encoding='utf-8')
book1 = set(f1.read().split())
book2 = set(f2.read().split())
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

for x in book1:
    for char in x:
        if char in punc:
            x = x.replace(char, "")
for x in book2:
    for char in x:
        if char in punc:
            x = x.replace(char, "")            

book3 = book1.intersection(book2)
print(book3)