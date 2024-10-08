with open('text.txt', 'r', encoding='utf-8') as f:
    spis = f.read()

words = spis.split()

length = len(words)
print('КОличество слов равно:',length)