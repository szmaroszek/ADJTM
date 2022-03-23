import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import pandas
from tqdm import tqdm
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def clear_text(text):
    re.sub(r'[.,]', '', text)
    re.sub(r'[:;][^\s]{1,2}', '', text), re.findall(r'[:;][^\s]{1,2}', text)
    re.sub(r'\d', '', text)
    re.sub(r'<.*?>', '', text)
    re.sub(r'[.,]', '', text)
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
    
def stem_text(text):
    porter = PorterStemmer()
    return [porter.stem(word) for word in text.split()]

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = words.count(word)
    return word_count

df = pandas.read_csv('News _dataset/Fake.csv')

string = ""
for i in tqdm(range(len(df['title']))):
    string += df['text'].iloc[i] + " "


cleared_string = stem_text(clear_stopwords(clear_text(string)))
bow = count_words(cleared_string)

wc = WordCloud()
wc.generate_from_frequencies(bow)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
