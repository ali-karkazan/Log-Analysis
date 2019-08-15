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

    # Question 1- top 3 articles (plz refer to the views in README.md file)
    views = """select count(*) as num_viewed, title from article_log
            group by title order by num_viewed desc limit 3;"""
    c.execute(views)
    views = c.fetchall()

    print("\nThe most popular articles of all time:\n")
    for n in views:
        print(' ' + str(n[1]) + " " + str(n[0]) + " views\n")

    # Question 2- the author of all time
    author_of_all_time = """select count(*) as author_of_all_time,
                        name from author_name
                        group by name order by author_of_all_time desc;"""
    c.execute(author_of_all_time)
    author_of_all_time = c.fetchall()

    print('\n The most popular authors of all time:\n')
    for i in author_of_all_time:
        print(' ' + str(i[1]) + " " + str(i[0]) + " views\n")

    # Question 3 - The day more than 1% of requests lead to errors
    error_count = """ select day,percentage from error_rate
    where percentage > 1.0 order by day;"""

    c.execute(error_count)
    error_count = c.fetchall()

    print('\n The day more than 1% of requests lead to errors: \n')
    for e in error_count:
        print(' ' + str(e[0]) + " " + str(e[1]) + "%" + "\n")

    db.close()

log_analysis()
