from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
example_text = """This is a sample sentence,
                  showing off the stop words filtration."""
 
stop_words = set(stopwords.words('english'))
 
word_tokens = word_tokenize(example_text)
  
filtered_sentence = ''
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence += ' ' + w

print(filtered_sentence)