from typing import List


class Solution:

    digit_mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
    }

    def letter_combinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        result = []

        def backtrack(path: str ,index: int):
            if len(digits) == 0:
                result.append(path)
                return
            else:
                for char in self.digit_mapping[digits[index]]:
                    backtrack(path + char, index + 1)
        
        
        backtrack("", digits)
        return result

