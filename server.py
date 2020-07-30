import os
from flask import Flask, request, render_template
import random
import markovify
import names
from bs4 import BeautifulSoup
import requests

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')
  
@app.route('/title', methods=['GET'])
def title():
    """Talk title from Markov chain
    """
    with open('ted_titles.txt', 'r') as f:
      chain = markovify.Text(f.read())
    return chain.make_sentence(tries=100)

@app.route('/author', methods=['GET'])
def author():
    """Random Speaker Name
    """

    return (random.choice(['Sir ', '', 'Lady ', 'Dr. ', 'Prof. '])
            + names.get_full_name()
            + random.choice([', PhD', '', ', MD']))

@app.route('/topic', methods=['GET'])
def topic():
    """Random topic tag
    """
    with open('ted_tags.txt', 'r') as f:
        tags = f.read().split('\n')
    return random.choice(tags)

@app.route('/easter', methods=['GET'])
def easter_egg():
    """Easter egg
    """
    return "Hi! You're great! <3"

@app.route('/karaoke', methods=['GET'])
def karaoke():
  return render_template('karaoke.html')

@app.route('/slides_url', methods=['GET'])
def findslides():
  with open('ted_tags.txt', 'r') as f:
    tags = f.read().split('\n')
  searchterm =  random.choice(tags)
  baseurl = 'https://search.lycos.com/web/?q=filetype%3Appt+'
  soup = BeautifulSoup(requests.get(baseurl+searchterm).content, "html.parser")
  ppts = []
  for a_tag in soup.findAll("a"):
      href = a_tag.attrs.get("href")
      if '.ppt' in str(href):
        ppts.append(href)
  url = random.choice(ppts)
  if url[:7] == 'http://':
    url = 'https://' + url[7:]
  return url

if __name__ == '__main__':
    app.run()