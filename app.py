import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, text

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

connection_string = "postgres://mpiljlhpdduyfa:2332f5bec0021e7c8a94d4f2450748ccf8aeaf1a965c62cc3d3885a838a5e316@ec2-52-22-238-188.compute-1.amazonaws.com:5432/d29t1m9qk328vp"
engine = create_engine(f'{connection_string}')

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/quotes<br/>"
        f"/authors<br/>"
    )

@app.route("/authors")
def authors():
    result = {}
    authors = []
    author_resuletset = engine.execute(
        'select name , born , description from author')
    result['count'] = author_resuletset.rowcount

    for author_row in author_resuletset:
        this_author = {}
        quotes = []
        this_author['name'] = author_row.name
        this_author['description'] = author_row.description
        this_author['born'] = author_row.born
        quotes = quotes_for_author(author_row.name)
        this_author['count'] = len(quotes)
        this_author['quotes'] = quotes
        authors.append(this_author)

    result['details'] = authors

    return jsonify(result)

@app.route("/quotes")
def quotes():

    result = {}
    result_set = engine.execute('''select id, author_name, text
    from quotes q inner join author a on q.author_name = a.name
    order by id''')

    result['total'] = result_set.rowcount

    quotes = []
    for row in result_set:
        quote = {}
        quote['text'] = row.text
        quote['author'] = row.author_name
        tags = tags_for_the_quote(row.id)
        quote['tags'] = tags
        quotes.append(quote)

    result['quotes'] = quotes
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
