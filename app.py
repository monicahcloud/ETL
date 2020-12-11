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
    author_resultset = engine.execute(
        'select author, dob, description from authors')
    result['count'] = author_resultset.rowcount

    for author_row in author_resultset:
        this_author = {}
        this_author['author'] = author_row.author
        this_author['description'] = author_row.description
        this_author['dob'] = author_row.dob
     
        authors.append(this_author)

    result['details'] = authors

    return jsonify(result)

@app.route("/quotes")
def quotes():

    result = {}
    result_set = engine.execute('''select t.author, quote, tags
    from quotes q inner join tags t on q.id = t.id
    order by t.id''')

    result['total'] = result_set.rowcount

    quotes = []
    for row in result_set:
        quote = {}
        quote['quotes'] = row.quote
        quote['author'] = row.author
        quote['tags'] = row.tags
        quotes.append(quote)

    result['quotes'] = quotes
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
