from nltk.stem import PorterStemmer

sentence="Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."

def stem_str(text: str):
    porter = PorterStemmer()
    return [porter.stem(word) for word in text.split()]

print(stem_str(sentence))