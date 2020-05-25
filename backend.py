import sqlite3

#Connecting to DB
def Connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS BOOK(BOOK_ID INTEGER PRIMARY KEY AUTOINCREMENT,Title VARCHAR,Author VARCHAR,Year INTEGER,ISBN INTEGER)")
    conn.commit()
    conn.close()



def Insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO BOOK(Title,Author,Year,ISBN) VALUES(?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def View():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute('Select * from book')
    rows=cur.fetchall()
    conn.close()
    return rows


def Search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("Select * from book where title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def Delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("Delete from book where BOOK_ID=?",(id,))
    conn.commit()
    conn.close()
    

def Update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET Title=?, Author=?, Year=?,ISBN=? where BOOK_ID=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

    
Connect()
