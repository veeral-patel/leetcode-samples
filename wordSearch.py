from typing import Optional, List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False

        wordFirstLetter = word[0]

        # look for all possible starting locations (where character matches
        # the first character of the word)
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                letter = board[i][j]
                if letter == wordFirstLetter:
                    # and launch a search from each location
                    if self.wordSearchFromLocation(board, word, 0, i, j):
                        return True

    def wordSearchFromLocation(self, board, word, wordIndex, row, col):
        # check at the character at the location in the board is right
        c = word[wordIndex]
        if board[row][col] != c:
            return []

        # if at the end of the word, return True
        if wordIndex == len(word)-1:
            return [[row, col]]

        # search for rest of the characters
        if row < len(board)-1:
            res = self.wordSearchFromLocation(board, word, wordIndex+1, row+1, col)
            if res and [row, col] not in res:
                res.append([row, col])
                return res

        if row > 0:
            res = self.wordSearchFromLocation(board, word, wordIndex+1, row-1, col)
            if res and [row, col] not in res:
                res.append([row, col])
                return res

        if col < len(board[0])-1:
            res = self.wordSearchFromLocation(board, word, wordIndex+1, row, col+1)
            if res and [row, col] not in res:
                res.append([row, col])
                return res

        if col > 0:
            res = self.wordSearchFromLocation(board, word, wordIndex+1, row, col-1)
            if res and [row, col] not in res:
                res.append([row, col])
                return res

        return []

board = [["a","a"]]
word = "aaa"

sol = Solution()
sol.exist(board, word)
