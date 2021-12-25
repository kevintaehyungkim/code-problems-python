'''
You are a developer for a university. 
Your current project is to develop a system for students to find courses they share with friends. 
The university has a system for querying courses students are enrolled in, 
returned as a list of (ID, course) pairs.

Write a function that takes in a list of (student ID number, course name) pairs and returns, 
for every pair of students, a list of all courses they share.

Sample Input:
student_course_pairs = [
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"]
]

Sample Output (pseudocode, in any order)

find_pairs(student_course_pairs) =>
{
    [58, 17]: ["Software Design", "Linear Algebra"]
    [58, 94]: ["Economics"]
    [17, 94]: []
}  
'''

def find_pairs(student_course_pairs):

    student_ids = set()
    student_pairs = []
    course_students = {}

    for pair in student_course_pairs:
        student, course = int(pair[0]), pair[1]
        if student not in student_ids:
            student_ids.add(student)
            for 
        course_students

'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
'''

'''
A graph question. Find the furthest ancestor of a node.  
'''

# go through each node - DFS


# time: O()
def find_furthest(nodes):

    furthest_ancestor = ("", "", 0)
    current_node = ""
    # visited_edges = set()
    visited_nodes = set()

    def dfs(start, curr_node, dist):
        for 

    for node in node:
        dfs(node, node, 0)

    return furthest_ancestor






