
# spark, hadoop
# How would you design a system to hold a streaming database of billions of tweets, to allow for rapid querying?
# pascals triangle 

'''
A lot of simple SQL questions to find the top songs in a table etc.
garbage collection to distributed systems to monitoring/alerting.

Practice subqueries, joins, filtering, sorting, aggregations.

What is your experience in working with a particular technology such as SQL?
-> like counts, bookmark counts 
-> verifying on hive (runs over hadoop and provides sql interface for processing data)
-> Hadoop is an open source framework that helps to store, process and analyze a large volume of data 
-> HDFS is the distributed file system of Hadoop that provides high throughput data access

What is CAP Theorem in distributed computing?
How do you delete a linked list?

Is there something you feel you could’ve done better in your projects involving data?
Given an order table, write SQL queries to get the desired output.
'''

'''
Write a function that gives make the cth column of the rth row of pascal's triangle
'''
def generate(num_rows):
    triangle = []

    for row_num in range(num_rows):
        # The first and last row elements are always 1.
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, len(row)-1):
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

        triangle.append(row)

    return triangle


'''
Write a code to find the second largest number in an array.
-> heapq approach: O(n) time and space
-> ask can there be negative values in arr
'''
def second_largest(nums):
	if len(nums) < 2:
		return None 

    first, second = float('-inf'), float('-inf')
    for num in nums:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num

    return second 

'''
How would you scale it to a million records?
-> first reduce to set 
-> apply map reduce like processing xw
'''


'''
list files -> ls
move files -> mv <source> <destination>
rename file -> mv file1.txt file2.txt

'''


group by + having (count)
'''
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name
HAVING COUNT(*) > value;
'''

min/max
''' 
SELECT MIN (column_names) FROM table_name WHERE condition;
'''


order by
'''
SELECT * 
FROM table_name 
ORDER BY column1 ASC, column2 DESC;
'''


left outer join #all records from left and matched records from right table 
'''
SELECT column_name(s)
FROM table_1
LEFT JOIN table_2
ON table_1.column_name = table_2.column_name;
'''


inner join
'''
SELECT column_names 
FROM table1 
INNER JOIN table2 
ON table1.column_name=table2.column_name;

SELECT table1.column_name1, table2.column_name2, table3.column_name3 
FROM ((table1 INNER JOIN table2 ON relationship) 
INNER JOIN table3 ON relationship);
'''


full outer join
'''
SELECT column_names 
FROM table1 
FULL OUTER JOIN table2 
ON table1.column_name=table2.column_name;
'''


'''
ex. find the top songs in a table etc.
'''
select song_id, count(*)
from songs
group by song_id 
order by song_id desc 

'''
Given a list of user record, select out unique users in one city
'''




'''
join 2 tables together to label start/end of a track play , 
only when I proposed a working solution he diverted me to another solution that he had in mind all along, 
thinking it was better as it didn't require window functions, but it did require them. 
He just didn't know they are called window functions. Admittedly, the "Data Engineer" said he hasn't worked on spark in a while, and is quite junior.
'''
SELECT duration_seconds,
SUM(duration_seconds) OVER (ORDER BY start_time) AS running_total
FROM tutorial.dc_bikeshare_q1_2012


SELECT start_terminal, duration_seconds,
       SUM(duration_seconds) OVER
         (PARTITION BY start_terminal ORDER BY start_time)
         AS running_total,
       COUNT(duration_seconds) OVER
         (PARTITION BY start_terminal ORDER BY start_time)
         AS running_count,
       AVG(duration_seconds) OVER
         (PARTITION BY start_terminal ORDER BY start_time)
         AS running_avg
  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'




window functions
A window function performs a calculation across a set of table rows that are somehow related to the current row. 
















