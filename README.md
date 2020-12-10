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

We have multiple endpoint routes but not all of them were required for the assigment so the route were not completed(broken). 
Test_ground: Contains incomplete/old Codes for the assigments.

 We have multiple copies of some of the code since, we didn't want to overwrite any team members code in testing process. 
pseudocode.txt: Brainstorm text file where we planned and organized our approach to tackle this project. Also wrote some code to build out our Final work. Written process of how to mediate work in this large group.

Pg_SQL_quthors.sql: Postgres SQL DB  
