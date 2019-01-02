#!/user/bin/env python3
#
# Uses a reporting tool for a news station
# that answers the following questions:
# 1. What are the most popular three articles of all time?
# 2. Who are the most popular article authors of all time?
# 3. On which days did more than 1% of requests lead to errors?

from report_tool import topArticles, topAuthors, errDays

topArticles = topArticles()
print
print "Top 3 Articles:"
for row in topArticles:
    print "  ", row[0], "-", row[1], "views"

topAuthors = topAuthors()
print
print "Top Authors:"
for row in topAuthors:
    print " ", row[0], "-", row[1], "views"

errDays = errDays()
print
print "Erroneous Days:"
for row in errDays:
    timestamp = row[0]
    date = timestamp.strftime("%B %d, %Y")
    print " ", date, "-", row[1], "% errors"
