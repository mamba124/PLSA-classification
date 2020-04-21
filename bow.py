
import nltk
nltk.download('punkt')
from sklearn.feature_extraction.text import CountVectorizer
  
#################
#Преобразовываем текстовые данные в числовые/векторные для обучения нейросетью
#################
vocs=[]
for t in texts:
    count_vectorizer = CountVectorizer(
            analyzer="word", tokenizer=nltk.word_tokenize,
            preprocessor=None, max_features=None)    

    count_vectorizer.fit_transform(t.split())

    bag_of_words = count_vectorizer.vocabulary_
    vocs.append(bag_of_words)

count_vectorizer = CountVectorizer(
    analyzer="word", tokenizer=nltk.word_tokenize,
    preprocessor=None, max_features=None)    

count_vectorizer.fit_transform(texts)

bag_of_words = count_vectorizer.vocabulary_

