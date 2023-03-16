class Solution:
    # Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        print(arr)
        if len(arr) == 1:
            return arr[0]

        if len(arr) == 2:
            output = []
            i, j = 0, 0
            while i < len(arr[0]) and j < len(arr[1]):
                if arr[0][i] < arr[1][j]:
                    output.append(arr[0][i])
                    i += 1
                else:
                    output.append(arr[1][j])
                    j += 1
            while i < len(arr[0]):
                output.append(arr[0][i])
                i += 1
            while j < len(arr[1]):
                output.append(arr[1][j])
                j += 1
            return output

        if len(arr) > 2:
            return self.mergeKArrays([
                self.mergeKArrays(arr[:len(arr) // 2], K),
                self.mergeKArrays(arr[len(arr) // 2 + 1:], K)
            ],
                K);


if __name__=="__main__":
    ob = Solution()
    merged = ob.mergeKArrays([[5, 9, 44],
                              [51, 65, 88],
                              [2, 79, 89]], 3)
    print(merged)