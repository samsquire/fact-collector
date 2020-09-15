import json
import time
from flask import Flask, request, make_response, Response, render_template
app = Flask(__name__)
import psycopg2

try:
    conn = psycopg2.connect("dbname='forum' user='forum' host='172.17.0.1' password='forum'")
except Exception as e:
    print("I am unable to connect to the database")
    print(e)

@app.route("/save/<collection>", methods=["POST"])
def save(collection):
    data = request.get_json()
    cur = conn.cursor()
    cur.execute("""
    insert into facts (fact, parsed, fact_collection) values (%s, %s, %s);
    """, (data["fact"], json.dumps(data["parsed"]), collection))
    conn.commit()
    return make_response('', 200)

@app.route("/facts/<collection>", methods=["GET"])
def get_collection(collection):
    cur = conn.cursor()
    cur.execute("""
    select id, name from fact_collections;
    """)
    fact_collections = cur.fetchall()
    valid_collections = {}
    for fact in fact_collections:
        valid_collections[fact[1]] = fact[0]
    if collection not in valid_collections:
        return make_response('[]', 404)
    cur = conn.cursor()
    cur.execute("""
    select id, fact, parsed from facts where fact_collection = %s;
    """, (collection,))
    facts = cur.fetchall()
    transformed = []
    for fact in facts:
        transformed.append({
            "id": fact[0],
            "name": fact[1],
            "parsed": fact[2]
        })
    return json.dumps(transformed)



@app.route("/")
def render():
    return render_template("index.html")
