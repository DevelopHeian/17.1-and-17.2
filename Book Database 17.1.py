#17.1
#(Books Database) In an IPython session, perform each of the following tasks on the
#books database from Section 17.2:
#a) Select all authors’ last names from the authors table in descending order.
#b) Select all book titles from the titles table in ascending order.
#c) Use an INNER JOIN to select all the books for a specific author. Include the title,
#copyright year and ISBN. Order the information alphabetically by title.
#d) Insert a new author into the authors table.
#e) Insert a new title for an author. Remember that the book must have an entry in the author_ISBN table and an entry in the titles table.


import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')
#pd.options.display.max_columns = 10
#pd.read_sql('SELECT last FROM authors', connection)
cursor = connection.cursor()
cursor.execute('SELECT last FROM authors ORDER BY last DESC')
data = cursor.fetchall()
print(data)
print('\n')

cursor.execute('SELECT title FROM titles ORDER BY title ASC')
data = cursor.fetchall()
print(data)
print('\n')

cursor.execute('SELECT title,copyright,isbn FROM titles INNER JOIN authors ON authors.id = 1 ORDER BY title')
data = cursor.fetchall()
print(data)
print('\n')

cursor.execute("INSERT INTO authors(first,last) VALUES('Heian' , 'Alrousan')")
cursor.execute('SELECT * FROM authors ORDER BY last DESC')
data = cursor.fetchall()
print(data)
print('\n')

cursor.execute("INSERT INTO titles(isbn,title,edition,copyright) VALUES('0111111','Python For Heian', 1, '2022')")
cursor.execute("INSERT INTO author_ISBN(id,isbn) VALUES(6,'0111111')")
cursor.execute('SELECT title FROM titles ORDER BY title ASC')
data = cursor.fetchall()
print(data)
print('\n')



