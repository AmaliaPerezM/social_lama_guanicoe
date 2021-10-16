from flask import Flask, request
from db import *
import uuid
import json

con = sql_connection()
create_user_table(con)

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>hello world</p>"


@app.route("/user", methods=["GET","POST"])
def user():
    if request.method == "GET":
        id = request.args["id"]
        con = sql_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE id=:uuid", {"uuid": id})
        row_headers=[x[0] for x in cur.description] 
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)

    if request.method == "POST":
        data = request.get_json()
        con = sql_connection()
        cur = con.cursor()
        id = str(uuid.uuid4())
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?)", (id, data["name"], data["email"], data["password"]))
        con.commit()
        return id

