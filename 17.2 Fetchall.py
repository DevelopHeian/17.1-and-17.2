







#17.1
#(Books Database) In an IPython session, perform each of the following tasks on the
#books database from Section 17.2:
#a) Select all authors’ last names from the authors table in descending order.
#b) Select all book titles from the titles table in ascending order.
#c) Use an INNER JOIN to select all the books for a specific author. Include the title,
#copyright year and ISBN. Order the information alphabetically by title.
#d) Insert a new author into the authors table.
#e) Insert a new title for an author. Remember that the book must have an entry
#in the author_ISBN table and an entry in the titles table.










#17.2
#Cursor Method fetchall and Attribute description - When you use a sqlite3
#Cursor’s execute method to perform a query, the query’s results are stored in the Cursor
#object. The Cursor attribute description contains metadata about the results stored as a
#tuple of tuples. Each nested tuple’s first value is a column name in the query results. Cursor
#method fetchall returns the query result’s data as a list of tuples. Investigate the description attribute and fetchall method. Open the books database and use Cursor
#method execute to select all the data in the titles table, then use description and
#fetchall to display the data in tabular format


import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM authors', connection,index_col=['id'])

cursor = connection.cursor()
cursor.execute("SELECT * FROM titles")
description = cursor.description
data = cursor.fetchall()

tabularFormatData = ''
for value in data:
    tabularFormatData += f'{value}\n'
print(tabularFormatData)
    
