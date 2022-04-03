import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas
import numpy as np


def text_tokenizer(text):
    text = clear_text(text)
    text = stem_text(text)
    text = clear_stopwords(text)
    text = clear_short_words(text)
    return text.split()

def clear_text(text):
    text = re.sub(r'[.,]', '', text)
    text = re.sub(r'[:;][^\s]{1,2}', '', text)
    text = re.sub(r'\d', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[.,]', '', text)
    text = " ".join(text.split())
    return text

def clear_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = ''
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence += ' ' + w
    return filtered_sentence
    
def stem_text(text: str) -> str:
    porter = PorterStemmer()
    return " ".join(porter.stem(word) for word in text.split())

def clear_short_words(text):
    return " ".join(word for word in text.split() if len(word)>=3)


df = pandas.read_csv('News_dataset/True.csv', usecols=['title', 'text'])    

# 1
vectorizer = CountVectorizer(tokenizer=text_tokenizer)
X_transform = vectorizer.fit_transform(df['title'][:1])
print(X_transform.toarray())
print('----------------------------')

# 2
vectorizer = CountVectorizer(tokenizer=text_tokenizer)
X_transform = vectorizer.fit_transform(df['title'])
x_transformed_arr = np.sum(X_transform.toarray(), 0)
top_10 = []
for i in range(10):
    arr_index = (np.argmax(x_transformed_arr, 0))
    top_10.append(arr_index)
    x_transformed_arr[arr_index] = 0
    i += 1

names_out = vectorizer.get_feature_names_out()

for top in top_10:
    print(names_out[top])

# 3
vectorizer = TfidfVectorizer(tokenizer=text_tokenizer)
X_transform = vectorizer.fit_transform(df['title'])
x_transformed_arr = np.sum(X_transform.toarray(), 0)
top_10 = []
for i in range(10):
    arr_index = (np.argmax(x_transformed_arr, 0))
    top_10.append(arr_index)
    x_transformed_arr[arr_index] = 0
    i += 1

names_out = vectorizer.get_feature_names_out()

for top in top_10:
    print(names_out[top])

# 4
vectorizer = CountVectorizer(tokenizer=text_tokenizer)
X_transform = vectorizer.fit_transform(df['title'])
x_transformed_arr = np.sum(X_transform.toarray(), 1)
top_10 = []
for i in range(10):
    arr_index = (np.argmax(x_transformed_arr, 0))
    top_10.append(arr_index)
    x_transformed_arr[arr_index] = 0
    i += 1

for top in top_10:
    print(df['title'][top])
