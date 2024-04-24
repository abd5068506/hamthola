import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
text = open('paragraphs.txt','r').read()
words = text.split()
filtered_words = [word for word in words if word.lower() not in stop_words]

word_freq = {}
for word in filtered_words:
    word_freq[word] = word_freq.get(word, 0) + 1
for word, freq in word_freq.items():
        print(f"{word}: {freq}")


