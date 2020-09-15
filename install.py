import psycopg2

try:
    conn = psycopg2.connect("dbname='forum' user='forum' host='172.17.0.1' password='forum'")
except Exception as e:
    print("I am unable to connect to the database")
    print(e)

cur = conn.cursor()
cur.execute("""

create table if not exists fact_collections (
    id SERIAL PRIMARY KEY,
    name TEXT
);

create table if not exists facts (
    id SERIAL PRIMARY KEY,
    fact TEXT,
    fact_collection TEXT,
    parsed JSON
);

""")


cur.close()
conn.commit()
