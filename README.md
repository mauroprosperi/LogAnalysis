# LogAnalysis
A log analysis project for Udacity, this is a reporting tool that use information of a large database showing conclusions from the information, the data that we are looking for is: 

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
  
  
  5. Load the database:
  ~~~
  psql -d news -f newsdata.sql
  ~~~
  6. Connect to the database:
  ~~~
  psql -d news
  ~~~
  7. Run the python file from the command line when you have the python and the SQL file 
  ~~~
  python3 newsdb.py
  ~~~ 
  
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
