import json
from nltk_utils import tokenization,stem,bag_of_words
import numpy as np
with open('intents.json','r') as f:
    intents = json.load(f)

# print(intents)

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenization(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?','!',',','.']
all_words = [stem(word) for word in all_words if word not in ignore_words]

all_words = sorted(set(all_words)) # removing duplicate by using set function
tags = sorted(set(tags))

# making Training data
X_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

print(X_train)
print('/n')
print(y_train)