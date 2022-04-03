import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import pandas
from tqdm import tqdm
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = words.count(word)
    return word_count

def create_string(csv_file, i):
    return " ".join(rec[1] for rec in csv_file['title'][:i].iteritems())

df = pandas.read_csv('News _dataset/True.csv', usecols=['title', 'text'])


print(create_string(df,3))

cleared_string = clear_stopwords(stem_text(clear_text(create_string(df,3))))
print(cleared_string)
# bow = count_words(cleared_string)

# wc = WordCloud()
# wc.generate_from_frequencies(bow)
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.show()
