import psycopg2

DBNAME = "news"


def log_analysis():

    # connect to the database
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
    c = db.cursor()
    views = """select count(*) as num_viewed, title from article_log
            group by title order by num_viewed desc limit 3;"""
    c.execute(views)
    views = c.fetchall()
    for n in views:
        print str(n[1]) + " " + str(n[0]) + " views"
    db.close()

log_analysis()
