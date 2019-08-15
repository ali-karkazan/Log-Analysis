### Logs Analysis Project - Udacity Full Stack Nanodegree - One Million 	 Arab Coder

### About the logs analysis project:
The project demonstrates my skills in databases and SQL specifically PostgreSQL, and Python DB-API. The application runs three queries and displays the output in the command-line that answers below three questions

	1 - What are the most popular three articles of all time?
	2 - Who are the most popular article authors of all time?
	3 - On which days did more than 1% of requests lead to errors?

### Software required to run the program:
- [Python](https://www.python.org/)
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)

### Setting up the project:
	1 - install Vagrant and virtualBox
	2 - Download the [Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
	3 - download the database into Vagrant directory.
	4 - To load the database, `cd` into the `Vagrant` directory and use command
	```psql -d news -f newsdata.sql```.
### Views to be created:
    create view article_log as select log.path,articles.slug,articles.title
	from log join articles on log.path = '/article/' || articles.slug;

	create view author_name as select authorcount.author,authors.id,authors.id,authors.name from author_count join authors on author_count.author = authors.id;

	create view author_of_all_time as select count(*) as author_of_all_time, name from author_name group by name order by author_of_all_time desc;

	create view error_rate as 
	select error_requests.day, round((error_requests.errors * 1.0) / (total_requests.requests * 1.0) * 100, 2) as percentage
	from
	(select time::date as day, count(*) as requests from log group by day) as total_requests, 
	(select time::date as day, count(*) as errors from log where status = '404 NOT FOUND' group by day) as error_requests
	where
	total_requests.day = error_requests.day;

### How to run the program:
	from you terminal `cd` into vagrant folder and run below:
	```python log.py```

