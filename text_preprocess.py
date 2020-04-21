# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 08:23:46 2020

@author: Professional
"""

###########################
# Чтение файла в текст
##########################
def readText(fileName):
  f = open(fileName, 'r')
  text = f.read()
  texts = text.split('\n')
  
  return texts


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

texts = []
doc1 = [text for text in readText('doc1.txt')]
doc2 = [text for text in readText('doc2.txt')]
doc3 = [text for text in readText('doc3.txt')]

docs = [doc1,doc2,doc3]

for doc in docs:
    for text in doc:
        if len(text)>2:
            texts.append(text)