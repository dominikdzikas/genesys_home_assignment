from src.letter_combinations.solution import Solution


def test_two_digits() -> None:
    solution = Solution()
    assert solution.letter_combinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def test_zero_digits() -> None:
    solution = Solution()
    assert solution.letter_combinations("") == []

def test_one_digits() -> None:
    solution = Solution()
    assert solution.letter_combinations("2") == ["a","b","c"]
