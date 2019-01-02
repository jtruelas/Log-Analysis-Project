# Tool that accesses the database titled news
# and extracts data to answer the following questions:
#
# 1. What are the most popular three articles of all time?
# 2. Who are the most popular article authors of all time?
# 3. On which days did more than 1% of requests lead to errors?

import psycopg2

DBNAME = "news"


def topArticles():

    """Returns the top three articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select titles.title, tophits.hits\
        from tophits, titles\
        where tophits.path = titles.slug\
        order by hits desc limit 3;")
    results = c.fetchall()
    c.close()
    return results


def topAuthors():

    """Returns the top authors of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name, sum(hits) as hits\
        from authorhits group by name\
        order by hits desc;")
    results = c.fetchall()
    c.close()
    return results


def errDays():

    """Returns the days where more than 1% of requests resulted in an error"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select date, percent from avg_error\
        where percent > 1.00;")
    results = c.fetchall()
    c.close()
    return results
