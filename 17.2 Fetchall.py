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

tabularFormatData = f'{description[0][0]}   {description[1][0]}  {description[2][0]}  {description[3][0]}\n'  
for value in data:
    tabularFormatData += f'{value}\n'
print(tabularFormatData)
    
