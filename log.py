

import psycopg2

DBNAME = "news"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()
query = "select count(*) as num_viewed, slug from article_log group by slug order by num_viewed desc limit 3;"
c.execute(query)
views = c.fetchall()
for n in views:
	print str(n[1])+" " + str(n[0])+ " views"

db.close()
