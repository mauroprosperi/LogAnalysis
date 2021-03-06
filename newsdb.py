#!/usr/bin/env python3
import psycopg2
dbname = "news"


def connect(dbname="news"):
    try:
        """Connect to the PostgreSQL."""
        database = psycopg2.connect("dbname={}".format(dbname))
        c = database.cursor()
        return database, c
    except:
        print("There was an error unexpected on the database, try again later")


def topArticles():
    """Prints the tops articles"""
    database, c = connect()
    query = """
    select title, views
    from articles
    inner join
    (select path, count(path) as views
    from log
    group by log.path) as log
    on log.path = '/article/' || articles.slug
    order by views DESC
    limit 3;
    """
    c.execute(query)
    result = c.fetchall()
    database.close()
    print ("\nTop Articles:\n")
    for i in range(0, len(result), 1):
        print ("\"" + result[i][0] + " - " + str(result[i][1]) + " views")


def popularAuthors():
    """Prints most popular authors"""
    database, c = connect()
    query = """
    select name, sum(log.views) as views
    from authors ,articles inner join
    (select path, count(path)
    as views
    from log
    group by log.path) as log
    on log.path = '/article/' || articles.slug
    where articles.author = authors.id
    group by authors.name
    order by views desc
    """
    c.execute(query)
    result = c.fetchall()
    database.close()
    print ("\nPopular Authors:\n")
    for i in range(0, len(result), 1):
        print ("\"" + result[i][0] + "\" - " + str(result[i][1]) + " views")


def geterror():
    """Creates a view to show the error faster"""
    database, c = connect()
    query = """
    create view geterror as select date(time) as day,
    count(status) as total,
    sum(case when status != '200 OK' then 1 else 0 end) as errors
    from log
    group by day
    order by errors desc
    """
    c.execute(query)
    database.commit()
    database.close()


def percentualError():
    """Prints the specific day with more bugs found"""
    database, c = connect()
    query = """
    select day, percent
    from (select day,errors,(errors::float*100)/Total::float
    as percent from geterror)
    as percent
    where percent >= 1
    """
    c.execute(query)
    result = c.fetchall()
    database.close()
    print ("\nTop day of the month with most errors:\n")
    for i in range(0, len(result), 2):
        print ("\"" + str(result[i][0]) + "\" - " +
               str(round(result[i][1], 2)) + "% errors\n")


if __name__ == "__main__":
    """
    You must uncomment this function below
    to have the view created for percentualError:
    """
    '''geterror()'''
    topArticles()
    popularAuthors()
    percentualError()
