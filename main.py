#ввод данных
with open('text.txt', 'r', encoding='utf-8') as f:#чтение информации из файла text.txt
    spis = f.read()#переменная списка 

words = spis.split()#определение слов

length = len(words)#определение количества слов
print('КОличество слов равно:',length)#вывод результата
