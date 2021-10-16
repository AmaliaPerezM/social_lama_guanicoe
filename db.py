import sqlite3

def sql_connection():
    try:
        con = sqlite3.connect("social_lama_guanicoe.db")
        return con
    except Error:
        raise Error

def create_user_table(con):
    cur = con.cursor()
    if(not table_exists("users", con)):
        cur.execute("CREATE TABLE users(id string PRIMARY KEY, user_name text, email text, password text)")
    con.commit()

def table_exists(tableName, con):
    cur = con.cursor()
    cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=:name ''', {"name":tableName})
    if cur.fetchone()[0]==1:
        return True
    else:
        return False