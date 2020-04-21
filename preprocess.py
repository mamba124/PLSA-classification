# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:54:19 2020

@author: Professional
"""
import tensorflow
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import utils

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, MaxPooling1D, Dropout

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer, text_to_word_sequence
###########################
# Чтение файла в текст
##########################
def readText(fileName):
  f = open(fileName, 'r')
  text = f.read()
  text = text.replace("\n", " ")
  
  return text


###########################
# Очистка текста и превращение в набор слов
##########################
def text2Words(text):

  text = text.replace(".", " ")
  text = text.replace("—", " ")
  text = text.replace(",", " ")
  text = text.replace("!", " ")
  text = text.replace("?", " ")
  text = text.replace("…", " ")
  text = text.replace("-", " ")
  text = text.replace("(", " ")
  text = text.replace(")", " ")
  text = text.replace(";", " ")
  text = text.lower()
  
  words = []
  currWord = ""
  for symbol in text[1:]:

    if (symbol != " "):
      currWord += symbol
    else:
      if (currWord != ""):
        words.append(currWord)
        currWord = ""

  if (currWord != ""):
        words.append(currWord)
  
  return words

text = []
text.append(readText('doc1.txt'))
text.append(readText('doc2.txt'))
text.append(readText('doc3.txt'))

words = []
allwords = []
for i in range(len(text)):
  words.append(text2Words(text[i]))
  allwords += words[i]
  
#################
#Преобразовываем текстовые данные в числовые/векторные для обучения нейросетью
#################

maxWordsCount = 100000 #Определяем макс.кол-во слов/индексов, учитываемое при обучении текстов

#Для этого воспользуемся встроенной в Keras функцией Tokenizer для разбиения текста и превращения в матрицу числовых значений
tokenizer = Tokenizer(num_words=maxWordsCount, filters='!"#$%&()*+,-––—./:;<=>?@[\\]^_`{|}~\t\n\xa0', lower=True, split=' ', oov_token='unknown', char_level=False)

vocs = []
for i in range(3):
  tokenizer = Tokenizer(num_words=maxWordsCount, filters='!"#$%&()*+,-––—./:;<=>?@[\\]^_`{|}~\t\n\xa0', lower=True, split=' ', oov_token='unknown', char_level=False)
  tokenizer.fit_on_texts(words[i]) #"Скармливаем" наши тексты, т.е даём в обработку методу, который соберет словарь частотности
  #Преобразовываем текст в последовательность индексов согласно частотному словарю
  xTrainIndexes = tokenizer.texts_to_sequences(words) #Обучающие тексты в индексы
  vocs.append(tokenizer.word_index)
  vocabularyItems = list(tokenizer.word_index.items()) #Список с cодержимым словаря
  vocabularySize = len(vocabularyItems)+1 #Размер словаря
  print( 'Фрагмент словаря : {}'.format(vocabularyItems[:50]))
  print( 'Размер словаря : {}'.format(vocabularySize))
  
topics = ['Computer  Science','Electrical  Engineering',  'Psychology',  'Mechanical  Engineering','Civil  Engineering',  'Medical  Science',  'biochemistry']