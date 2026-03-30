import sys
from src.letter_combinations.solution import Solution

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <digits>")
        return
    
    digits = sys.argv[1]
    solution = Solution()
    output = solution.letter_combinations(digits)

    print(output)


if __name__ == "__main__":
    main()