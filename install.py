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
drop table facts;
create table if not exists facts (
    id SERIAL PRIMARY KEY,
    fact TEXT,
    fact_collection TEXT,
    parsed JSON,
    timestamp timestamptz,
    class text
);

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
