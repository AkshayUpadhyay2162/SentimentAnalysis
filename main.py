import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

text = open('myText.txt', encoding="utf-8").read()  # opening the text file and reading text from it.
lowercase = text.lower()  # converting the text into lowercase.

cleaned_text = lowercase.translate(
    str.maketrans('', '', string.punctuation))  # cleaning the text -> removing all the punctuations.
# print(string.punctuation)

# Tokenization
tokenized_words = word_tokenize(cleaned_text, "english")
# print(tokenized_words)


# Stop words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words("english"):
        final_words.append(word)

# print(final_words)

emotion_list = []
with open('emotions.txt', 'r') as file_emotions:
    for line in file_emotions:
        cleaned_line = line.replace("\n", "").replace(",", "").replace("'", "").strip()
        # print(cleaned_line)
        word, emotion = cleaned_line.split(": ")
        # print("Word:", word, ",", "Emotion:", emotion)

        if word in final_words:
            emotion_list.append(emotion)

# print(emotion_list)
count_emotion = Counter(emotion_list)

# print(count_emotion)
fig, ax1 = plt.subplots()
ax1.bar(count_emotion.keys(), count_emotion.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()
