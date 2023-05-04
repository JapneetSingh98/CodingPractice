class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        visited = {}

        for num in nums:
            if (num in visited):
                continue
            # stand alone number
            elif (num - 1 not in visited and num + 1 not in visited):
                visited[num] = 1
                maxSeq = max(maxSeq, 1)

            # number on either side
            elif (num - 1 in visited and num + 1 in visited):
                newLength = visited[num - 1] + 1 + visited[num + 1]
                visited[num - visited[num - 1]] = newLength
                visited[num - 1] = newLength
                visited[num + visited[num + 1]] = newLength
                visited[num + 1] = newLength
                visited[num] = newLength
                maxSeq = max(maxSeq, newLength)

            # number on left side
            elif (num - 1 in visited):
                newLength = visited[num - 1] + 1
                visited[num - visited[num - 1]] = newLength
                visited[num - 1] = newLength
                visited[num] = newLength
                maxSeq = max(maxSeq, newLength)

            # number on right side
            else:
                newLength = 1 + visited[num + 1]
                visited[num + visited[num + 1]] = newLength
                visited[num + 1] = newLength
                visited[num] = newLength
                maxSeq = max(maxSeq, newLength)

        return maxSeq