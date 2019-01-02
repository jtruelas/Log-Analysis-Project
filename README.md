# Log Analysis Project

## Description
This program accesses a database from a news station.

With the data located in the database the program answers the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The output will appear on the terminal window with the answers in order the questions are listed.

## Quick Startup
To run this program on your machine, _FORK_ [this](https://github.com/jtruelas/Log-Analysis-Project.git) virtual machine and clone it to a local directory.
```
user ~ $ mkdir new_directory
user ~ $ git clone repo_url new_directory
user ~ $ cd new_directory
```
To log in to the vm, run the following:
```
user new_directory $ vagrant up && vagrant ssh
```
Download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip the file. Place the file `newsdata.sql` in the `vagrant` directory shared with the vm.

Once you are in:
```
vagrant@vagrant:~$ cd /vagrant
vagrant@vagrant:/vagrant$ psql -d news -f newsdata.sql
```
Then create the [views](https://github.com/jtruelas/Log-Analysis-Project#created-views) listed below before going on to run the program.

When you are finished, run the program:
```
news=> \q
vagrant@vagrant:/vagrant$ python news.py
```
## Created Views:
_tophits:_
```
create view tophits as
select path, count(*) as hits from log
where status = '200 OK'
and path like '/a%'
group by path
order by hits desc
limit 10;
```
_titles:_
```
create view titles as
select title, concat('/article', articles.slug) as slug from articles;
```
_authorhits:_
```
create view authorhits as
select authors.id, authors.name, titles.slug, tophits.hits
from titles, tophits, authors, articles
where authors.id = articles.author
and titles.title = articles.title
and titles.slug = tophits.path
order by hits desc;
```
*e_status:*
```
create view e_status as 
select date(time), count(status) as error from log
where status != '200 OK'
group by date
order by date;
```
*t_status:*
```
news=> create view t_status as
select date(time), count(status) as status from log
group by date
order by date;
```
*avg_error:*
```
create view avg_error as
select e_status.date, round(100.0 * e_status.error/t_status.status, 2) as percent from e_status, t_status
where e_status.date = t_status.date;
```
