def solve():
    N = int(input())
    numbers = list(map(int, input().split()))

    unique_numbers = set(numbers)
    print(len(unique_numbers))

solve()