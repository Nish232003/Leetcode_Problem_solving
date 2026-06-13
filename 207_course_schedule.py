# LeetCode 207: Course Schedule | Kahn's Algorithm (Topological Sort)

# Approach:
# We model courses and prerequisites as a directed graph.
# If the graph contains a cycle, it is impossible to finish all courses.

# 1. Build the graph:
#    - Create an adjacency list.
#    - Maintain an indegree array to count prerequisites for each course.

# 2. Find courses with no prerequisites:
#    - Add all courses with indegree 0 to a queue.

# 3. Process the queue:
#    - Remove a course from the queue.
#    - Count it as completed.
#    - Reduce indegree of its neighboring courses.
#    - If any neighbor's indegree becomes 0, add it to the queue.

# 4. Check completion:
#    - If completed courses == numCourses, return True.
#    - Otherwise, a cycle exists, return False.

# 5. Complexity:
#    - Time Complexity: O(V + E)
#    - Space Complexity: O(V + E)


from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:
            course = q.popleft()
            completed += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return completed == numCourses
