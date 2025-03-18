numbers = {'a': 1, 'b': 2, 'c': -1}

print(numbers.items())

print(dict(sorted(numbers.items(), key=lambda m: m[1])))