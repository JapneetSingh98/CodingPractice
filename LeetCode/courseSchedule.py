class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def visit(cur):
            if (cur in finalVisited):
                return
            if (cur in initVisited):
                # cycle found
                return []

            initVisited[cur] = True
            for course in nextCourses.get(cur, []):
                if (visit(course) == []):
                    return []
            initVisited.pop(cur)
            finalVisited[cur] = True
            output.insert(0, cur)

        nextCourses = {}
        for pair in prerequisites:
            if (pair[1] not in nextCourses):
                nextCourses[pair[1]] = [pair[0]]
            else:
                nextCourses[pair[1]].append(pair[0])

        output = []

        finalVisited = {}
        initVisited = {}

        for i in range(numCourses):
            if (i in finalVisited):
                continue
            else:
                if (visit(i) == []):
                    return []

        return output