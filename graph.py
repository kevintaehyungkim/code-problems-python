
########################
### ALIEN DICTIONARY ###
########################
'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
    Input:
    [
      "wrt",
      "wrf",
      "er",
      "ett",
      "rftt"
    ]
    Output: "wertf"

Example 2:
    Input:
    [
      "z",
      "x"
    ]

    Output: "zx"

Example 3:
    Input:
    [
      "z",
      "x",
      "z"
    ] 

    Output: "" 

Explanation: The order is invalid, so return "".


All approaches break the problem into three steps.

Extracting dependency rules from the input. 
For example "A must be before C", "X must be before D", or "E must be before B".
Putting the dependency rules into a graph with letters as nodes and dependencies as edges (an adjacency list is best).
Topologically sorting the graph nodes.

Time: O(C)
Space: O(1) or O(U + min(U^2,N) where U = unique letters and N = edges
'''

def alienOrder(self, words):
    graph  = {}
    for word in words:
        for c in word:
            graph[c] = set()
    
    
    for first, second in zip(words, words[1:]):
        print first, second
        for c,d in zip(first, second):
            print c, d
            if c !=d:
                graph[c].add(d)
                break
            else:
                if len(second)<len(first):
                    return ""
            
    visited  = {}
    checked = {}
    for word in words:
        for c in word:
            visited[c] = False
            checked[c] = False
    
    output = deque([])
    
    def topological_dfs(node):
        if checked[node]:
            return True
        
        # cycle detection
        if visited[node]:
            return False
        
        visited[node] = True
        
        ret = True
        for i in graph[node]:
            ret = topological_dfs(i)
            if not ret:
                break
        
        visited[node] = False
        checked[node] = True
        output.appendleft(node)
        return ret
    
    
    for key in graph.keys():
        if not topological_dfs(key):
            return ""
    
    return "".join(output)



#######################
### COURSE SCHEDULE ###
#######################
'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
is it possible for you to finish all courses?

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
'''
# time: O(V + E)
# spacE: O(V + E)
def can_finish(numCourses, prerequisites):
    graph = [[] for _ in xrange(numCourses)] #[[], []]
    visit = [0 for _ in xrange(numCourses)] #[0, 0]
    
    for x, y in prerequisites:
        graph[x].append(y)
    
    # base state: visit[i] = 0
    # if visited: visit[i] = -1
    # if visiting: visit[i] = 1
    def is_cycle(i):
        if visit[i] == 1:
            return False
        if visit[i] == -1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if is_cycle(j):
                return True
        visit[i] = 1
        return False
    
    for i in xrange(numCourses):
        if is_cycle(i):
            return False
    return True



######################################
### NUMBER OF CONNECTED COMPONENTS ###
######################################
'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to find the number of connected components in an undirected graph.


Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2


Example 2:
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

# DFS using recursion
# time: O(n)
# space: O(n)
def countComponents(n, edges):
    graph = collections.defaultdict(list)
    
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    count = 0
    visited = set()
    for node in range(n):
        if node not in visited:
            dfs(node, visited)
            count += 1
    return count

def dfs(node, visited):
    visited.add(node)            
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)



#############################
### RECONSTRUCT ITINERARY ###
#############################
'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. 
Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that 
has the smallest lexical order when read as a single string. 
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.

Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
'''

# key idea: DFS and add to stack until no more destination and reverse stack
# time: O(Elog(E/V)) -> DFS sort dominates, otherwise DFS -> O(E)
# space: O(V+E)
def findItinerary(tickets):
    graph = {}

    # Create a graph for each airport and keep list of airport reachable from it
    for start, dest in tickets:
        if start in graph:
            graph[start].append(dest)
        else:
            graph[start] = [dest]

    for src in graph.keys():
        graph[src].sort(reverse=True)
        # Sort children list in descending order so that we can pop last element 
        # instead of pop out first element which is costly operation
        
    stack = ["JFK"]
    res = []

    # Start with JFK as starting airport and keep adding the next child to traverse 
    # for the last airport at the top of the stack. If we reach to an airport from where 
    # we can't go further then add it to the result. This airport should be the last to go 
    # since we can't go anywhere from here. That's why we return the reverse of the result
    # After this backtrack to the top airport in the stack and continue to traaverse it's children
    
    while len(stack) > 0:
        elem = stack[-1]
        if elem in graph and len(graph[elem]) > 0: 
            # Check if elem in graph as there may be a case when there is no out edge from an airport 
            # In that case it won't be present as a key in graph
            stack.append(graph[elem].pop())
        else:
            res.append(stack.pop())
            # If there is no further children to traverse then add that airport to res
            # This airport should be the last to go since we can't anywhere from this
            # That's why we return the reverse of the result
    return res[::-1]


### WORD LADDER ### 
'''
A transformation sequence from word beginWord to word endWord using a 
dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. 

Note that beginWord does not need to be in wordList.
sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence from beginWord to endWord, 
or 0 if no such sequence exists.
'''

def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word) 
                
        bfs_queue = [(beginWord, 1)]
        visited = set()
        visited.add(beginWord)
        
        while bfs_queue:
            current_word, level = bfs_queue.pop(0)
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        bfs_queue.append((word, level + 1))
        return 0

