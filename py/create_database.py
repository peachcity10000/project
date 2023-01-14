import sqlite3
import os

from click import command

def create_sql():
    with open('./sql/create_db.sql',newline='') as f:
        create_db_sql = f.read()

    db = sqlite3.connect('peachCity.db')
    with db:
        try:
            db.executescript(create_db_sql)
        except:
            a= 0

def test_sql():
    db = sqlite3.connect('peachCity.db')
    c = db.cursor()

    # test commit the tables
    with open('./sql/test_db_commit.sql',newline='' ,encoding='utf-8') as f:
        test_db_sql = f.read()
        c.executescript(test_db_sql)
        db.commit()
    
    # Test selecting the "account" table
    c.execute("SELECT * FROM account;")
    db.commit()
    for row in c:
        print(row)

    # Test selecting the "post" table
    c.execute("SELECT * FROM post;")
    db.commit()
    for row in c:
        print(row)

    # Test selecting the "store" table
    c.execute("SELECT * FROM store ;")
    db.commit()
    for row in c:
        print(row)
    
    # Test selecting the "img" table
    c.execute("SELECT * FROM img ;")
    db.commit()
    for row in c:
        print(row)

    # Test selecting the "postcast" table
    c.execute("SELECT * FROM postcast where store_id = 1;")
    db.commit()
    for row in c:
        print(row)
    

    
def delete_sql():
    db = sqlite3.connect('peachCity.db')
    c = db.cursor()
    with open('./sql/delete_db.sql',newline='' ,encoding='utf-8') as f:
        test_db_sql = f.read()
        c.executescript(test_db_sql)
        db.commit()
    db.close()
    try:
        os.remove('./peachCity.db')
    except OSError as e:
        print(e)
    else:
        print("File is deleted successfully")



# create_sql()
test_sql()
# delete_sql()
# create_sql()
print("test successfully")
