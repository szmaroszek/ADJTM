from matplotlib import pyplot as plt
from nltk import collections
from prettytable import PrettyTable
from wordcloud import WordCloud
from dataOperations.getData import get_data, split_dataset
from dataOperations.cleanData import clean_data
from dataOperations.wordCloud import generate_cloud
from Classifiers.Models import train_model, prediction, accurcy, compare_predictions

# get sample data
data = get_data('data/alexa_reviews.csv', rows = 20000)

# prepare data
cleaned_data = clean_data(data)

# split dataset
dataset_split = split_dataset(cleaned_data['verified_reviews'], cleaned_data["rating"])

# # show word cloud
# generate_cloud(cleaned_data['verified_reviews'])


# train model
model = train_model(dataset_split['X_train'], dataset_split["Y_train"], "LinearSVC")
accurcy(model, dataset_split['X_test'], dataset_split["Y_test"])


reviews = ["That was an awesome place. Great food! Highly recommend",
           "It was good but lacking, maybe we will visit again",
           "Food was cold and awful, won't come back",
           "The worst restaurant I have ever been to!!",
           "Portions were alright, but we waited for a long time and there was a lot of people"]


compare_predictions(reviews, "LinearSVC", cleaned_data)