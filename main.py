import string
from collections import Counter
import matplotlib.pyplot as plt

text = open('myText.txt', encoding="utf-8").read()  # opening the text file and reading text from it.
lowercase = text.lower()  # converting the text into lowercase.

cleaned_text = lowercase.translate(
    str.maketrans('', '', string.punctuation))  # cleaning the text -> removing all the punctuations.
# print(string.punctuation)

# Tokenization
tokenized_words = cleaned_text.split()

# Stop words

# print(tokenized_words)
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
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
