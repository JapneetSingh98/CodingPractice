class Solution:
    def helper(self, board, word, index, pos, visited):
        if index == len(word) - 1:
            return True
        (m, n) = pos
        # print(pos, index, visited)

        # top
        if m > 0 and (m - 1, n) not in visited and word[index + 1] == board[m - 1][n]:
            if self.helper(board, word, index + 1, (m - 1, n), visited + [(m, n)]):
                return True

        # bottom
        # print(visited)
        if m < len(board) - 1 and (m + 1, n) not in visited and word[index + 1] == board[m + 1][n]:
            if self.helper(board, word, index + 1, (m + 1, n), visited + [(m, n)]):
                return True

        # left
        # print(visited)
        if n > 0 and (m, n - 1) not in visited and word[index + 1] == board[m][n - 1]:
            if self.helper(board, word, index + 1, (m, n - 1), visited + [(m, n)]):
                return True

        # right
        # print(visited)
        if n < len(board[m]) - 1 and (m, n + 1) not in visited and word[index + 1] == board[m][n + 1]:
            if self.helper(board, word, index + 1, (m, n + 1), visited + [(m, n)]):
                return True

        else:
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        # for m in range(len(board)):
        #     print(board[m])
        for m in range(len(board)):
            for n in range(len(board[m])):
                if board[m][n] == word[0] and self.helper(board, word, 0, (m, n), []):
                    return True
        return False