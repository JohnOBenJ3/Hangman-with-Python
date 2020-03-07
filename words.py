import re


words_file = open("words.txt", encoding="utf-8")
data = words_file.read()
words_file.close()

words_list = re.findall(r'\w+', data)
