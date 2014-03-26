mapreduce
=========

**Repository of MapReduce scripts that I wrote in Python for the Udacity course [Intro to Hadoop and MapReduce](https://www.udacity.com/course/ud617).** Each mapper script has a complementary reducer script. Together, the mapper and the reducer receive data from the standard input. These scripts can be used locally or they can create MapReduce jobs in Hadoop with [Hadoop Streaming](http://hadoop.apache.org/docs/r1.2.1/streaming.html). As detailed below, these scripts process data from one of three sources: data of user posts on Udacity's forums [[link](http://content.udacity-data.com/course/hadoop/forum_data.tar.gz)], web log data [[link](http://content.udacity-data.com/courses/ud617/access_log.gz)], and sales data from different stores [[link](http://content.udacity-data.com/courses/ud617/purchases.txt.gz)].

To run a mapper and a reducer on 100 lines of data and view the output on a Linux machine, try a command like the one below.
```head -100 ./example_data.txt | ./example_mapper.py | sort | ./example_reducer.py | less```

- **average_length_mapper.py** and **average_length_reducer.py** count the length of every question on Udacity's forum and compute the average length of the answers to each question, outputting the result in three columns: *question ID*, *question length*, and *mean answer length*. Questions without answers receive an average answer length of 0.
