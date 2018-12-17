#!/usr/bin/env python
# Tested on python 2.7
# PostGreSQL 9.5
# All on Ubuntu as prescribed on vagrant file, Contained on MacOSX
# For Udacity FSND - Project 1 - Log Analysis
# Thanks to Udacity instructors, staff,classmates on slack and study groups
# for all the help
# Thanks to w3c schools, oracle OTN documents, youtube videos,
# git hub pages of udacity, ddavignon,aviryan,poko
# Change log - V1.2(changes after first # REVIEW:1 )
# Change log - V1.2(changes after first # REVIEW:1.2-out code file exe verified)
import psycopg2
DBNAME = "news"
sql_Pop3Art = """
select
    title, count (*)
from
    valid_visitor_articles
group by
    (title)
order by count(path) desc
limit 3;
"""
sql_ArtAut = """
select
    authors.name, count(valid_visitor_articles.path) as views
from articles
inner join
    authors on articles.author = authors.id
inner join
    valid_visitor_articles on concat('/article/', articles.slug)
    = valid_visitor_articles.path
group by authors.name
order by count(valid_visitor_articles.path ) desc;
"""
sql_PgErr = """
select * from
(select t_req.day,
    round(cast((100*usreq.unserved_requests) as numeric) /
    cast(t_req.tot_requests as numeric), 2)
    as repErr from
  (select date(time) as day, count(*) as tot_requests from log
   group by day)
    as t_req
inner join
  (select date(time) as day, count(*) as unserved_requests from log where
    status like '4%' OR status like '5%' group by day )
    as usreq
on t_req.day = usreq.day)
as toter where repErr >1.0;
"""


class logAnalysisHandler:
        def __init__(self):
            try:
                self.db = psycopg2.connect('dbname=news')
                self.cursor = self.db.cursor()
            except Exception as expx:
                print('Connection Exception issue', expx)

        def query_db(self, squery):
            try:
                self.cursor.execute(squery)
                dbresult = self.cursor.fetchall()
                return dbresult
            except Exception as expx:
                print('Query Executional exception ', expx)

        def conClean(self):
            try:
                self.db.close()
            except Exception as expx:
                print('Connection resource clearing up exception', expx)

        def printRset(self, squery, qryty):
            squery = squery.replace('\n', ' ')
            result = self.query_db(squery)
            lenrs = len(result)
            if (result != 'null'):
                i = 1
                for row in result:
                    ansAdden = row[0]
                    addTy = type(ansAdden)
                    ansDeden = row[1]
                    print i, "-", ansAdden, " ---- ", ansDeden, qryty
                    i = i+1
            print ('------------------------------------------------------')


if __name__ == '__main__':
    AnalysisOb = logAnalysisHandler()
    print('Welcome to News Analysis, please check read me')
    print('Question 1 - What are the most popular three articles of all time?')
    qryty = 'views'
    AnalysisOb.printRset(sql_Pop3Art, qryty)
    print('Question 2 - Who are the most popular article authors of all time?')
    qryty = 'views'
    AnalysisOb.printRset(sql_ArtAut, qryty)
    print('Question 3 - On which days did more'
          'than 1% of requests lead to errors?')
    qryty = 'Error in %'
    AnalysisOb.printRset(sql_PgErr, qryty)
    AnalysisOb.conClean()
    print('Thank you for reviewing the work, have a good day')
