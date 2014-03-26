mapreduce
=========

**Repository of MapReduce scripts that I wrote in Python for the Udacity course [Intro to Hadoop and MapReduce](https://www.udacity.com/course/ud617).** Each mapper script has a complementary reducer script. Together, the mapper and the reducer receive data from the standard input. These scripts can be used locally or they can create MapReduce jobs in Hadoop with [Hadoop Streaming](http://hadoop.apache.org/docs/r1.2.1/streaming.html). As detailed below, these scripts process data from one of three sources: data about users of and posts on Udacity's forums [[link](http://content.udacity-data.com/course/hadoop/forum_data.tar.gz)], web log data [[link](http://content.udacity-data.com/courses/ud617/access_log.gz)], and sales data from different stores [[link](http://content.udacity-data.com/courses/ud617/purchases.txt.gz)].

To run a mapper and a reducer on 100 lines of data and view the output on a Linux machine, try a command like the one below.
```head -100 ./example_data.txt | ./example_mapper.py | sort | ./example_reducer.py | less```

- **average_length_mapper.py** and **average_length_reducer.py** count the length of every question on Udacity's forum and compute the average length of the answers to each question, outputting the results in three columns: *question ID*, *question length*, and *mean answer length*. Questions without answers receive an average answer length of 0.

- **combine_mapper.py** and **combine_reducer.py** output information from *forum_node* about the posts in Udacity's forum and combine it with the reputation statistics of their authors from *forum_node*.

- **count_mapper.py** and **count_reducer.py** count the number of hits to the web pages referenced in the web log data, outputting the results in two columns: *web page* and *number of hits*.

- **inverted_index_mapper.py** and **inverted_index_reducer.py**

- **maximum_mapper.py** and **maximum_reducer.py**

- **maximum_item_mapper.py** and **maximum_item_reducer.py**

- **mean_mapper.py** and **mean_reducer.py**

- **popular_tags_mapper.py** and **popular_tags_reducer.py**

- **student_times_mapper.py** and **student_times_reducer.py**

- **study_groups_mapper.py** and **study_groups_reducer.py**
