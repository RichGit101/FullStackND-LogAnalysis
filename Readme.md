Readme.md
Project version V1.2 All review 1 suggestions completed
Date: 16 Dec 2018

## Acknowledgments

* Thanks to Udacity instructors, staff,classmates on slack and study groups for all the help
* Thanks to w3c schools, oracle OTN documents, youtube videos, git hub pages of udacity, ddavignon,aviryan,poko and many more. Thank * You.

# Project Title
For Udacity Full Stack ND - Project Log Analysis

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
Vagrant
Ubuntu
python
PostGreSQL
Creating DB view as shown below
Executing python py file on command line


### Installing
First Follow Udacity Guide.

1) VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org
2) Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com.
3) VM configuration
you can use Github to fork and clone the [repository] https://github.com/udacity/fullstack-nanodegree-vm.

If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.

Please read vagrant configuration file. It explains configurations for ssh,
the way Linux and PostGreSQL is installed.

Navigate to vagrant subdirectory news. We will be working inside this subdirectory.

a-How to create DB
b-Where to get newsdata.sql with database schema and data
Location for [data pack]
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

c) -Comressed version included
d )-How to import the scheme and data into database
To load the data, cd into the vagrant directory and use the command
psql -d news -f newsdata.sql

e) How to create required view
psql
news=> create view valid_visitor_articles as
news-> select l.path, l.ip,l.status, a.slug, a.author,a.title from log l , articles a
news-> where l.status like '%200%' and l.path !='/'
news-> and concat('/article/',a.slug) = l.path ;

Result will be

CREATE VIEW
news=> \d valid_visitor_articles ;
View "public.valid_visitor_articles"
 Column |  Type   | Modifiers
--------+---------+-----------
 path   | text    |
 ip     | inet    |
 status | text    |
 slug   | text    |
 author | integer |
 title  | text    |

### Execution of script and verifying sample results

vagrant@vagrant:/vagrant/newsdata$ python newspaperdb.py
Welcome to News Analysis, please check read me
Question 1 - What are the most popular three articles of all time?
	1 . Candidate is jerk, alleges rival -- 338647 views
	2 . Bears love berries, alleges bear -- 253801 views
	3 . Bad things gone, say good people -- 170098 views

Question 2 - Who are the most popular article authors of all time?
	1 . Ursula La Multa -- 507594 views
	2 . Rudolf von Treppenwitz -- 423457 views
	3 . Anonymous Contributor -- 170098 views
	4 . Markoff Chaney -- 84557 views

Question 3 - On which days did more than 1% of requests lead to errors?
	1 . 2016-07-17 -- 2.26 views

Thank you for reviewing the work, have a good day
vagrant@vagrant:/vagrant/newsdata$


## Running the tests

Execute the script in test or qa environment, verify db before and after, verify file system and processes.

### Break down into end to end tests

Unit test for code basic execution
DB level query tests
Testing for exceptions handling

### And coding style tests
PEP guidelines and Udacity guidelines


## Deployment

Make sure you have pre-requisites from Udacity git hub page. Create View first. Copy script .py file to script execution folder and test.

## Built With

* [Python] V2.7
* [PGreSQL] V9.5
* [Ubuntu] V16
* [Vagrant]
* [Virtual Box]
* [MacOSX Host]

## Contributing

We will plan for improvements

## Versioning

Simple versioning mapping local git

## Authors

VA
Udacity FSND student 2018

## License

This project is Free as in free beer
