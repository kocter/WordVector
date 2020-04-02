# -*- coding: utf8 -*-
import re
import numpy as np
import sqlite3




####################### Часть отвечающая за работу с БД #################################
import sqlite3

conn = sqlite3.connect("DataBase/mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

try:
    cursor.execute("""CREATE TABLE testtext
                         (content text)
                      """)
except Exception:
    print('Таблица с тестовыми текстами уже создана')


def FindOneTest():


## Инициализаия БД
    conn = sqlite3.connect("DataBase/mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    try:
        cursor.execute("""CREATE TABLE testtext
                             (content text)
                          """)
    except Exception:
        print('Таблица с тестовыми текстами уже создана')

    sql = "SELECT * FROM Vector"
    cursor.execute(sql)
    a= DelLite(str(cursor.fetchall())) # or use fetchone()
    a=a.split(' ')
    # for word in a:
    #     word = Text.DelLite()
    return a

# Удаляет лишние символы из вывода #
def DelLite(s):
    s = re.sub(r"[)\[\]'(,]", "", s)
    return s



#########################################################################################

def counting(data_list): #Частотный способ

    words_counts = {}
    for text in data_list:
        for word in text.split():
         if word in words_counts:
             words_counts[word] += 1
         else:
            words_counts[word] = 1


    return words_counts

############### Векторизация ##################
def my_bag_of_words(text):
   words_to_index = (WordVec())  # Берем Вектор слов из БД
   size_of_dictionary = len(words_to_index)  # Считает длину словаря
   print(size_of_dictionary)

   word_vector = np.zeros(size_of_dictionary)
   for word in text.split():
       if word in words_to_index:
          word_vector[words_to_index[word]] += 1

   ################# Создание JSON структуры для передачи #########################
   #print(word_vector)
   myArray = []
   for i in range(0, len(word_vector)):
       myArray.append(word_vector[i])

       # myArray.append(article(L[i], List[i]))

   ########################
   import json
   d = dict(value=myArray)

   # print(json.dumps(d, indent=2))
   #################################

   return json.dumps(d, indent=1)




   #return word_vector
################################################


def WordVec():
    index_to_word=FindOneTest()
    words_to_index = {word: i for i, word in enumerate(index_to_word)}
    return words_to_index