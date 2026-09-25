def find_missing(numbers: list[int], n: int) -> int:
    total = sum(numbers)
    theorical_sum = n*(n+1)//2
    rest = theorical_sum - total
    return rest

numbers = [1, 2, 3, 4, 5]
n = 6
print(find_missing(numbers, n))
