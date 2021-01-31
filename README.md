# ETL
ETL Mini-Project

Final-WebScrapping.ipynb: Jupyter notebook contains the code for the following tasks:

     - Webscrapping for : 'http://quotes.toscrape.com/'

     - Imported Splinter, pymongo, pandas, requests

     - utilized BeautifulSoup, sqlalchemy

     - created functions for data scraping for:
 
             - quote text,tags,Author Name, Author Details (born, description)        
     - Send data to MongoDB 

     - Move data from MongoDB to Postgres

         - created 3 Tables : Author info, Tags, Quotes
         
app.py : Created FLASK API for the following endpoints.

In the app.py:

        NAVIGATE TO THESE ENDPOINTS:

        **"/authors"**

        **"/quotes"**


Imported flask, sqlalchemy, pandas

Connected engine to the SQL DB AWS server

Created multiple routes for endpoint testing.
        
        - Welcome Page
        
        - Quotes

        - Authors

        -Tags

        -Top 10 Tags


