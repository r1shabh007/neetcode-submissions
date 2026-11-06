class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # check for cycles
        recs = {i: [] for i in range(numCourses)}
        checked = set()
        for a, b in prerequisites:
            recs[a].append(b)
        
        def dfs(course, seen):
            #base case 1
            if course in checked:
                return True
            
            # base case 2
            if course in seen:
                return False
            seen.add(course)

            # dfs with short circuiting
            for i in recs[course]:
                if not dfs(i, seen):
                    return False
            
            # otherwise true
            seen.remove(course)
            checked.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        return True