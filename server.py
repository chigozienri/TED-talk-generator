import os
from flask import Flask, request, render_template
import random
import markovify
import names

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
    return chain.make_sentence()

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

if __name__ == '__main__':
    app.run()