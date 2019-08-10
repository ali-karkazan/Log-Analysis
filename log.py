

import psycopg2
# 
DBNAME = "news"


def log_analysis():

	# connect to database news

	try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
	c = db.cursor()

	# Query for first question, refer README.md for VIEWS details,
	
	views = "select count(*) as num_viewed, slug from article_log group by slug order by num_viewed desc limit 3;"
	
	c.execute(views)
	views = c.fetchall()

	# Printing out the answer for first Question

	for n in views:
		print str(n[1])+" " + str(n[0])+ " views"

	db.close()
log_analysis()
