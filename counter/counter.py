# Python3 program for a word frequency
# counter after crawling a web-page
import requests
from bs4 import BeautifulSoup
from collections import Counter

'''Function defining the web-crawler/core 
spider, which will fetch information from 
a given website, and push the contents to 
the second function clean_wordlist()'''


def start(url):

    # empty list to store the contents of
    # the website fetched from our web-crawler
    wordlist = []
    source_code = requests.get(url).text

    # BeautifulSoup object which will
    # ping the requested url for data
    soup = BeautifulSoup(source_code, 'html.parser')

    # Text in given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.findAll('html'):
        content = each_text.text

        # use split() to break the sentence into
        # words and convert them into lowercase
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        word_list = clean_wordlist(wordlist)
        return word_list

# Function removes any unwanted symbols


def clean_wordlist(wordlist):

    filter_words = ['and', 'the', 'to', 'for', 'is', 'are', 'of' , 'a', 'an', 'at', 'on', 'in', 'i']

    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0 and word.lower() not in filter_words:
            clean_list.append(word)
    word_dict = create_dictionary(clean_list)
    return word_dict

# Creates a dictionary conatining each word's
# count and top_20 ocuuring words


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    c = Counter(word_count)

    # returns the most occurring elements
    top = c.most_common(10)
    return top
