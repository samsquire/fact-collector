import psycopg2

try:
    conn = psycopg2.connect("dbname='forum' user='forum' host='127.0.0.1' password='forum'")
except Exception as e:
    print("I am unable to connect to the database")
    print(e)

cur = conn.cursor()
cur.execute("""
drop table if exists fact_collections;
create table if not exists fact_collections (
    id SERIAL PRIMARY KEY,
    name TEXT
);
drop table if exists facts;
create table if not exists facts (
    id SERIAL PRIMARY KEY,
    fact TEXT,
    fact_collection TEXT,
    parsed JSON,
    timestamp timestamptz,
    class text
);

""")

fact_collections = ["main"]
for fact_collection in fact_collections:
    cur = conn.cursor()
    cur.execute("""
    insert into fact_collections (name) values('main');
    """)

beginner_facts = [
    "I ate a <fooditem> at <time> with <person>",
    "Addendum I eat <fooditem>",
    "Addendum I know <person>",
    "I drunk <drinkitem>",
    "Inference and(likes(sam, X), likes(X, sam)).",
    "Inference and(likes(sam, X), \+(likes(X, sam))).",
    "Logic likes(sam, john).",
    "Logic likes(sam, peter).",
    "Logic likes(john, sam)."
    ]

for fact in beginner_facts:
    cur = conn.cursor()
    cur.execute("""
    insert into facts (fact, parsed, class, fact_collection, timestamp) values (%s, %s, %s, %s, now());
    """, (fact, "{}", "", "main"))
conn.commit()


cur.close()
