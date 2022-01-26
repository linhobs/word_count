from curses import start_color
from urllib import request
from bs4 import BeautifulSoup
import lxml 
import time

def count_words(url):
    # simulate a delay
    time.sleep(2)

    print(f"counting words at {url}")
    start = time.time()
    r = request.urlopen(url)
    soup = BeautifulSoup(r.read().decode(),'lxml')
    paragraphs = " ".join([p.text for p in soup.find_all("p")])
    word_count = dict()
    for i in paragraphs.split():
        if not i in word_count:
            word_count[i] = 1
        else:
            word_count[i] +=1
    end_time = time.time()
    
    time_elapsed = end_time - start
    print(word_count)
    print(f"Total Words: {len(word_count)}")
    print(f"Time  Elapsed: {time_elapsed}")
    return word_count
