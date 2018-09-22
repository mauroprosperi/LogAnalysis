# LogAnalysis
A log analysis project for Udacity, this is a reporting tool that uses information of a large database(that contain information about articles, their authors and the view of their articles) showing conclusions from the information, the data that we are looking for is:

1) What are the most popular three articles of all time 
2) Who are the most popular article authors of all time? 
3) On which days did more than 1% of requests lead to errors?
## PreRequisites
- Python3
- Vagrant
- VirtualBox
- PostgreSQL

## Instruccion

  1. Install [Vagrant][1] and [VirtualBox][2]
  
  [1]:https://www.vagrantup.com/
  [2]:https://www.virtualbox.org/wiki/Downloads
  
  2. Clone the repository to your local machine:
  ~~~
  git clone https://github.com/mauroprosperi/LogAnalisys
  ~~~
  
  3. Download the SQL file from [here][3]
  
  [3]:https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
  
  4. Start the virtual machine:
  
  
   First Use ***vagrant up*** to download the Linux operating system and install it:
   ~~~
   $ vagrant up
   ~~~
   Then, use ***vagrant ssh*** to log in your new installed VM, this insclude the PostgreSQL needed:
   ~~~
   $ vagrant ssh
   ~~~
  5. Create the view: You can do this on two ways; 
  
      * Uncomment the line 67 from python file that will trigger a function when executing the python file
    
      * Creating the view by your own, go to [accesing to the database][4]
    
  [4]:https://github.com/mauroprosperi/LogAnalysis#loganalysis
  
  6. Run the python file from the command line when you have the python and the SQL file 
  
  ~~~
  python3 newsdb.py
  ~~~ 
  
## Accesing to the database:

  1. Load the database:
  ~~~
  psql -d news -f newsdata.sql
  ~~~
  
  2. Connect to the database:
  ~~~
  psql -d news
  ~~~
  
  3. Create the followin view(copy this into your line command):
  ~~~
  create view geterror as select date(time) as day,
  count(status) as total,
  sum(case when status != '200 OK' then 1 else 0 end) as errors
  from log
  group by day
  order by errors desc;
  ~~~ 
  
  4. Exit from the database and go back to vagrant: 
  ~~~
    \q
  ~~~
  or
  ~~~
    ctrl + Z
  ~~~
  
  5. Go and initialize the python file as showed in [instruccion][5] - part 6
  
  [5]:https://github.com/mauroprosperi/LogAnalysis#instruccion
  
## About

The database have three tables:
- The authors table
- The article table
- The log

You can inspect in the command line of vagrant with the follow commands:
~~~
\dt             <--- Shows the tables

\d tablename    <--- shows the content of that table

\h              <--- Helps for SQL commands

\q              <--- Quits psql
~~~

## Example
![Example](https://i.imgur.com/pAuvbAv.png)
