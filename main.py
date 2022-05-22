from dataOperations.getData import get_data, split_dataset
from dataOperations.cleanData import clean_data
from dataOperations.wordCloud import generate_cloud
from Classifiers.Models import train_model, accurcy, compare_predictions

# get sample data
data = get_data('data/alexa_reviews.csv', rows = 200000)

# prepare data
cleaned_data = clean_data(data)

# split dataset
dataset_split = split_dataset(cleaned_data['verified_reviews'], cleaned_data["rating"])

# train model
model = train_model(dataset_split['X_train'], dataset_split["Y_train"], "LinearSVC")
accurcy(model, dataset_split['X_test'], dataset_split["Y_test"])


reviews = ["I love it! Highly recommend.",
           "I dislike the product. It keeps breaking all the time.",
           "I would deffinitely buy it again",
           "The worst product I have ever bought",]


compare_predictions(model, reviews, "LinearSVC", cleaned_data)


# show word cloud
generate_cloud(cleaned_data['verified_reviews'])