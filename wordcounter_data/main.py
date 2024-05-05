# Importing requests, BeautifulSoup, nltk, and Counter
import requests
from bs4 import BeautifulSoup
import nltk
from collections import Counter

# Getting the Moby Dick HTML 
r = requests.get('https://www.gutenberg.org/files/2701/2701-h/2701-h.htm')


# Setting the correct text encoding of the HTML page
r.encoding = 'utf-8'

# Extracting the HTML from the request object
html = r.text

# Printing the first 2000 characters in html
print(html[0:2000])

# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, 'html.parser')

# Getting the text out of the soup
text = soup.get_text()

# Printing out text between characters 32000 and 34000
print(text[32000:34000])

# Creating a tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer('\w+')

# Tokenizing the text
tokens = tokenizer.tokenize(text)

# Printing out the first 8 words / tokens 
tokens[:20]

# Create a list called words containing all tokens transformed to lower-case
words = [token.lower() for token in tokens]

# Printing out the first 8 words / tokens 
words[:5]

# Getting the English stop words from nltk
from nltk.corpus import stopwords

sw = stopwords.words('english')
# Printing out the first eight stop words

sw[:8]

# Create a list words_ns containing all words that are in words but not in sw
words_ns = [word for word in words if word not in sw]

# Printing the first 5 words_ns to check that stop words are gone
words_ns[:5]

# Initialize a Counter object from our processed list of words
count = Counter(words_ns)

# Store 10 most common words and their counts as top_ten
top_ten = count.most_common(10)

# Print the top ten words and their counts
print(top_ten)

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

top_words = count.most_common(20)
top_20 = []
i = 0
while i < len(top_words):
  top_20.append(top_words[i][0])
  i += 1
    
#convert list to string and generate
unique_string=(" ").join(top_20)
wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()