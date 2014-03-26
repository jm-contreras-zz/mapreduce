mapreduce
=========

**Repository of MapReduce scripts that I wrote in Python for the Udacity course [Intro to Hadoop and MapReduce](https://www.udacity.com/course/ud617), a course about Hadoop and how to write MapReduce programs.** Each mapper script has a complementary reducer script. Together, the mapper and the reducer receive data from the standard input. These scripts can be used locally or they can create MapReduce jobs in Hadoop with [Hadoop Streaming](http://hadoop.apache.org/docs/r1.2.1/streaming.html). As detailed below, these scripts process data from one of three sources: data about users of and posts on Udacity's forums [[link](http://content.udacity-data.com/course/hadoop/forum_data.tar.gz)], weblog data [[link](http://content.udacity-data.com/courses/ud617/access_log.gz)], and sales data from different stores [[link](http://content.udacity-data.com/courses/ud617/purchases.txt.gz)].

To run a mapper and a reducer on 100 lines of data and view the output on a Linux machine, try a command like the one below.

```head -100 ./example_data.txt | ./example_mapper.py | sort | ./example_reducer.py | less```

Forum Data
----------
- **average_length_mapper.py** and **average_length_reducer.py** count the length of every question and compute the average length of the answers to each question. Reuslts are output in three columns: (1) *question ID*, (2) *question length*, and (3) *mean answer length*. Questions without answers receive an average answer length of zero.

- **popular_tags_mapper.py** and **popular_tags_reducer.py** count the number of times each tag is applied to a post by its author and keep track of the *N*-most popular tags, where *N* = the number of tags to output. Results are output in two columns, sorted by popularity: (1) *tag* and (2) *number of posts with the tag*.

- **inverted_index_mapper.py** and **inverted_index_reducer.py** count the number of times a term appears in posts (e.g., 'fantastic') and keep track of the posts in which the term appears. Two results are output: (1) *term count* and (2) *list of posts in which the term appears*.

- **student_times_mapper.py** and **student_times_reducer.py** count the number of times that each user posts at the different hours of the day and finds the hour at which each user posted most often. Results are output in two columns: (1) *user ID* and (2) *hour with the most posts*. Hours that tie are output as different records.

- **study_groups_mapper.py** and **study_groups_reducer.py** create a list of the users who interacted via a question; that is, for each question, the list includes the ID of the user who asked the question and the IDs of the users who answered and the users who commented on the question and the answers. Results are output in two columns: (1) *question ID* and (2) *list of user IDs*.

- **combine_mapper.py** and **combine_reducer.py** output information from *forum_node* about the posts and combine it with the reputation statistics of their authors from *forum_node*.

Web Log Data
------------
- **count_mapper.py** and **count_reducer.py** count the number of hits to each webpage. Results are output in two columns: (1) *webpage* and (2) *number of hits*.

- **maximum_mapper.py** and **maximum_reducer.py** operate similarly, but they only output these results for the webpage with the most hits.

Sales Data
----------
- **maximum_item_mapper.py** and **maximum_item_reducer.py** find the highest price, across all stores, at which each item was sold. Results are output. Two results are output: (1) *item name* and (2) *price*.

- **mean_mapper.py** and **mean_reducer.py** compute the average item price, across all stores, on a given day of the week (e.g., Sunday). The only result that is output is *the mean item price*.
