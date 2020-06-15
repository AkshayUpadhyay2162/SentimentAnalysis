import string
from collections import Counter
import matplotlib.pyplot as plt
import GetOldTweets3 as got


def get_tweets():
    hashtag = input("Enter twitter Hashtag: ")
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(hashtag) \
        .setSince("2019-01-01") \
        .setUntil("2020-05-30") \
        .setMaxTweets(500)

    # List of object gets stored in tweets variable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # Iterating through tweets list, storing them temporarily in tweet variable.
    # Get text and store it as a list inside text_tweets variable.
    tweets_list = [[tweet.text] for tweet in tweets]
    return tweets_list


text = ""
text_tweets = get_tweets()

for i in range(0, len(text_tweets)):
    text = text_tweets[i][0] + " " + text
    # print(text)

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
