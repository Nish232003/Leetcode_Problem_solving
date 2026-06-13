# LeetCode 210: Course Schedule II | Kahn's Algorithm (Topological Sort)

# Approach:
# We model courses and prerequisites as a directed graph.
# A valid course order is a topological ordering of the graph.
# If a cycle exists, no valid ordering is possible.

# 1. Build the graph:
#    - Create an adjacency list.
#    - Maintain an indegree array to count prerequisites.

# 2. Find courses with no prerequisites:
#    - Add all courses with indegree 0 to a queue.

# 3. Process the queue:
#    - Remove a course from the queue.
#    - Add it to the result.
#    - Reduce indegree of its neighboring courses.
#    - If any neighbor's indegree becomes 0, add it to the queue.

# 4. Check completion:
#    - If result contains all courses, return it.
#    - Otherwise, a cycle exists, return an empty list.

# 5. Complexity:
#    - Time Complexity: O(V + E)
#    - Space Complexity: O(V + E)


from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        order = []

        while q:
            course = q.popleft()
            order.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return order if len(order) == numCourses else []
