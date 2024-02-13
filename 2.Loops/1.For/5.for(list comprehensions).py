squares = [x ** 2 for x in range(10)]
print(squares)

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)

pairs = [(x, y) for x in range(3) for y in range(2, 5)]
print(pairs)
